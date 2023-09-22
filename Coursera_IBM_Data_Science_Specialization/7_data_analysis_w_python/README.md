# **Course 7** - IBM Specialization - Data Analysis with Python

#### Jason Head

[Course Link](https://www.coursera.org/learn/data-analysis-with-python/home/week/1)

Topics include:  
- collecting and importing data 
- cleaning, preparing & formatting data 
- data frame manipulation 
- summarizing data 
- building machine learning regression models 
- model refinement 
- creating data pipelines

You will learn how to import data from multiple sources, clean and wrangle data, perform exploratory data analysis (EDA), and create meaningful data visualizations. You will then predict future trends from data by developing linear, multiple, polynomial regression models & pipelines and learn how to evaluate them.  

### Week 1 Importing Datasets

#### Importing Data
Two important properties
* format
    * csv, json, xlsx, etc.
* file path
    * computer: mycomputer/myfile
    * internet: https://www.....
 
Importing a csv into python \
![image.png](d5bd904d-935c-4f06-8744-1d38c4200554.png)

Importing a csv without a header \
![image.png](ae8b6bb7-7c2b-4802-a66a-f28d879abc50.png)

* df.head() to show the first n rows
* df.tail() to show last n rows

Adding Headers \
![image.png](cd8739d9-b39d-4e2d-8927-5986225d3655.png)

Exporting a pandas dataframe as CSV \
![image.png](d8b42320-4127-40b8-b179-7113217ed64a.png)

Exporting to different formats in Python \
![image.png](734aa143-a15a-47d4-92e3-1434c8b102d6.png)

#### Getting Started Analyzing Data
* Data Types
* Data Distribution
* Locatee potential errors in the data

Data Types
* int and float very similar
* Why check data types? potential info and type mismatch and compatibility w python methods
* *df.dtypes* checks data types
* *df.describe()* returns a statiscal summary of each column to learn about the distribution of data in each column \
  ![image.png](71c30768-1a7c-42a3-9144-96fd1142f69e.png)

* *df.describe(include = 'all')*: Full summary statistics of all columns \
![image.png](94c47865-9f83-40ae-8d0c-1a6cb00cf82f.png)

* *df.info()*: Shows the top 30 rows and the bottom 30 rows of the dataframe

#### Accessing DBs w Python
DB-API: Used to  connect with and get results from databases using Python \
Writing Code using DB-API \
![image.png](fb9ba093-77bd-4df0-8a34-35d2e8c0df9c.png)


### Week 2 Data Wrangling 
#### Data Pre-processing in Python
* The process of converting or mapping data from the initial "raw" form into another format, in order to prepare the data for further analysis

#### Dealing with Missing Values in Python
* Occurs when data value is stored for a variable in an observation
* "?","N/A",0 or just a blank cell

How to deal with missing data
* Check the data collection source
* Drop the missing values
    * drop the variable
    * drop the data entry: Good where not missing a lot of values
* Replacing data is better since no data is wasted, however, less accurate
    * replace w average of similar datapoints
    * replace it by frequency
    * replace it based on other functions
* Leave as missing data

How to drop missing values in Python
* df.dropna():
    * axis = 0 drops the entire *row*
    * axis = 1 drops the entire *column* 
    * inplace = True : allows the modification to be done on the dataset directly. **VERY IMPORTANT** \
 ![image.png](53e8360f-8097-4462-9bd2-ace4be8ee35c.png)

How to replace missing values in Python
* df.replace(missing_value, new_value): \
![image.png](4c60c014-c8b9-4d25-970e-67b1d0a5cdf3.png)

#### Data Formatting in Python
* Bringing data into a common standard of expression allows users to make meaninful comparison

Applying calculations to an entire column \
![image.png](3b5e5e78-3cf8-40f6-a039-7bcde5a04fbe.png)

Incorrect Data Types
* df.dtypes() : Checks data type
* df.astype() : Converts data type

#### Data Normalization in Python
![image.png](d51b882d-1149-4382-9a66-1cf652f69d66.png)

Methods of normalizing data
* *Simple Feature Scaling*: Ranges from 0 to 1; divides each value by the maximum value for that feature.
* *Min-Max*: Ranges from 0 to 1; subtracts the minimum value of that feature from each value and divides by the range of that feature
* *Z-score*: Result values hover around 0 and typically range -3 to +3; Subtract the average of that feature from each value and divide by the standard deviation
![image.png](b413728e-2325-4c41-8851-e908ba8d7ccd.png)

Simple Feature Scaling in Python \
![image.png](e575c287-79c8-4199-b855-a639938b83b7.png)

Min-max in Python \
![image.png](68558b32-02b8-436c-ad14-84037334dca2.png)

Z-score in Python \
![image.png](01ca0944-103c-4720-a71a-a3da8a2201d4.png) 

#### Binning in Python
* Binning: Grouping values into "bins"
* Converts numeric into categorical variables
* Group a set of numerical values into a set of "bins" \
![image.png](0f839d08-5604-42c8-b203-245ba1b53428.png)

#### Turning Categorical variables into Quantitative variables in Python
* *Problem*: Most stats models cannot take in the objects / strings as input
    * "One-hot encoding": Add dummy variables for each unique category, assign 0 or 1 in each category \
![image.png](48ca6b8c-bc22-4c78-9bcc-6919b0f99871.png)

* Use pandas.get_dummies()
    * pd.get_dummies(df['fuel'])
  



```python

```
