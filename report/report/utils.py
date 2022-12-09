import pymongo
client = pymongo.MongoClient('mongodb+srv://admin:w41I0DHA3EkkYY8V@sprint4.jcenge9.mongodb.net/?retryWrites=true&w=majority')

db = client['requests']
#collection object
collection = db['requests']

def reportesCredito():
    resp=""
    cursor = collection.find({})
    for document in cursor:
        resp=resp + str(document) + "\n" 
    print(resp)
    return resp    
    
def reportesEmpresas():
    resp=""
    for emp in collection.find().distinct('Empresa'):
        resp=resp + emp + "\n" 
    print(resp)
    return resp

reportesEmpresas()
