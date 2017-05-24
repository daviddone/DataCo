from pymongo import MongoClient


class Mongo():
    def __init__(self):
        user = "david"
        pwd = "1234"
        server = "192.168.31.111"
        port = "27017"
        uri = 'mongodb://' + user + ':' + pwd + '@' + server + ':' + port +'/'
        self.client = MongoClient(uri)
        self.db = self.client.test

    def populate(self):
        self.db.things.remove()
        things = [
            {"name": "Vishnu"},
            {"name": "Lakshmi"},
            {"name": "Ganesha"},
            {"name": "Krishna"},
            {"name": "Murugan"}
        ]
        self.db.things.insert(things)

    def count(self):
        return self.db.things.count()

if __name__ == "__main__":
    mongo = Mongo()
    mongo.populate()
    print(mongo.count())

