# Automated Grading System

## Overview
This Automated Grading System leverages advanced natural language processing (NLP) techniques to provide efficient and accurate grading of student responses. Developed using PyTorch, the system utilizes a BERT-based sentence transformer, attention masking, Kmeans clustering, and cosine similarity to analyze, group, and grade submissions.

## Features
- **PyTorch Implementation**: Utilizes PyTorch for efficient NLP operations.
- **BERT-based Sentence Transformer**: Analyzes student responses using a transformer model based on BERT.
- **Attention Masking**: Enhances accuracy by focusing on crucial elements in the responses.
- **Kmeans Clustering**: Groups similar student submissions for consistent grading.
- **Cosine Similarity**: Measures the similarity between responses for precise grading.

## Technologies and Skills
- **Streamlit**: Designed the front-end using Streamlit framework in Python to create a simple user interface for teachers and students.
- **Python**: Utilized for backend development and integration.
- **Neural Language Models**: Implemented using PyTorch and BERT architecture.
- **SQL**: Managed student data and grading information.
- **Machine Learning**: Applied for clustering and grading algorithms.
- **Natural Language Processing (NLP)**: Core technology for analyzing student responses.
- **PyTorch**: Framework for building and training neural language models.

## File Descriptions
- `Backend.py`: Contains the backend logic for the web application.
- `Gen.py`: Script for generating data or models.
- `database.py`: Manages database interactions and operations.
- `main.py`: Entry point for running the web application.
- `students.db`: SQLite database file storing student data.
- `answers.txt`: Sample answers or reference answers for grading.
- `README.md`: Documentation file for the project.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ayushsinghal021/automated-grading-system.git
    cd automated-grading-system
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the web application:
    ```bash
    streamlit run main.py
    ```
2. Access the application through the provided local URL.
3. Follow the on-screen instructions to upload student responses and view grading results.

## Screenshots

1. User can proceed as Teacher or Student
   ![image](https://github.com/ayushsinghal021/Automated-Grading-System/assets/64143038/5a1d3752-802b-4d5d-9ac2-f992aad0f7b4)
   ![image](https://github.com/ayushsinghal021/Automated-Grading-System/assets/64143038/8be56164-6122-4f4b-b056-fdca7e7a24f9)

2. Teacher is prompted for the correct answer
   ![image](https://github.com/ayushsinghal021/Automated-Grading-System/assets/64143038/07319e05-6c26-4568-84a7-5ab5f5b4d6d2)
   
3. Teacher can add a new student
   ![image](https://github.com/ayushsinghal021/Automated-Grading-System/assets/64143038/11e57d45-6b83-4d79-9c9e-6ccaadfe5e4b)

4. Student is prompted to select name and subject and upload the answer in pdf format. The model evaluates the grade on the basis of the correct answer from teacher.
   ![image](https://github.com/ayushsinghal021/Automated-Grading-System/assets/64143038/a07c323d-96e2-40a6-b9ed-52a6ccc7c253)
