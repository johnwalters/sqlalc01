import sys
sys.path.append(r'C:/Users/johnw_000\AppData/Local/Programs/Python/Python37-32/Lib/site-packages')
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
session.query(Person).all()
# Return the first Person from all Persons in the database
person = session.query(Person).first()
print ('person 1 name:' + person.name)
session.query(Address).filter(Address.person == person).all()
# Retrieve one Address whose person field is point to the person object
session.query(Address).filter(Address.person == person).one()
address = session.query(Address).filter(Address.person == person).one()
print ('First Address post_code:' + address.post_code)
