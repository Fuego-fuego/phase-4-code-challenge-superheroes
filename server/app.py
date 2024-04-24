#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from sqlalchemy import asc
from models import db, Hero, Power, HeroPower
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# start of index
@app.route('/')
def index():
    return '<h1>Code challenge</h1>'
# end of index
# start of heroes
@app.route('/heroes')
def heroes():
    if request.method=='GET':
        heroes = []        
        for hero in Hero.query.all():
            hero_dict = {
                "id":hero.id,
                "name":hero.name,
                "super_name": hero.super_name
            }
            heroes.append(hero_dict)
        
        return make_response(heroes, 200)

@app.route('/heroes/<int:id>')
def hero_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()
    
    if hero == None:
        response_body = {
            "error": "Hero not found"
        }
        
        response = make_response(response_body, 404)        
        return response
    else:
        if request.method == 'GET':
            hero_dict= hero.to_dict()
            
            return make_response(hero_dict,200)
# end of heroes
# start of powers
@app.route('/powers')
def powers():
    if request.method=='GET':
        powers = []        
        for power in Power.query.all():
            power_dict = {
                "description":power.description,
                "id":power.id,
                "name": power.name
            }
            powers.append(power_dict)
        
        return make_response(powers, 200)
    
    
@app.route('/powers/<int:id>', methods=['GET','PATCH'])
def power_by_id(id):
    power = Power.query.filter(Power.id == id).first()
    
    if power == None:
        response_body = {
            "error": "Power not found"
        }
        
        response = make_response(response_body, 404)        
        return response
    else:
        if request.method == 'GET':
            power_dict= {
                "description":power.description,
                "id":power.id,
                "name": power.name
            }
            
            return make_response(power_dict,200)
        elif request.method=='PATCH':
            for attr in request.get_json():
                data=request.get_json()
                setattr(power,attr,data[attr])
                
            db.session.add(power)
            db.session.commit()
            power_dict = power.to_dict()        
            
        
        return make_response(power_dict, 200)
            
# end of powers
# start of hero_powers
@app.route('/hero_powers', methods=['POST'])
def hero_powers():
    if request.method=='POST':
        data=request.get_json()
        power = Power.query.filter(Power.id==data['power_id']).first().to_dict()
        hero = Hero.query.filter(Hero.id==data['hero_id']).first().to_dict()
        new_hero_power = HeroPower(
            strength=data['strength'],
            power_id=power,
            hero_id=hero            
        )
        
        db.session.add(new_hero_power)
        db.session.commit()        
        new_hero_power_dict = new_hero_power.to_dict()        
            
        
        return make_response(new_hero_power_dict, 200)
        
if __name__ == '__main__':
    app.run(port=5555, debug=True)
