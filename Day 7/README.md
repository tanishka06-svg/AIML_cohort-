# Python Libraries and NumPy

## Introduction

Python provides many libraries that make programming easier. Libraries can be used for different tasks 

## Python Libraries

### Why We Use Libraries

- Libraries provide ready-made functions and tools.
- They save time and reduce the amount of code.
- They make complex tasks easier.
- Different libraries are useful for different types of work.

### Common Uses of Python Libraries

- Mathematical calculations
- Data preprocessing
- Training machine learning models
- Data visualization
- Working with dates and time
- Working with databases
- File handling

## Math Module

- math is a built-in Python module.
- It provides functions for mathematical calculations.


## NumPy

### Introduction to NumPy

- NumPy stands for Numerical Python.
- It is used for numerical calculations.
- NumPy provides arrays for storing and processing numerical data.


## Lists and Arrays

### Python List

- A list can store multiple elements.
- A list can contain different types of data.

### NumPy Array

- A NumPy array is mainly used for numerical data.
- Arrays are useful for mathematical operations.
- NumPy allows operations to be performed on multiple elements efficiently.

## NumPy Array Operations

### Creating an Array

- `np.array()` is used to create a NumPy array.
- It can convert a Python list into a NumPy array.

## NumPy Functions

### np.zeros()

- Creates an array filled with zeros.
- The number of elements can be specified.

### np.ones()

- Creates an array filled with ones.
- The number of elements can be specified.

### np.arange()

- Creates an array of values within a specified range.
- A step value can also be provided.

### np.sum()

- Returns the sum of all elements in an array.

### np.mean()

- Returns the average of the elements in an array.

### np.max()

- Returns the maximum value from an array.

## Array Indexing

### Accessing Elements

- NumPy arrays use indexing to access elements.
- Indexing starts from 0.
- The first element has index 0.
- Elements can be changed using their index.

### Two-Dimensional Array

- A two-dimensional array contains rows and columns.
- The first index represents the row.
- The second index represents the column.
- Both indexes are separated by a comma.

## Array Shape

### shape

- The shape property gives the dimensions of an array.
- For a two-dimensional array, it gives the number of rows and columns.
- For example, `(2, 3)` means 2 rows and 3 columns.

## urllib Module

### Introduction

- urllib  is a built-in Python module.
- It is used to work with URLs.
- It can be used to access web resources.

### urllib.request

- urllib.request provides functions for opening URLs.
- urlopen() can be used to send a request to a URL.
- The response contains information received from the website.

### Response Status

- response.status gives the HTTP status code.
- Status code 200 generally means the request was successful.

## Requests Module

### Introduction

- Requests is a third-party Python library.
- It is used to send HTTP requests.
- It provides simpler syntax compared to urllib.

## GET Request

### requests.get()

- `requests.get()` is used to send a GET request.
- GET is generally used to retrieve data from a website or API.
- The response can be stored in a variable.

### Response Object

- The response object contains information received from the server.
- It provides details such as status code and response content.

## Response Properties and Methods

### response.status_code

- Gives the HTTP status code.

### response.text

- Returns the response content as text.
- It is useful when the server returns HTML or other text-based content.

### response.raise_for_status()

- Checks whether the request was successful.
- Raises an exception if an HTTP error occurs.

### response.json()

- Converts a valid JSON response into Python data.
- It is commonly used when working with APIs.
- It should only be used when the server returns valid JSON.

## POST Request

### requests.post()

- requests.post() is used to send data to a server.
- POST requests are commonly used when submitting or creating data.
- Data can be sent using the json parameter.

### Sending JSON Data

- The json parameter is used to send data in JSON format.
- The data is usually stored in a Python dictionary.
- The API receives the dictionary as JSON data.

## GET and POST

### GET

- Used mainly to retrieve data.
- Commonly used when requesting information from an API.

### POST

- Used mainly to send data.
- Commonly used when submitting or creating information.

## APIs

### Introduction

- API stands for Application Programming Interface.
- An API allows different applications to communicate with each other.
- APIs commonly provide data in JSON format.
- Python Requests can be used to communicate with APIs.

## Summary
 - We learned Python libraries, NumPy, urllib, and Requests.
 - Making GET and POST requests, checking response status, reading response text, handling JSON data.