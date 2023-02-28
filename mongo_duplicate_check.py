"""
Script that checks for duplicates in a mongo collection
"""
import sys
from pymongo import MongoClient

client = MongoClient()
db = client['mirrulations']

pipeline = [
    {
        "$group": {
            "_id": {
                "id": "$data.id",
                "modifyDate": "$data.attributes.modifydate"
            },
            "count": {"$sum": 1},
            "duplicates": {"$push": "$_id"}
        }
    },
    {
        "$match": {"count": {"$gt": 1}}
    }
]


def collection_for_query():
    """
    Return
    -------
    database collection on which to search for duplicates
    """
    collections = db.list_collection_names()
    print(f"collections in mirrulations {collections}")
    collection_name = input("which database collection to search for duplicates: ")
    if collection_name not in collections:
        print("Collection not in database, exiting")
        sys.exit()
    else:
        return collection_name


def show_duplication_results(results):
    """
    Displays query results to user
    """
    if len(results) > 0:
        print("Duplicates exist in collection")
        response = input("do you want to see full list of duplicates? y/n: ")
        if response.lower() == 'n':
            print(str(len(results)) + ' duplicates in collection')
            sys.exit()
        elif response.lower() == 'y':
            print("Processing Query")
            for result in results:
                print(result)
    else:
        print("no duplicates in collection")


def main():
    collection = collection_for_query()
    print("Processing Query, may take a minute")
    results = list(db[collection].aggregate(pipeline, allowDiskUse=True))

    show_duplication_results(results)


if __name__ == '__main__':
    main()
