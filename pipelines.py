from pymongo import MongoClient
from datetime import datetime

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
        { "$group": { "_id": { "gender": "$Sex", "age": "$Age"}, "count": {"$sum": 1}}},
        { "$out": "population"}
    ]

    # Race Partition
    pipeline4 = [
        { "$group": { "_id": "$Race", "count": {"$sum": 1}}},
        { "$out": "race"}
    ]

    # InjuryCity by county 
    pipeline5 = [
        { "$group": { "_id": "$InjuryCityGeo", "count": {"$sum": 1}}},
        { "$out": "injurygeo"}
    ]

    # ResidenceCity by county

    # Which opioids

    # More complicated query

    # More complicated query 2

    drugs.aggregate(pipeline5)