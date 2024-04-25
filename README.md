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

#### Implementation:
PyCharm: Used as the Integrated Development Environment (IDE) for writing, testing, and debugging the code. PyCharm provides tools for managing Python projects, including code analysis, a graphical debugger, a testing runner, and integration with version control systems.


## Operations

### Scrapy file:
Initiated the project by using the following command - 
```
scrapy startproject chicago_crawler
```
Within the project, the ``` ChicagoWikiSpider ``` class was created in a file named ``` chicagospider.py ```. This spider is responsible for crawling the Chicago Wikipedia page. The code defines the spider's behavior, including the URLs to start with, the allowed domains, and settings like depth limit and auto-throttling to manage the request rate. To execute the spider and begin crawling, the command - 
```
scrapy crawl chicago_wiki
```
This was used from the terminal within the project directory. This command triggers the spider to start processing the URLs defined in ``` start_urls ```.

### Indexer:

1. The script starts by opening and reading the ``` chicago_data.json ```  file using Python's built-in json module, which converts the JSON formatted data into Python dictionaries.

2. HTML Parsing; Utilizes ``` BeautifulSoup ``` from the ``` bs4 ``` package to parse HTML content and extract plain text.

3. A ``` TfidfVectorizer ``` object from ``` scikit-learn ``` is created to transform the cleaned text into a TF-IDF matrix. This matrix represents the text data in a form that is suitable for information retrieval and similarity calculations.

4. The vectorizer and the TF-IDF matrix are serialized using Python's pickle module and saved into .pkl files. These files (``` vectorizer.pkl ``` and ``` tfidf_matrix.pkl ```) can be used later for loading the vectorization model and matrix quickly without needing to reprocess the data.

5. All of this was ran under the ``` tfidf_vectorizer.py ``` file.

To run the script and handle its dependencies, you should have the following Python packages installed: json, re, pickle, numpy, BeautifulSoup, scikit-learn. I used the following terminal command to install it- 
```
pip install numpy beautifulsoup4 scikit-learn
```

### Flask Processor:
1. The script begins by loading the pre-trained TF-IDF vectorizer and the corresponding matrix using Python’s pickle module. These files are essential for transforming new queries into the same vector space as the indexed documents. Additionally, it loads the original document data from a JSON file, which contains metadata and content related to each indexed document.
2. The search function takes a query and an optional parameter top_k to determine how many results to return. It transforms the query into a vector, calculates cosine similarities with the indexed documents, and sorts these to return the top results.
3. Home Route (/): A simple HTML form is served that allows users to input search queries.
Search Route (/search): Handles the logic for receiving search queries via POST or GET, processes them using the search function, and returns the results in JSON format. This route also handles error conditions like empty queries.
4. Ensure Python3 is installed using the following command :
``` 
python -m venv venv
source venv/bin/activate  # On Unix or macOS
venv\Scripts\activate  # On Windows
```
5. Use this command to install all the libraries - 
```
pip install Flask numpy scikit-learn
```

## Conclusion

#### Outputs:
The project outputs include:
* JSON File: Containing the scraped data from Wikipedia, structured and ready for processing.
* Pickle Files: Including the saved TF-IDF vectorizer and matrix, which are crucial for processing and responding to search queries.
* Web Application: A functioning web interface that allows users to enter queries and view the search results in real time.

  For the web application and running the search query, run the flask_installer.py file, it will show you the following output -

<img width="989" alt="image" src="https://github.com/mehal-gosalia/CS429_IR_Project/assets/118829943/d9655438-7e6f-4c41-9539-e0fda98bc866">

Click on the link shown - ``` http://127.0.0.1:5000 ```

it will lead you to a page on chrome/ any web browser of your choice and show this:
<img width="1271" alt="image" src="https://github.com/mehal-gosalia/CS429_IR_Project/assets/118829943/6fc89ed6-c6fb-4308-8af1-61a7e2d42bd0">

Then enter your search query, for example if I enter 'Architecture' it shows me this output:

<img width="1019" alt="image" src="https://github.com/mehal-gosalia/CS429_IR_Project/assets/118829943/db0cecf5-1458-4a1d-8336-94df4990b4a1">


#### Caveats and Cautions:
* The current system is designed for a relatively small dataset and might not perform well with significantly larger data volumes. Scaling the system to handle more extensive data or higher query volumes would require optimizations such as implementing more efficient data structures or moving to more robust infrastructure.
* The Flask application is running in debug mode, which is not suitable for production environments. Additionally, the handling of user input should be thoroughly validated to prevent security vulnerabilities, such as SQL injection or cross-site scripting (XSS).
*  While the scraper and indexer function well with the structured data from Wikipedia, they may not perform as effectively with poorly structured or more diverse content sources without further refinement of the data extraction and processing techniques.

## Data Sources
All of my data is from the Chicago Wikipedia page : ``` https://en.wikipedia.org/wiki/Chicago ```

## Test Cases
Setup and teardown processes prepare and clean the test environment, ensuring isolated conditions for each test case. The test harness executes functionality and edge case tests, utilizing Flask’s test client to simulate HTTP requests and verify the responses. Coverage includes verifying the crawler’s data fetching and storage, the indexer's accurate text transformation and serialization, the Flask app’s route handling and security, as well as overall system integration to ensure end-to-end functionality. This rigorous testing ensures the system performs reliably under various scenarios, preparing it for future enhancements and scalability.

## Source Code
This project's source code is all open-source and compliant with MIT licensing; comprehensive documentation is included for every part of the code.

## Bibliography
* Open AI for some help with terminal commands to install packages and stuff.
* Chicago Wikipedia Page
* Professor. Panchal and the TA's (Special thanks!)
