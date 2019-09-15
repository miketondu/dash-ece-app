import pandas as pd
import psycopg2


df=pd.read_csv(r"D:/dash-ece-app-master/ECE_copy.csv")

df.to_csv('use.csv',index=False)

host="ec2-174-129-227-80.compute-1.amazonaws.com"
db="d6kqslcuso8lr"
us="bnwycizeyrtlgn"
pwd="8d207872efa476ea7e3f9ae0bc23045fe114ae3ac4b67956b7e3d754a5632d3e"

conn = psycopg2.connect(host=host,database=db, user=us, password=pwd)

cur = conn.cursor()
with open('use.csv', 'r') as f:

    next(f) # Skip the header row.
    cur.copy_from(f, 'data', sep=',')
    conn.commit()

