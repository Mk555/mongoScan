#!/usr/bin/python

import pprint
import pymongo
import argparse

# ARGS
parser = argparse.ArgumentParser()
parser.add_argument('--host', required=True, help='Host to scan')
parser.add_argument('--port', default=27017, required=False, help='Port MongoDB (default 27017)')
parser.add_argument('--db', default=False, required=False, help='DB name to scan')
parser.add_argument('--collection', default=False, required=False, help='Collection name to scan')
parser.add_argument('--fields', type=bool, required=False, default=False, help='Print the name of the fields')
parser.add_argument('--data', type=bool, required=False, default=False, help='True/False -> Print or not the content of the collection')
parser.add_argument('--field', required=False, default=False, help='Content of the field to print')


args = parser.parse_args()

# VARS
#dbAddr = '107.170.195.35'
#dbAddr = '52.35.222.227'
dbAddr = args.host
dbPort = args.port
dbName = args.db
collName = args.collection
fieldName = args.field

# FUNCTIONS

# Print the field names of a collection 
def printFields( collection ):
  db = client[dbName]
  item = db[collection].find_one()
  print('[+] Fields for [' + dbName + '][' + collName + '] : ')
  for field in item:
    print( '  [+] ' + field)
###

# Print the content of a collection
def printRawData( collection ):
  db = client[dbName]
  cursor = db.events.find()
  print('[+] Data [' + dbName + '][' + collName + '] : ')
  for item in cursor:
    pprint.pprint(item)
###

def scanDB():
  print('[ ] Databases avaible :')
  for database in client.database_names():
    print('[+]  [' + database + ']')
    db = client[database]
    print('[ ]  Collections :')
    for collection in db.collection_names():
      print('[+]    [' + collection + ']')
###

def printField( collection, field ):
  db = client[dbName]
  cursor = db.events.find()
  print('[+] Data [' + dbName + '][' + collName + '] : ')
  for item in cursor:
    print('  [+] ' + item[field])



# MAIN
# Create the connexion
client = pymongo.MongoClient(dbAddr, dbPort)
print('[ ] Connecting ' + dbAddr + ':' + str(dbPort))

try:
  # Debug
  #pprint.pprint(client.server_info())
  client.server_info()
except pymongo.errors.ServerSelectionTimeoutError:
  print('[-] Connexion failed !')

print('[+] Connexion established !')

if args.db == False:
  scanDB()
elif args.collection != False and args.fields == True:
  printFields(collName)
elif args.collection != False and args.data == True:
  printRawData(collName)
elif fieldName != False and args.db != False:
  printField(collName, fieldName)


exit(0)

