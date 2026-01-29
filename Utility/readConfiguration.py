import configparser
import os

config =configparser.RawConfigParser()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(BASE_DIR, "Configuration", "config.ini")

config.read(config_path)

class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get("common data","base_url")
        return url

    @staticmethod
    def get_user_email():
        username = config.get("common data","user_email")
        return  username


    @staticmethod
    def get_password():
         password= config.get("common data","user_password")
         return  password