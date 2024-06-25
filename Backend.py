import numpy as np
import torch
from torch import nn
from sentence_transformers import SentenceTransformer

def softmax(x):
  return (np.exp(x).T / np.sum(np.exp(x), axis=-1)).T

def scaled_dot_product_attention(q, k, v, mask=False):
  d_k = q.shape[-1]
  scaled = np.matmul(q, k.T) / np.sqrt(d_k)
  #print(scaled.shape)
  if mask:
    mask=np.tril(np.ones(scaled.shape))
    mask[mask == 0] = -np.inf
    mask[mask == 1] = 0
    scaled = scaled + mask
  attention = softmax(scaled)
  out = np.matmul(attention, v)
  return out, attention

def qkv_declarer(embeddings):
    from Gen import MyModel
    gen = MyModel()
    gen.load_state_dict(torch.load('/Users/ajaychawla/Downloads/gen.pt'))
    gen.eval()
    return gen(embeddings)

def precedence_generator(text):
    sentences=text.replace('\n','.').split('.')
    
    while ('' in sentences):
        sentences.remove('')
        
    #model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    
    embeddings = model.encode(sentences)
    new=np.array(embeddings)
    
    q, k, v = qkv_declarer(torch.from_numpy(new).type(torch.float32))
    values, attention = scaled_dot_product_attention(q.detach().numpy(), k.detach().numpy(), v.detach().numpy(), True)
    temp2=attention                                             #temp2 creates a duplicate copy of attention
    l=np.argsort(temp2[-1])                                     #temp2[-1] calls last element and argsort provides indices to sort it, this is stored in l
    c=1                                                         #precedence counter
    list_of_imp_sentences=[]
    precedence_score={}                                         # precedence of each sentence corresponding to their index number
    for i in l[::-1]:                                           #Read argsort array in reverse order
        #print(c, "--> ",sentences[i],"\v",i)
        list_of_imp_sentences.append(sentences[i])
        #print("------------")
        precedence_score[i]=c
        c+=1
    return precedence_score, sentences

def evaluator(user_sentences, centres, precedence_score):
    from sentence_transformers import SentenceTransformer
    from sklearn.cluster import KMeans
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    
    # Load a pre-trained sentence transformer model
    model = SentenceTransformer('all-mpnet-base-v2')
    
    # Sample sentences (centroids)
    centroids = centres
    
    # Additional sample sentences (points around centroids)
    additional_sentences = user_sentences
    
    # Combine centroids and additional sentences
    sentences = centroids + additional_sentences
    
    # Encode sentences into numerical vectors
    sentence_embeddings = model.encode(sentences)
    
    # Number of centroids
    num_centroids = len(centroids)
    
    # Specify the number of clusters (equal to the number of centroids)
    k = num_centroids
    
    # Initialize KMeans model
    kmeans = KMeans(n_clusters=k, init=np.array(sentence_embeddings[:num_centroids]))
    
    # Fit KMeans model to sentence embeddings
    kmeans.fit(sentence_embeddings)
    
    # Get cluster labels
    labels = kmeans.labels_
    
    scoring_list=[]
    weight_list=[]
    # Compute cosine similarity between each centroid and sentences in its cluster
    for i, centroid in enumerate(centroids):
        cluster_indices = np.where(labels == i)[0]  # Indices of sentences in the cluster
        cluster_sentences = [sentences[idx] for idx in cluster_indices]  # Sentences in the cluster
        centroid_embedding = model.encode([centroid])  # Embedding of the centroid
    
        # Compute cosine similarity between centroid and sentences in the cluster
        similarities = cosine_similarity(centroid_embedding, model.encode(cluster_sentences))
        #print(f"Centroid: {centroid}")
        c=0
        l=[]
        for j, sentence in enumerate(cluster_sentences):
            #print(f"Similarity with sentence '{sentence}': {similarities[0][j]}")
            if c!=0:
                #print(precedence_score[user_sentences.index(sentence)])
                #print()
                l.append(len(user_sentences)-precedence_score[user_sentences.index(sentence)]+1)
            else:
                c+=1
        scores=np.delete(similarities[0], 0)
        #print("\t", l, scores ,"\n\n")
        if len(scores)>0:
            weight_list.append(l[scores.argsort()[::-1][0]])
            scoring_list.append(l[scores.argsort()[::-1][0]]*scores[scores.argsort()[::-1][0]])
        #print("-" * 50)
    final_value = np.sum(np.array(scoring_list))/np.sum(np.array(weight_list))
    return final_value

def grader(student):
    f=open('/Users/ajaychawla/Downloads/complete_app/answers.txt')
    teacher = f.read()
    teacher.replace("\u2060","")
    centres = teacher.replace('\n','.').split('.')
    for i in centres:
        if i=='':
            centres.remove(i)
    f.close()
    precedence_score, sentences = precedence_generator(student)
    score = evaluator(sentences, centres, precedence_score)

    if score<=1 and score>0.8:
        return 'A'
    elif score<=0.8 and score>0.6:
        return 'B'
    elif score<=0.6 and score>0.4:
        return 'C'
    elif score<=0.4 and score>0.2:
        return 'D'
    else:
        return 'F'