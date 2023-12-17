# CMPE255-Project-Clustering-Research-Paper-Abstracts

## Overview
This project is a part of CMPE 255 (Data Mining) and focuses on clustering research paper abstracts. The primary objective is to develop a system capable of effectively grouping abstracts based on their content. This system aims to facilitate easier navigation and discovery within large datasets of academic papers. The approach likely involves data mining techniques and algorithms for clustering text data, specifically abstracts of research papers, to identify and categorize similar topics or themes.

## Methodology:

- The project focuses on unsupervised clustering of scientific papers using sentence embeddings of abstracts.
- Various word embedding algorithms (GloVe, Word2Vec, FastText) and sentence embedding techniques (Concatenated Power Means, Universal Sentence Encoder) are utilized.
- Clustering algorithms like K Means, MiniBatch K Means, and spectral clustering are employed.
- The effectiveness of clustering is measured using Silhouette Score and Davies Bouldin Score metrics.

## Technologies Used:

- Word Embedding Algorithms: GloVe, Word2Vec, and FastText.
- Sentence Embedding Techniques: Concatenated Power Means and Universal Sentence Encoder.
- Clustering Algorithms: K Means, MiniBatch K Means, and spectral clustering.
- Evaluation Metrics: Silhouette Score and Davies Bouldin Score.

## Project Resources
- **Project Report**: [CMPE-255-Report.pdf](https://github.com/AtharvaJadhav/CMPE255-Project-Clustering-Research-Paper-Abstracts/blob/main/CMPE-255-Report.pdf)
- **Presentation**: [CMPE-255 Final Project.pptx](https://github.com/AtharvaJadhav/CMPE255-Project-Clustering-Research-Paper-Abstracts/blob/main/CMPE-255%20Final%20Project.pptx)
- **Presentaion Recording**: [Final_Project_recording.mp4](https://github.com/AtharvaJadhav/CMPE255-Project-Clustering-Research-Paper-Abstracts/blob/main/Final_Project_recording.mp4)

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x

## Conclusion:
- Traditional clustering techniques (Co-Citation Analysis, Bibliographic Coupling, Direct Citation relations) and NLP methods (keyword-based approaches, LSI, LDA) were found to be more effective for unsupervised clustering of research papers compared to the proposed method.
- The proposed method of unsupervised clustering using Concatenated Power Means and Centroids didn't achieve sufficient statistical scores for viability in unsupervised clustering of research papers, though it showed promise for supervised clustering.
- A key challenge with sentence embeddings is their high-dimensional representation, which, while beneficial for tasks like classification and sentiment analysis, complicates clustering due to the spatial distribution of data points.

## Future Scope:
- Investigate the use of reduced-size word and sentence embeddings for clustering, alongside dimensionality reduction techniques such as PCA, normalization, and scaling.
- Explore the use of Doc2Vec or similar models to represent entire documents, offering a more comprehensive analysis than just using abstracts or titles.
- Experiment with advanced neural network-based sentence embedding models like the Universal Sentence Encoder or Infersent to potentially improve clustering accuracy.
- Test the Concatenated Power Means method on labeled datasets for supervised clustering to develop more robust comparison metrics.
- Focus on reducing the dimensions of representation embeddings, enabling rapid distribution fingerprinting and enhancing clustering efficiency.

