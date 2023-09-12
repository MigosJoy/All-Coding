# Python for Data Science, AI and Development

Jason Head

### Course 4 of the IBM DS Specialization

https://www.coursera.org/learn/python-for-applied-data-science-ai?specialization=ibm-data-science

[Python Cheat Sheet from Course](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/handouts/Python%20Cheat%20Sheet%20-%20The%20Basics%20Coursera.pdf)

* Describe Python Basics including Data Types, Expressions, Variables, and Data Structures.
* Demonstrate proficiency in using Python libraries such as Pandas, Numpy, and Beautiful Soup.
* Apply Python programming logic using Branching, Loops, Functions, Objects & Classes.
* Access web data using APIs and web scraping from Python in Jupyter Notebooks.  

#### Week 1 Python Basics

* Demonstrate an understanding of types in Python by converting or casting data types such as strings, floats, and integers.
* Interpret variables and solve expressions by applying mathematical operations.
* Describe how to manipulate strings by using a variety of methods and operations.
* Build a program in JupyterLab to demonstrate your knowledge of types, expressions, and variables.
* Work with, manipulate, and perform operations on strings in Python.

#### Notes

Types: How python represents different types of data. Integers, real numbers or words.

Expressions and Variables
* Expressions: Mathematical Operations
  * Use // for integer division (round down)
* Variables: We use variables to store values

String Operations
* String: A sequence of characters, can be spaces or digits or special characters. We can bind a string to a variable
* The last element of a string is given by index [-1]
* Name = "Michael Jackson"
    * *Slicing*
        * Name[0:4] = Mich
        * Name[8:12] = Jack
    * *Striding*
        * Name[::2] = Every 2nd value; "McalJcsn"
        * Name[0:5:2] = Every 2nd value up to index 4
* Statement = Name + "is the best"
* Statement = "Michael Jackson is the best"
* Strings are immutable
*  " \ " are meant to proceed escape sequences. Escape sequences are strings that are difficult to input.
    * " \n " represent a new line. print("Michael Jackson /n is the best")
        * Michael Jackson
        *  is the best
    * " \t " represents a new tab
    * Use " \\ " to place a backslash IN your string

String Methods
* Sequence Methods: Work on lists and tuples
* String Methods: Only work on strings
    * *Method*
        * ex: B = A.upper()
        * ex: B = A.replace('Michael','Janet') 

 

 

#### Week 2 Python Data Structures

Lists and Tuples: Compound Data Types 
* Tuples: An ordered sequence. Tuples are written as comma-separated elements within parentheses. All different types can be contained in a tuple.
    * Tuple1 = ("disco",10,1.2)
        * Tuple1[0] = "disco"
        * Tuple1[1] = 10
        * Tuple1[2] = 1.2
    * Tuples are immutable (it can't be changed). If you want to manipulate a tuple, you must create a new tuple instead.
    * A Tuple can contain other tuples as well. This is called *Nesting*. The same indexing logic applies.
        * NT = (1,2("pop","rock"),(3,4),("disco",(1,2)))
        * NT[2]:("pop","rock")[1] = "rock" => NT[2][1] = "rock"
     
* Lists: Also ordered sequences. Represented with square brackets. One key differences with tuples are that lists are mutable. Tuples can be nested within lists. The same indexing conventions apply
    * L = ["Michael Jackson",10.1,1982]
    * Using extend adds all elements of a new list to current list and append adds everything as one element.
    * Multiple names referring to the same object is known as aliasing
    * Where A and B reference the same list (A = list | B = A), changing an element in list A will also change that element in B.
    * Where A is a list and B is a variable equal to the *clone* of the list of A (B = A[:]), changing an element in list A will **not** change that element in B.
 
Dictionaries: A type of collection in python. 
* Where a lists consists of indexes (can be like addresses and are integers) and elements, a dictionary has keys (can be like addreses but don't have to be integers, they are usually characters) and values (similar to elements).
    * Dictionaries are denoted with curly bracket {}
    * The keys are the first elements, they must be immutable and unique
    * Each key is followed by a value separated by a colon
    * Values can be immutable, mutable and duplicates
    * Each key and value pair is separated by a comma
* DICT.keys() = all keys
* DICT.values() = all values

Sets: A type of collection in python. 
* Like lists and tuples you can input different python types.
    * Unlike lists and tuples, they are unordered. This means sets do not record element position
    * Sets only have unique elements. This means there is only one of a particular element in a set
    * define using curly brackets {}
    * Set1 = {"pop","rock","soul","rock"} => Set1 = {"pop","rock","soul"}
    * Convert list to set by using function = set() > *typecasting*
    * Use add() to add an element to a set. If there is a duplicate of that element already, nothing will be added
    * Use remove() to remove an element from a set
    * In python we use " & " to find the intersection of two sets. The new set will only contain the elements that were present in both sets
    * In python we use union() to find the union of two sets. The new set will contain all unique elements that were present in both sets
    * Use issubset() to understand if a set is a subset of another set. TRUE or FALSE
  

#### Week 3 Python Programming Fundamentals

Conditions and Branching
* Comparison operations: Compare and produce a boolean
* Branching allows us to run different statements for a different input
    * elif: Allows us to check for additional conditions if the preceding condition is false
* Logic Operators: Take boolean values and produce different boolean values
    * not() / or() -- or() only produces false if all boolean values are false / and() -- and() only produces true is all boolean values are true

Loops
* *range*: Outputs an ordered sequence as a list *i*. If the input is a positive integer, the output is a sequence. The sequence contains the same number of elements as in input. Starts at 0. range(3) => [0,1,2] / range(10,15) => [10,11,12,13,14]
* for loops: Loops perform a task over and over. Ex; For square 0 in squares, square 0 = white square / For square 1 in squares, square 1 = white square
    * for i in range(0,5):
          squares[i] = 'white'
    * for i,x in enumerate(['A','B','C']):
        print(i,x)
      0 A
      1 B
      2 C
* while loops: Similar to for loops but while loops only run while the condition is met
    * squares = ['orange','orange','purple']
      newsquares = []
      i = 0
      while(squares[i] == 'orange'):
          newsquares.append(squares[i])
          i = i + 1

Functions
* Take some input, then produce some output or change. A function is just a piece of code you can reuse. Functions take an input and produce a new output.
    * def add1(a):
          b = a + 1
          return b
* A function can have multiple parameters
    * def Mult(a,b):
          c = a * b
          return c
    * Mult(2,3)
      6
* The multiplication symbol (*) can also mean to repeat a sequence
* If your function has no return statement, you can treat it as if the function returns nothing at all
    * def MJ():
          print('Michael Jackson')
      MJ()
      'Michael Jackson'
    * def NoWork():
          pass
      print(NoWork())
      None
* Collecting Arguments
* Scope: Variables defined outside of any function are said to be within the global scope, meaning they can be accessed anywhere after they are defined. A variable defined in the global scope is called a global variable. After a value is returned the scope of the function is deleted.
* Local variables only exist within the scope of a function.
    * Ex: When we call a function, we create a new scope. Within the scope of that function, the value of the date is set to 1982. The value of date does not exist within the global scope. Variables in side the global scope can have the same name as variables in the local scope with no conflict.
    * If a variable is not defined within the function, python will check the global scope.
    * If we define a variable within a function with the keyword global, the variable will be a global variable
 
Exception Handling
*  Try...Except...Else...Finally : This type of statement will first attempt to execute the code in the "try" block, but if an error occurs it will kick out and begin searching for the exception that matches the error. Once it f inds the correct exception to handle the error it will then execute that line of code.

Objects and Classes
* Python has many different **types**. In python each one is an *object*.
    * Every object has:
        * a type
        * an internal data representation (a blueprint)
        * a set of procedures for interacting with the object (methods)
    * An object is an instance of a particular type
    * You can find the type of an object by using the command type()
        * type([1,2,3]) => class 'list'
* A type's methods are functions that every instance of that class or type provides
    * It's how you interact with the data in a object.
    * Call the method by adding a period at the end of the objects name and the methods name we would like to call with parentheses.
* You can create your own class in python
    * The class has data attributes and the class has methods
        * Class Circle / Data Attributes: radius, color
        * Class Rectangle / Data Attributes: color, height and width
* class Circle(object):   'class' is the Class Definition / 'Circle' is the name of the Class / 'object' is the Class parent
    * Object 1: Instance of type Circle / Data Attributes: radius = 4, color = red
    * Object 2: Instance of type Circle / Data Attributes: radius = 2 , color = green
* class Circle(object):  <= Define your class
     def _ init _ (self, radius, color):         <= Data attributes used to intialize each instance of the class
          self.radius = radius;
          self.color = color;
* The function *init* is a constructor function that tells python you are making a new class
* Radius and Color are *parameters* used to initialize the radius and color data attributes of the class instance
* Self is a *parameter* refers to the newly created instance of the class
* How to create an object of class circle:
    * RedCircle = Circle(10,"red")  <= Everything from the 2nd 'Circle' onward is called the class constructor, where 'Circle' is the name of the class and 10 and "red" are the attributes
    * RedCircle.radius = 10
    * RedCircle.color = "red"

Methods: Functions that interact and change the data attributed, changing or using the data attributes of the object.
* class Circle(object):
     * def _ init _ (self, radius, color):
          *  self.radius = radius;
          *  self.color = color;
     *  def add_radius(self,r):
          * self.radius = self.radius + r    <= Method used to add r to radius
* Don't need to worry about the self parameter when calling the method
    * RedCircle = Circle(10,"red")
    * RedCircle.add_radius(8)
    * RedCircle.radius = 18
* the dir(Nameofobject) function is useful for obtaining the list of data attributes and methods associated with a class
  


#### 

Reading Files with Open
* use open()
    * File1 = open("/resources/data/Example2.txt","r") <= where the first parameter is the file path (which includes the file name and file directory) and the 2nd parameter is the mode. Common values include "r" for reading, "w" for writing and "a" for appending. *File1* is the file object
    * File1.name
    * Always close file object using File1.close()
    * open files using a with statement because it automatically closes the file
        * **with** open("Example1.txt","r") as File1:
            * file_stuff = File1.read()
            * print(file_stuff
    * print every line as an element in a list using the method .readlines(). The first line corresponds to the first element in the list.
    * file_stuff[0] = ['This is line 1 /n']
    * readline() reads the first line of the file
    * **with** open("Example1.txt","r") as File1:
        * for line in File1:       <= will print out each line in the file separately``
            * print(line)
    * readlines(16) will call the first 16 characters of a line

Writing Files with Open
* use open()
    * method .write() will write data to that file
    * File1 = open("/resources/data/Example2.txt","w")
* **with** open("Example2.txt","w") as File1:
    * File1.write('This is line A")
* use \n to signify a new line
* We can set the mode to append using "a". This will not create a new file but just use the existing file

Loading Data with Pandas
* libraries are pre-written code to help solve problems
* **import** pandas as pd. <= use *as* to shorten so you can reference
* csv_path = 'file1.csv'
* df = pd.read_csv(csv_path)
* df.head() <= df is short for dataframe. Use *head* to examine first five rows
* pd.read_excel() for excel files, the result is a dataframe.
* Dataframes
    * Comprised of rows and columns
    * can be created out of a dictionary
    * keys are columns and values are rows
    * cast a dictionary to a dataframe using the function *pd.DataFrame(dictionary)*
    * keys are headers anbd values are lists corresponding to the rows

Pandas: Working with and Saving Data
List Unique Values
* df['Column_Name'].unique()
* ex: df1 = df[df['Released']>=1980] <= will create a new dataframe with all columns for albums released in or after 1980
Save as CSV
* d1.to_csv('newcsv_name.csv')

One Dimensional Numpy
Numpy: Library for scientific computing. Alsos the basis for pandas 

The Basics and Array Creation  
A Numpy array is similar to a list
* **import** numpy as np
* a = np.array([0,1,2,3,4]) <= we can then acceess the data via an index
* type(a):numpy.ndarray
* a.dtype:dtype('int64')
* a.size: 5
* a.dim: 1 <= the number of dimensions
* a.shape: (5,) A tuple of integers indicating the size of the array in each dimension

    Indexing and Slicing
    * c = np.array([10,1,2,3,4])
    * c:array([20,1,2,3,4]
    * c[0] = 100
    * c:array([100,1,2,3,4])
 
    * d = c[1:4]
    * d:array([1,2,3])
 
    * c[3:5]=300,400
    * c:array([100,1,2,300,400])

    Basic Operations  
    Vector Addition and Substraction  
    * u=[1,0]  
    * v=[1,0]  
    * z=[]  
    * for n,m **in** zip(u,v):     <= this will add the two vectors and place the result in vector *z*
        * z.append(n+m)  
    * Can also perform using 1 line of numpy code
    * u=np.array([1,0])
    * v=np.array([0,1])
    * z = u+v
    * z:array([1,1])        
    * Numpy code will run much faster
    
    Array Multiplication with a scalar
    * y = np.array(1,2])
    * z = 2*y
    * z:array([2,4])
 
    Product of two Numpy Arrays  
    **Hadamard** Product
    * u = np.array([1,2])
    * v = np.array([3,2])
    * z = u*v
    * z:array([3,4])  
    **Dot Product**
    * A single number that represents how similar the two vectors are.
    * u = np.array([1,2])
    * v = np.array([3,2])
    * result = np.dot(u,v)
    * result:7
 
    Adding Constant to a Numpy Array
    * u = np.array([1,2,3,-1])
    * z = u+1 <= adds the number to each element, this is known as *broadcasting*
    * z:array([2,3,4,0])
 
    Universal Functions: A function that operates on nd arrays
    * a = np.array([1,-1,1,-1])
    * mean_a = a.mean()
    * mean_a:0.0
    * .max() <= returns max
    * .linspace() <= returns evenly spaced numbers over a specified interval  

Two Dimensional Numpy
* a = [[11,12,13],[21,22,23],[31,32,33]]
* A = np.array(a)
* A.ndim : 2 The number of nested lists. The first list represents the first dimension. This list contains another set of lists
* A.shape: (3,3) <= returns a tuple. The first element in the tuple corresponds to the number of nested lists contained in the original list. The second element corresponds to the size of each of the nested lists
* A.size : 9

* X = np.array([[1,0],[0,1]])
* Y = np.array([[2,1],[1,2]])
* Z = X + Y
* Z : array([[3,1],[1,3]])

    Matrix multiplication
    * We must make sure that the number of columns in matrix A is equal to the number of rows in matrix B
    * A = np.array([[0,1,1],[1,0,1]])
    * B = np.array([[1,1],[1,1],[-1,1]])
    * C = np.dot(A,B);
    * C : array([[0,2],[0,2]])
  

#### Week 5 APIs and Data Collection

Simple APIs (Part 1)

What is an API?  
Let's two pieces of software talk to each other. Talks to other software via inputs and outputs

    REST APIs: Representational State Transfer API
    * Used to interact with web services, ie. apps that you call through the internet
    * your program is called the client
    They have a set of rules regarding:
        1. Communication
        2. Inputs or Request
        3. Output or Response
    HTTP Methods are a way of transmitting data over the internet
        We tell the REST API what to do by sending a request. The request is usually communicated via an HTTP message. The HTTP message usually contains a JSON file.
        This message contains instructions for what operation we would like the service to perform. The operation is transmitted to the web service via the internet. The service peforms the operation. 
        The web service returns a response via an HTTP message, where the information is usually returned via a JSON. This info is transmmitted back to the client

Simple APIs (Part 2)  
API Keys and Endpoints: Give access to the API
* First Call to the API will include the API key which will give access to the API. In many APIs you will get charged for each call
* Endpoint is simply the location of the service used to find the API on the internet.
 

REST APIs & HTTP Requests - Part 1  
HTTP Protocol: The general protocol for transferring information through the web  
URL: Uniform Resource Locator  
* Scheme: The protocol, for this lab it will always be http://
* Internet Address or Base URL: Used to find the location
* Route: Location on the web server

Request and Response

REST APIs & HTTP Requests - Part 2
HTTP Using the Requests Library in Python
* requests is a python library that allows you to send HTTP/1.1 requests easily
* Make a request.get(url) request
* There is no body for a get request
* Like a GET request a POST request is used to send data to a server, but the POST request sends the data in a request body, not the url.
    * Change the route to 'post'
    * POST request has no name or value pairs in its URL
 
Webscraping
* import BeautifulSoup
* soup = BeautifulSoup(html, 'html5lib')
* tag_object = soup.title
* *find_all*: This is a filter you can use to filter based on tags's name, its attributes, the text of a string or on some combination of these.
* table = BeautifulSoup(html,'html5lib')
* table_row = table.find_all(name = 'tr') <= the result is a python iterable just like a list, each element is a tag object
* for i, row **in** enumerate(table_rows):
    * print("row", i)
    * cells = row.find_all("td")
    * for j, cell **in** enumerate(cells):
      * print("column",j,"cell",cell)
     
Working with Different file formats (csv, xml, json, xlsx)



```python

```
