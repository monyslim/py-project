# Importing necessary libraries
import pandas as pd
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
print(os.getenv("MY_KEY"))

# # SQL library to help connect the excel file to the database.
import psycopg2 as pg2

# # importing SQL from psycopg2 to create and run sql queries.
from psycopg2 import sql

# # Password for Postgres
secret = "password"

# # Connecting the database to excel
connection= pg2.connect(database = os.getenv("DATABASE"), 
                   user = os.getenv("USER"),
                   password = os.getenv("PASSWORD"),
                   host = os.getenv("HOST"),
                   port = os.getenv("PORT"))

# # Function to send the sql commands to be executed and fetch data from the database
cursor = connection.cursor() 

# # Table name to connect to
table_name = "superstores_data"

# # Specifying the filepath.
file_path = "superstore.xlsx"

# # Reading the sheet in the excel workbook
super_sheet = pd.read_excel(file_path, sheet_name = "Orders")

# # Showing the first 10 rows of the excel sheet.
# # print(super_sheet.head(10))
    
# # Inserting the query using psocopg2  .sql.SQL method
insert_query = sql.SQL("""
                       INSERT INTO "superstores_data" (
                           "row_id", "order_id", "order_date", "ship_date", "ship_mode", "customer_id", 
                           "customer_name", "segment", "country", "city", "state", 
                           "postal_code", "region", "product_id", "category",
                           "sub_category", "product_name", "sales", "quantity", 
                           "discount", "profit"
                           )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """).format(table=sql.Identifier(table_name))

# # Converting the excel file using panda to a dataframe format
contents = pd.DataFrame(super_sheet)

# # Loop through the rows in the table of contents
for index, content in contents.iterrows():
    
#     # Helps to insert the data as tuples using the .execute function
    cursor.execute(insert_query, tuple(content))

# # Saving the data to the database
connection.commit()

# # Ending the connection
cursor.close()
connection.close()