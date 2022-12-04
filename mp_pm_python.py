from pymongo import MongoClient
from bson.code import Code
import pandas as pd

def get_database():

    connection_string = "mongodb://localhost:27017/"
    client = MongoClient(connection_string)
    return client['project3']

def main():

    db = get_database
    drugs = db.drugabuse()

    mapper = Code("""
    function() { 
        var CT = 
    """)

    reducer = Code( """
    function(key, value) {
        var total = 0;
        for (var i; i < values.length; i++) {
            total += values[i]
        }
        return total;
        }
    """)