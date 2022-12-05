import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

from pipelines import get_database

db = get_database()

## Age distribution

ages = []
cursor1 = db.age.aggregate([
        {"$sort": {"_id": 1}}
    ])
for age in cursor1:
    ages.append([age['_id'], age['count']])
print(ages)

sns.set_style(style="darkgrid")

counts = [age[1] for age in ages]
bins = [age[0] for age in ages]
plt.bar(bins, counts)
plt.xlabel('Age')
plt.ylabel('Number of drug-related deaths')
plt.title('Age Distribution')
# plt.savefig('./plt/02_age_distribution.png')

# Sex distribution

gender_list=[]
cursor2 = db.gender.find()
for gender in cursor2:
    gender_list.append([gender['_id'], gender['count']])

df2 = pd.DataFrame(gender_list, columns=['Gender', 'Counts'])
total = 0
for count in df2['Counts']:
    total += count

sns.set_style(style="darkgrid")
bar,ax = plt.subplots(figsize=(10,6))
ax = sns.barplot(x="Counts", y="Gender", data=df2, errorbar=None, palette="muted",orient='h')
ax.set_title("Gender distribution")
ax.set_xlabel ("Counts")
ax.set_ylabel ("Gender")
for rect in ax.patches:
    ax.text(rect.get_width(), rect.get_y() + rect.get_height() / 2,'{:.1f}%'.format(100 * rect.get_width()/total), weight='bold')
# plt.savefig("./plt/01_gender_distribution.png")

# Age and Gender 

cursor3 = db.population.find()

pop = []
for doc in cursor3:
    pop.append([doc['_id']['gender'], doc['_id']['age'], doc['count']])

df3 = pd.DataFrame(pop, columns=['Gender', 'Age', 'Count'])
print(df3.head)