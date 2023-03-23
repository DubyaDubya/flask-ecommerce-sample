import warnings
from settings import db_user, db_host, db_name
warnings.simplefilter(action='ignore')
import pandas as pd
url = "https://raw.githubusercontent.com/tech-interviews-jigsaw/data-analysis-takehomes/main/1-approaches-for-problems/ecommerce-dataset.csv"
df = pd.read_csv(url)
breakpoint()
from sqlalchemy import create_engine
conn_string = f'postgresql://{db_user}@{db_host}/{db_name}'

conn = create_engine(conn_string)
df.to_sql('raw_transactions', conn, if_exists='replace')