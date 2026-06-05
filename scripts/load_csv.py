import duckdb
import pandas as pd

conn = duckdb.connect("warehouse/sales.duckdb")

df = pd.read_csv("data/sales.csv")

conn.execute("""
CREATE OR REPLACE TABLE bronze_sales AS
SELECT * FROM df
""")

print("Data loaded successfully")