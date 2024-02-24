import pandas as pd
from titan_db_class import update_fundamental_info, query_fundamental_info

df = pd.read_csv("./adj.csv", index_col=0, header=0)
dates = df.index.values
symbol_ids = df.columns.values
attribute = "adjustment_factor"
data = df.values

success = update_fundamental_info(dates, symbol_ids, attribute, data)
result = query_fundamental_info(dates, symbol_ids, attribute)
