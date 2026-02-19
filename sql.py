import os
import pandas as pd
from dotenv import load_dotenv

# load variables
load_dotenv()

# credentials
host = os.getenv('db_host')
port = os.getenv('db_port')
db = os.getenv('db_name')
user = os.getenv('db_user')
pw = os.getenv('db_pass')

# connection string
connection_string = f"postgresql://{user}:{pw}@{host}:{port}/{db}"

# sql query
sql_query = """
select 
    s.id as sale_id,
    s.date,
    s.price,
    d.*
from eda.king_county_house_sales s
join eda.king_county_house_details d on s.house_id = d.id
"""

df = None

try:
    # string, not engine, new handling pandas 3.0.0
    df = pd.read_sql(sql_query, connection_string)
    
    # save and show
    df.to_csv('data/king_county_full.csv', index=False)
    print("Data loaded via SQLAlchemy and saved to 'data/king_county_full.csv'")
    display(df.head())

except Exception as e:
    print(f"Connection failed: {e}")