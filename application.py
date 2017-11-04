from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Show all restaurants
@app.route('/')
@app.route('/restaurant')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('mainpage.html', restaurants = restaurants)

#Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return render_template('menupage.html', items = items, restaurant = restaurant)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
