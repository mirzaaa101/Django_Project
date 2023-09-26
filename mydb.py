# intall mysql workbench on your local machine
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='01640720014'
)

# Create cursor object
cursorObj = mydb.cursor()

# Create database
cursorObj.execute("CREATE DATABASE IF NOT EXISTS crm")

# Connect to the 'crm' database
cursorObj.execute("USE crm")

print("All done!!")
