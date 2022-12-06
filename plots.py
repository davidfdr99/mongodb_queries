import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

from pipelines import get_database

def get_age_dist():
    ## Age distribution
    ages = []
    cursor1 = db.age.aggregate([
            {"$sort": {"_id": 1}}
        ])
    for age in cursor1:
        ages.append([age['_id'], age['count']])

    sns.set_style(style="darkgrid")

    counts = [age[1] for age in ages]
    bins = [age[0] for age in ages]
    plt.bar(bins, counts)
    plt.xlabel('Age')
    plt.ylabel('Number of drug-related deaths')
    plt.title('Age Distribution')
    # plt.savefig('./plt/02_age_distribution.png')


def get_sex_dist():
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


def get_population():
    # Age and Gender 
    cursor3 = db.population.find({"_id.age": {"$exists": True}})

    ll = []
    for doc in cursor3:
        ll.append([doc['_id']['age'], doc['_id']['gender'], doc['count']])

    df_plt = pd.DataFrame(ll, columns=['Age', 'Gender', 'Count'])
    # df_plt.to_csv('./plt/population.csv')

    #Race
    data = []
    cursor4 = db.race.find()
    for doc in cursor4:
        if doc['_id'] is not None:
            data.append([doc['_id'], doc['count']])
        else:
            data.append(['na', doc['count']])
    df_r = pd.DataFrame(data, columns=['Race', 'Deaths'])
    # df_r.to_csv('./plt/races.csv')

    return df_r

def get_opioid_dev():
    #Opioid Development
    cursor5 = db.opioid.find()
    oo = [[doc['_id'], doc['count']] for doc in cursor5]
    df_o = pd.DataFrame(oo, columns=["Year", "NumberOpioids"])
    print(df_o.head)

    sns.set(style="darkgrid")
    ax = sns.pointplot(x="Year", y="NumberOpioids", data=df_o)
    plt.xlabel("Years")
    plt.ylabel("Number of Deaths, any opioid usage")
    plt.title("Development of deaths related to any opioid usage")
    # plt.savefig('./plt/07_opioid_dev.png')

if __name__ =="__main__":

    db = get_database()