
# .SSH Terminal commands for connecting mySQL if using Google Colab:
# !sudo apt-get install python3-dev default-libmysqlclient-dev
# !pip3 install pymysql
# !pip3 install python-dotenv


from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv()
## Need to configure server to allow inbound connections 

# Create a special config fiel named 'mysql.cnf'
# Use nano for updates: sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf/

### CONNECTING DB TO VM ### 

# Load environment variables:
load_dotenv()

# change this to your IP address which is found on your GCP console
# store key as .json file in .gitignore
MYSQL_HOSTNAME = 'insert_external_IP_address'
MYSQL_USER = 'insert_user'
MYSQL_PASSWORD = 'insert_pass'
MYSQL_DATABASE = 'insert_db_name'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string # view output

# Using create_engine to allow us to link db to mysql
engine = create_engine(connection_string)
engine
# print(engine.table_names())

# Create a query
query = 'select * from db1.salarytable;'
query
## query = """select * from ds_salaries limit 10;""".format(MYSQL_DATABASE)


## Data 
df = pd.read_sql(query, con=engine)
df # shows empty table with column names (title, salary, year)


# pip install --upgrade sqlalchemy
salary = pd.read_csv('data\ds_salaries.csv')
salary

## Push salary df into db1
salary.to_sql('ds_salary_table', con=engine, if_exists='append') #607 

# Whoever has access to db1 now can query this data