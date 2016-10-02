import pandas as pd
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
import copy
import datetime
from decimal import Decimal

cluster = Cluster(contact_points = ['127.0.0.1'])
print(cluster)
session = cluster.connect('warehouse')

#This is to load data in table with counter since it can not be copied be directly copied from csv files
contents =[]
with open('table4.csv') as f:
        for x in f.readlines():
                if x not in contents:
                        contents.append(x)

i=1
while i < len(contents):
        transx = contents[i].strip('\n').split(",");
        query = 'UPDATE next_order SET d_next_o_id=d_next_o_id+'+transx[2]+ ' WHERE w_id='+ transx[0] +' and d_id='+ transx[1] +';'
	print(query)
        session.execute(query)
	i=i+1
