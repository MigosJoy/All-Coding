# Databases and SQL for Data Science

Jason Head

#### Course 6 in the IBM for Data Science Specialization

[Course Link](https://www.coursera.org/learn/sql-data-science/home/week/1)

#### Objectives

* write foundational SQL statements like: SELECT, INSERT, UPDATE, and DELETE 
* filter result sets, use WHERE, COUNT, DISTINCT, and LIMIT clauses 
* differentiate between DML & DDL  
* CREATE, ALTER, DROP and load tables 
* use string patterns and ranges; ORDER and GROUP result sets, and built-in database functions 
* build sub-queries and query data from multiple tables  
* access databases as a data scientist using Jupyter notebooks with SQL and Python 
* work with advanced concepts like Stored Procedures, Views, ACID Transactions, Inner & Outer JOINs 

#### Week 1 Getting Started w SQL

[SQL Cheat Sheet](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstREIwMjAxRU4tU2tpbGxzTmV0d29yay9sYWJzL0NoZWF0U2hlZXQvU1FMLUNoZWF0LVNoZWV0LUJhc2Npcy5tZCIsInRvb2xfdHlwZSI6Imluc3RydWN0aW9uYWwtbGFiIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE2OTI5NTE0Mzh9.7bS4GDbKzkxQXdDeuDJadkf82pu777fe8xHUJ8F3XnE)

#### Week 2 Intro to Relational DB and Tables

Relation Model
* Allows for data independence which provides logical, physical and phyiscal storage independence
* Most Used

Types of SQL statements (DDL vs DML)
* Data Definition Language statement
    * Used to define change or drop data
        * CREATE, ALTER, TRUNCATE and DROP
        * CREATE: Used for creating tables
        * ALTER Used to alter tables
        * TRUNCATE: Used to delete data in a table but not the table itself
        * DROP: Used to delete tables
* Data Manipulation Language statement
    * Used to read and modify data in tables
    * Sometimes referred to as CRUD (Create, Read, Update, Delete)
        * INSERT, SELECT, DELETE
        * INSERT: Used for inserting a row or several rows of data into a table
        * SELECT: Reads of selects row or rows from a table
        * DELETE: Removes a row or rows of data from a table

Week 3 Intermediate SQL
* Built-n DB Functions
    * can be included in sql statements
    * can reduce amount of data that needs to be retrieved and may be faster
    * can speed up data processing
    * can create own functions
    * 

Week 4 Accessing Databases using Python
* Access databases from Python using SQL magic.
* Describe concepts related to accessing Databases using Python.
* Create tables and insert data using Python.
* Connect to a database using ibm_db Python library.
* Analyze a data set using SQL and Python.

Accessing Databases Using Python 

Writing Code using DB-API  
Concepts of the Pyhton DB API
* Connection Objects: Used to connect to a database and manage transactions
* Cursor Objects: Used to run queries

Connection Methods
* cursor(): returns a new cursor object using the connection
* commit(): used to commit any pending trasnaction to the DB
* rollback(): casues the DB to roll back to the start of any pending transaction
* close(): used to close a DB connection

A database cursor is a control structure that enables traversal over the records in a DB. It behaves like a filename or file handle in a programming language

ibm_db API

Creating Tables, Loading Data and Querying Data

Week 5 
Course Assignment: 
In this assignment, you will be working with multiple real world datasets for the city of Chicago. You will be asked questions that will help you understand the data just as you would in the real wold. You will be assessed on the correctness of your SQL queries and results.

Objectives:
* Invoke SQL queries using Python.
* Retrieve SQL query results and analyze data.
* Interpret and translate data analysis questions into SQL queries.

Working w Real World Datasets

Working w csv files 
* These are text files which contain data values mostly separated by commas. sometime semi-colon.
*  DOGS.CSV
*  The first row in many cases refers to attribute labels which refer to column names in the table
*  Use double quotes to specify mixed-case column names:
    * select "Id" from DOGS
* Be default, spaces are mapped to underscores

Using Quotes in Jupyter
* selectQuery = 'select "Id" from dogs'
* Use a backslash as the escape character in cases where the query contains single quotes
    * selectQuery = 'select * from dogs where "Name_of_Dog" = \'Huggy\' '
 
* Use backslash to split the query into multiple lines:
    * %sql select "Id", "Name_of_Dog", \
              from dogs \
              where "Name_of_Dog" = 'Huggy'
* Or use %%sql in the first row of the cell in the notebook (using **Magic SQL**): \
    %%sql  
    select "Id", "Name_of_Dog",  
    from dogs   
    where "Name_of_Dog" = 'Huggy'  

Getting Table and Column Details

Week 6 Honor Module for Data Engineering

Views, Stored Procedures and Transactions
* **View**: An alternative way of representing data that exists in one or more tables or views
    * Can include specified columns from multiple base tables and existing views
    * Once created can be queried like a table
    * Only the definition of the view is stored, not the data

Views can:
* Show a selection of data for a given table
* Combine two or more tables in meaningful ways
* Simplify access to data
* Show only portions of data in the table
* EX: Create a view to display non-sensitive data from the Employees table

CREATE VIEW statement  \
CREATE VIEW [view name] ([column_alias_1],...,[column_alias_n])\
AS SELECT [column_1],...,[column_n]\
FROM [table name]\
where [predicate]; 


DROP VIEW to remove view completely

Stored Procedures
* A set of SQL statement stored and executed on the database server
    * write in many different languages
    * Accept information in the form of parameters
    * return results to the client app
 * Benefits
    * Less network traffic
    * Improvement in performance
    * Reuse of code
    * Increase in security

![image.png](fbd629bb-6820-458d-b38a-7731f56db294.png)

* Call from:
    * External applications
    * Dynamic SQL statements

![image.png](f3f75036-c36e-4290-86b8-6847917d4368.png)

ACID Transactions
* An indivisible unit of work
* Consists of one or more SQL statements
* Either all happens or none
* **Atomic**: All changes must be performed successfully or not at all
* **Consistent**: Data must be in a consistent state before and after the transaction
* **Isolated**: No other process can change the data while the transaction is running
* **Durable**: The changes made by the transaction must persist

ACID commands \
![image.png](f02f10c4-2030-4bc6-a082-632045dd89cb.png)

* BEGIN: Start the ACID transaction
* COMMIT: All statements complete successfully , save the new database state
* ROLLBACK: One or more statements fail , undo changes


```python

```


```python

```
