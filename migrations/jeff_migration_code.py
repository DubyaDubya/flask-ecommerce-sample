import warnings
warnings.simplefilter(action='ignore')
import pandas as pd
url = "https://raw.githubusercontent.com/tech-interviews-jigsaw/data-analysis-takehomes/main/1-approaches-for-problems/ecommerce-dataset.csv"
df = pd.read_csv(url)

from sqlalchemy import create_engine
conn_string = 'postgresql://jeffreykatz@localhost/sample_ecommerce'

conn = create_engine(conn_string)
df.to_sql('raw_transactions', conn, if_exists='replace')