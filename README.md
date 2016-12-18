# INTRO
This tool is very usefull to get infos of an open mongo DB.
To find open mongo DB :
https://www.shodan.io/search?query=port%3A27017&language=None

# USAGE
usage: mongoScan.py [-h] --host HOST [--port PORT] [--db DB]
                    [--collection COLLECTION] [--fields FIELDS] [--data DATA]
                    [--field FIELD]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Host to scan
  --port PORT           Port MongoDB (default 27017)
  --db DB               DB name to scan
  --collection COLLECTION
                        Collection name to scan
  --fields FIELDS       Print the name of the fields
  --data DATA           True/False -> Print or not the content of the
                        collection
  --field FIELD         Content of the field to print
