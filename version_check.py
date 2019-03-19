import os

# trying to install SQLAlchemy shows me where it is already installed
# C:\python34> pip install SQLAlchemy
# Requirement already satisfied: SQLAlchemy in c:\users\johnw_000\appdata\local\programs\python\python37-32\lib\site-packages
# so I append that location to the path (because I don't know how to add that to environment path)

import sys
sys.path.append(r'C:/Users/johnw_000/AppData/Local/Programs/Python/Python37-32/Lib/site-packages')

import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
v = sqlalchemy.__version__
print ('sqlalchemy version: ' + v)