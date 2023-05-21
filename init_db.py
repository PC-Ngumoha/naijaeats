#!/usr/bin/env python3
"""
This is a script aimed at populating the db with some initial
database objects for our app. Just so that we can see how everything looks
"""
from app import create_app
from app.extensions import db
from app.models.category import Category
from app.models.city import City
from app.models.user import User
from app.models.menu_item import MenuItem
from app.models.review import Review
from app.models.placed_order import PlacedOrder
from werkzeug.security import generate_password_hash

app = create_app()


# Cities
abuja = City(name='Abuja')
zaria = City(name='Zaria')
umuahia = City(name='Umuahia')

# Categories
food = Category(title='Food')
drinks = Category(title='Drinks')

# Restaurants
scrum = User(org_name='Scrumptuous', email='help@scrumptuous.org',
             is_business=True, password=generate_password_hash('123456'),
             city=abuja)
biggs = User(org_name='Mr. Biggs', email='support@mrbiggs.org',
              is_business=True, password=generate_password_hash('123456'),
              city=zaria)
light = User(org_name='Light Meals', email='help@lightmealsnigeria.org',
              is_business=True, password=generate_password_hash('123456'),
              city=umuahia)
    
# MenuItems
item1 = MenuItem(title='Small Chop', price=10.00, category=food,
                  restaurant=scrum)
item2 = MenuItem(title='Orange Juice', price=5.00, category=drinks,
                  restaurant=biggs)
item3 = MenuItem(title='Beer', price=10.00, category=drinks,
                  restaurant=biggs)
item4 = MenuItem(title='Fufu & Egusi', price=7.00, category=food,
                  restaurant=scrum)
item5 = MenuItem(title='Spaghetti', price=8.00, category=food,
                  restaurant=light)
item6 = MenuItem(title='Spicy Chops', price=9.00, category=food,
                  restaurant=scrum)
item7 = MenuItem(title='French Fries', price=10.00, category=food,
                  restaurant=scrum)
item8 = MenuItem(title='Cheese Burger', price=10.00, category=food,
                  restaurant=biggs)
item9 = MenuItem(title='Tequilla', price=6.00, category=drinks,
                  restaurant=light)

with app.app_context():
    db.drop_all() # It will drop all pre-existing tables if any
    db.create_all()  # Creates all called tables in the database    
    # Adding these objects to the database session
    db.session.add_all([abuja, zaria, umuahia])
    db.session.add_all([food, drinks])
    db.session.add_all([scrum, biggs, light])
    db.session.add_all([item1, item2, item3, item4, item5, item6, item7, item8,
                        item9])
    db.session.commit() # Save the session's contents
