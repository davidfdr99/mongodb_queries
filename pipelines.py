from pymongo import MongoClient
import time

def get_database():

    connection_string = "mongodb://localhost:27017/"
    client = MongoClient(connection_string)
    return client['project3']

if __name__ == "__main__":

    db = get_database()
    drugs = db.drugs

    a = drugs.find_one()
    print(a)

    #Gender Partition
    pipeline1 = [
        { "$match": {"Sex": {"$ne": "NA"}}},
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
        { "$match": {"Sex": {"$ne": "NA"}}},
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
    pipeline6 = [
        { "$group": { "_id": "$ResidenceCityGeo", "count": {"$sum": 1}}},
        { "$out": "residencegeo"}
    ]

    # Died of opioids per year
    pipeline7 = [
        {"$match": { "Any Opioid": 1}},
        {"$group": {"_id": {"$year": "$Date"}, "count": {"$sum": 1}}},
        {"$out": "opioid"}
    ]

    # Which opioids and change over time
    pipeline8 = [
        {"$project": {"drugs": {"$objectToArray": "$drugs"}, "Date": 1}},
        {"$unwind": "$drugs"},
        {"$match": {"drugs.v": 1}},
        {"$group": {"_id": {"type": "$drugs.k", "year": {"$year": "$Date"}}, "count": {"$sum": 1}}},
        {"$out": "types"}
    ]

    t1_start=time.perf_counter()
    drugs.aggregate(pipeline8)
    t1_stop = time.perf_counter()
    print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)