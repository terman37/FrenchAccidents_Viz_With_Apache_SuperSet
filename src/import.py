import pandas as pd
from sqlalchemy import create_engine
import os

data_folder = './datas'
data_files = os.listdir(data_folder)

sqlalchemy_conn_str = 'mysql://user:password@127.0.0.1:3306/fa'
engine = create_engine(sqlalchemy_conn_str)

for data_file in data_files:
    # data_file = "caracteristics.csv"

    table_name = os.path.splitext(data_file)[0][:-5]

    engine.execute("DROP TABLE IF EXISTS `%s`" % table_name)
    # engine.execute(table_creation[table_name])

    counter = 0
    reader = pd.read_csv(os.path.join(data_folder, data_file),
                         encoding='latin1',
                         sep=";",
                         decimal=",",
                         chunksize=10000)

    for chunk in reader:
        counter += chunk.shape[0]
        print("\rinsert into: %s -> %d records" % (table_name, counter), end='')
        for col in chunk.columns:
            if chunk[col].dtypes == 'object':
                chunk[col] = chunk[col].str.encode('latin1')

        chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
    print("\rinsert ok into: %s -> %d records" % (table_name, counter))

print('done !')
