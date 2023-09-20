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


```python

```
