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
