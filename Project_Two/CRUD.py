from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):

        #Connection configuration
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31203
        DB = 'AAC'
        COL = 'animals'
        
        #Initialize MongoClient with the provided credentials
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]
        
        print("Connection Successful")

# Create Method to add details to the DB
    def create(self, data):
        
        try:
            if data is not None:
                self.collection.insert_one(data)
                return True
            
            else:
                raise ValueError("Nothing to save, because data parameter is empty")
        except Exception as e:
                print("New An exception occurred ::", e)
                return False

# Read Method to read documents from the DB
    def read(self, data):
        try:
            if data is not None:
                query = list(self.database.animals.find(data))
                return query
            
            else:
                raise ValueError("Data parameter is empty")
            
        except Exception as e:
            print("Another exception occurred ::", e)
            return []
    
# Update to update details in DB
    def update(self, readData, updateData):
        try:
            if readData is not None:
                #Passes search argument and returns back the query
                index_update = self.database.animals.update(readData, {"$set":updateData})
                return index_update
            
            else:
                return {}
             
          #Exception Handling   
        except Exception as e:
            print("An exception occurred ::", e)       


# Delete entry method in DB
    def delete(self, data):
        try:
            if data is not None:
                #Passes search argument and returns back the query
                delete= self.database.animals.delete_many(data)
                return delete
                          
            else:
                return {}
            
         #Exception Handling   
        except Exception as e:
            print("An exception occurred ::", e)