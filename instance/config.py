import os

# flask config
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', '5000')

# mongo env
MONGOALCHEMY_DATABASE = os.getenv('MONGOALCHEMY_DATABASE','library')
#MONGOALCHEMY_SERVER = os.getenv('MONGOALCHEMY_SERVER','172.16.16.6')
#MONGOALCHEMY_PORT = os.getenv('MONGOALCHEMY_PORT', 27017)
#MONGOALCHEMY_USER = os.getenv('MONGOALCHEMY_USER', 'mongo')
#MONGOALCHEMY_PASSWORD = os.getenv('MONGOALCHEMY_PASSWORD', 'mongo')
MONGOALCHEMY_CONNECTION_STRING = os.getenv('MONGO_URI', "mongodb://mongo:mongo@127.0.0.1:27017/library")
