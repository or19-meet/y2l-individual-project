from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Item(Base):
	__tablename__="items"
	id=Column(Integer, primary_key=True)
	name=Column(String)
	price=Column(String)
	picture=Column(String)
		


# class User(Base):
#     __tablename__ = "User"
#     id_table = Column(Integer, primary_key = True)
#     name = Column(String)
#     password = Column(String)

#     def __repr__(self):
#         return ("Username: {},\n"
#             "password: {}. \n"
#         	).format(
#         		self.name,
#                 self.password)

# class Post(Base):
#     __tablename__ = "Post"
#     id_table = Column(Integer, primary_key = True)
#     post_string = Column(String)

#     def __repr__(self):
#         return ("{} \n "
#             "\n").format(
#                 self.post_string)

