from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///looks.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_products(name, picture, category):
	add_products= Products(
        name=name,
        picture=picture,
        category=category)
	session.add(add_products)
	session.commit()


def search_db(keyword):
	single_search = session.query(Products).filter(Products.picture==keyword or Products.category==keyword or Products.name==keyword)
	if single_search.first():
		return single_search
	else:
		return None







add_products("Bohemian Raphsody","shop1.jpg ","clothes" )
add_products("Queen Tshirt","shop3.jpg ","clothes" )
add_products("Jazz Tshirt","shop2.jpg ","clothes" )
add_products("Mug","shop4.jpg ","clothes" )
add_products("Brian May Jazz","shop5.jpg ","clothes" )
add_products("Jazz unisex","shop8.jpg ","clothes")
add_products("Bohemian Raphsody","shop6.png ","clothes" )
add_products("Smile","shop7.jpg ","clothes" )


   
def query_all():
	products=session.query(Products).all()
	return products

def query_by_name(name):
	products=session.query(Products).filter_by(name=name).first()
	return products 


def query_by_category(category):
	products=session.query(Products).filter_by(category=category).first()
	return products


print(query_all())