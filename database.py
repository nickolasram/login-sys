import pymongo


# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system
