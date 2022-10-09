
# .ssh terminal commands for connecting mySQL using Google Colab:
# !sudo apt-get install python3-dev default-libmysqlclient-dev
# !pip3 install pymysql
# !pip3 install python-dotenv
# !pip3 install requirements.txt


from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# Load environment variables:

# change this to your IP address which is found on your GCP console
MYSQL_HOSTNAME = 'insert_host'
MYSQL_USER = 'insert_user'
MYSQL_PASSWORD = 'insert_pass'
MYSQL_DATABASE = 'insert_db_name'

# CREATE ENGINE
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string # view output

# Using create_engine to allow us to link db to mysql
engine = create_engine(connection_string)

# Create a query
query = 'select * from salary.ds_salaries;'

# print(engine.table_names())

salary = pd.read_csv('data\ds_salaries.csv')

salary.to_sql('ds_salaries', con=engine, if_exists='append')