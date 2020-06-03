import os

class Config(object):
    SECRET_KEY =os.environ.get('SECRET_KEY') or "secret_string"



    MONGODB_SETTINGS ={
        'db':'cgsuppliers',
        'host':"mongodb+srv://admin:admin@cluster0-b8t27.mongodb.net/test?retryWrites=true&w=majority"
        }