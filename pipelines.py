from pymongo import MongoClient
from datetime import datetime
from pprint import pprint

def get_database():

    connection_string = "mongodb://localhost:27017/"
    client = MongoClient(connection_string)
    return client['project3']

if __name__ == "__main__":

    db = get_database()
    drugs = db.data

    a = drugs.find_one()
    print(a)

    #Gender Partition
    pipeline1 = [
    { "$group": { "_id": "$Sex", "count": {"$sum": 1}}},
    { "$out": "gender"}
    ]

    # Age Partition
    pipeline2 = [
        { "$group": { "_id": "$Age", "count": {"$sum": 1}}},
        { "$out": "age"}
    ]

    #Gender and Age Partition
    pipeline3 = [
        {}
    ]

    # Race Partition
    pipeline4 = [
    { "$group": { "_id": "$Race", "count": {"$sum": 1}}},
    { "$out": "race"}
    ]

    # InjuryCity by county 

    # ResidenceCity by county

    # Which opioids

    # More complicated query

    # More complicated query 2

    # drugs.aggregate(pipeline2)

    cursor = db.age.aggregate([
        {"$sort": {"_id": 1}}
    ])

    for age in list(cursor):
        pprint(age)