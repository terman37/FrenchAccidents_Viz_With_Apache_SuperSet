import pandas as pd
from sqlalchemy import create_engine
import os

data_folder = '../datas'
data_files = os.listdir(data_folder)

sqlalchemy_conn_str = 'mysql://user:password@127.0.0.1:3306/fa'
engine = create_engine(sqlalchemy_conn_str)

for data_file in data_files:
    df = pd.read_csv(os.path.join(data_folder, data_file), encoding='latin1')
    table_name = os.path.splitext(data_file)[0]
    print("insert into: %s -> %d records" % (table_name, df.shape[0]))
    df[:100].to_sql(table_name, con=engine, if_exists='replace', chunksize=10000)

print('done !')
