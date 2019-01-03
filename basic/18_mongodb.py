# coding=utf-8

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# dblist = myclient.list_database_names()
# print(dblist)

mydb = myclient['myblog-dev']
# print(mydb.list_collection_names())

colPosts = mydb['posts']
for post in colPosts.find():
    print(post)
