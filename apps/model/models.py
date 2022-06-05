from configparser import ConfigParser
from datetime import datetime
from email.policy import default
from peewee import (
    SQL,
    MySQLDatabase, 
    Model, 
    CharField,
    BigIntegerField,
    FloatField
)


conf = ConfigParser()
conf.read(filenames='model/config.ini')

db = MySQLDatabase(
    'trans_lab_db', 
    user='lama', 
    password='Drama22#', 
    port=3306, 
    host='localhost'
)


class Users(Model):
    id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    login = CharField(max_length=30)
    password = CharField(max_length=500)

    class Meta:
        database = db # This model uses the "people.db" database.


class Cars(Model):
    car_id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    name = CharField(max_length=35)
    model_car = CharField(max_length=255)
    year_car = CharField(max_length=5)
    volume_engine = FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.

class ApplicationTos(Model):
    id = BigIntegerField(primary_key=True, unique=True,
                        constraints=[SQL('AUTO_INCREMENT')])
    email = CharField(max_length=30, default=' - ')
    tel = CharField(max_length=20)
    username = CharField(max_length=255)
    name = CharField(max_length=35)
    model_car = CharField(max_length=255)
    year_car = CharField(max_length=5)
    volume_engine = FloatField()


    class Meta:
        database = db # This model uses the "people.db" database.