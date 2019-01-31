from model import Base, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///databases.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_item(name, price, picture, link):
    item_object = Item(name=name,
     price=price, picture=picture, link=link)
    session.add(item_object)
    session.commit()

add_item('Bohemian Rhapsody (The Original Soundtrack)', '$11.79', '/static/img/shop1.jpg','https://www.queenonlinestore.com/*/*/Bohemian-Rhapsody-The-Original-Soundtrack/5XR70000000')
add_item('Jazz World Tour 1978-79 Ringer T-Shirt','$39.99', '/static/img/shop2.jpg','https://www.queenonlinestore.com/*/*/-Jazz-World-Tour-1978-79-Ringer-T-Shirt/5Z0D0000000')
add_item('Queen Distressed T-shirt','$19.99','/static/img/shop3.jpg','https://www.rockabilia.com/browse/artists-groups/q/queen/queen-queen-distressed-t-shirt-411747.html')
add_item('Crest Type Mug Coffee Mug','$18.99', '/static/img/shop4.jpg','https://www.rockabilia.com/browse/artists-groups/q/queen/queen-crest-type-mug-coffee-mug-403920.html')
add_item('2018 Brian May Jazz Sixpence','$10','/static/img/shop5.jpg','https://www.queenonlinestore.com/*/*/2018-Brian-May-Jazz-Sixpence/5WY60000000')
add_item('Jazz 40th Anniversary Unisex White Sweatshirt','$39.15','/static/img/shop6.jpg','https://www.queenonlinestore.com/*/*/Smile/5YRN0000000')
add_item('Bohemian Rhapsody Double Vinyl LP','$35.23','/static/img/shop7.jpg','https://www.queenonlinestore.com/*/*/Bohemian-Rhapsody/60OW0000000')
add_item('Smile T-Shirt','$32.63','/static/img/shop8.jpg','https://www.queenonlinestore.com/*/*/Bohemian-Rhapsody/60OW0000000')


def query_all_items():
    items = session.query(
    	Item).all()
    return items

# def query_user_by_name(username):
# 	name = session.query(
# 		User).filter_by(name=username).first()
# 	return name

# def query_by_name_and_password(username, password):
#     return session.query(User).filter_by(name = username, password = password).first()

# def delete_user_by_id(user_id):
#     post = session.query(User).filter_by(id_table=user_id).delete()
#     session.commit()

# def query_user_by_id(user_id):
#     user = session.query(
#         User).filter_by(id_table=user_id).first()
#     return user

# def delete_all_users():
#     session.query(User).delete()
#     session.commit()

# def add_Post(post_string):
#     post_object = Post(post_string=post_string)
#     session.add(post_object)
#     session.commit()

# def query_all_posts():
#     posts = session.query(
# Post).all()
#     return posts

# def query_post_by_id(post_id):
#     post = session.query(Post).filter_by(id_table=post_id).first()
#     return post

# def delete_all_posts():
#     session.query(Post).delete()
#     session.commit

# def delete_post_by_id(post_id):
#     post = session.query(Post).filter_by(id_table=post_id).delete()
#     session.commit()

