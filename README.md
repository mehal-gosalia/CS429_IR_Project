# Chicago Wikipedia Search Engine

## Abstract

The project aims to develop a comprehensive system to index and search documents using a TF-IDF (Term Frequency-Inverse Document Frequency) model based on data scraped from the Chicago Wikipedia page. The system utilizes a Python-based web crawler (Scrapy), an indexer (Scikit-Learn), and a Flask-based web application to enable users to perform searches with cosine similarity scoring. Future enhancements include expanding data sources, implementing advanced NLP features for search optimization, and enhancing the user interface for broader access.

## Overview

The system was designed to extract, index, and search textual data from the web efficiently. The literature on information retrieval systems guided the design choices, including the use of TF-IDF and cosine similarity, which are well-established methods in the field. The proposed system comprises three main components: a web crawler, an indexer, and a query processor.

## Design

#### System Capabilities:
* Web Crawling: Dynamically scrapes data from specified URLs.
* Indexing: Processes and indexes the text using TF-IDF.
* Search: Allows users to query the indexed data and retrieves relevant results based on cosine similarity.

#### Interactions
* Users input search queries via a web interface.
* The system processes these inputs and displays search results.

#### Interaction
* The crawler feeds data into the indexer.
* The indexer updates the search database, which is queried by the Flask application.

## Architecture
#### Software Components: 
* Scrapy: Used for crawling web pages. This component handles the retrieval of data from the Chicago Wikipedia page and any related pages, based on predefined settings such as depth limit and page count.
* Scikit-Learn:  Employs this library to construct the TF-IDF model, which is essential for converting text data into a vectorized format that can be used for efficient indexing and similarity calculations.
* Flask: Serves as the backend framework for the web application, managing HTTP requests and responses. Flask enables the creation of web endpoints that users can interact with to submit search queries and receive results.
* BeautifulSoup: Utilized for parsing HTML content and extracting clean text, which is then processed by the indexer.
* NumPy: This library is used for handling large arrays and matrices of numerical data, crucial for the operations involving cosine similarity calculations in the search functionality.
* Pickle: Python’s built-in persistence model, used for saving and loading the TF-IDF model and the corresponding matrix from the disk, enabling quick reloads between sessions without reprocessing the data.

#### Interfaces:
* JSON files for data interchange between components.
* Pickle files for persisting Python objects (TF-IDF model and matrix).

####Implementation:
PyCharm: Used as the Integrated Development Environment (IDE) for writing, testing, and debugging the code. PyCharm provides tools for managing Python projects, including code analysis, a graphical debugger, a testing runner, and integration with version control systems.

