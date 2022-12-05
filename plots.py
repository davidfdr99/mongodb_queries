from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

from pipelines import get_database

db = get_database()
drugs = db.data

ages = []
cursor1 = db.age.aggregate([
        {"$sort": {"_id": 1}}
    ])
for age in cursor1:
    ages.append([age['_id'], age['count']])
print(ages)

counts = [age[1] for age in ages]
bins = [age[0] for age in ages]
plt.bar(bins, counts)
plt.show()