from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import selectable
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import MetaData, Table
from flask_migrate import Migrate
from flask import request
from sqlalchemy import engine, text
import json
import re

from config import app_config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def test():
        return 'Hello! I am back with db running .!'

    @app.route('/getall', methods=['GET'])
    def fetch():
        sql = 'Select * from users_db'
        users = db.engine.execute(sql)
        all_users = []
        for user in users:
            new_user = {
            "id": user.id,
            "name": user.name,
            "address": user.address,
            "phone": user.phone,
            "mobile_phone":user.mobile_phone,
            "email":user.email
            }
            all_users.append(new_user)
        return json.dumps(all_users, sort_keys=True), 200
    
    #Get User(s) by any property according to given any property key value pair
    @app.route('/search/<property>:<value>' , methods=['GET'])
    def fetch_search(property,value):
        mytable = Table('users_db', db.metadata, autoload_with=db.engine)
        if property=='name':
           users=db.session.query(mytable).filter_by(name=value)
        elif property=='adress':
           users=db.session.query(mytable).filter_by(address=value)
        elif property=='phone':
           users=db.session.query(mytable).filter_by(phone=value)
        elif property=='mobile_phone':
           users=db.session.query(mytable).filter_by(mobile_phone=value)
        elif property=='email':
           users=db.session.query(mytable).filter_by(email=value)     
        else: 
            return json.dumps("Please provide a valid property key (valid keys are : name,address,phone,mobile_phone,email) !"), 200   
        all_users = []
        for user in users:
            new_user = {
            "id": user.id,
            "name": user.name,
            "address": user.address,
            "phone": user.phone,
            "mobile_phone":user.mobile_phone,
            "email":user.email
            }
            all_users.append(new_user)
        return json.dumps(all_users, sort_keys=True), 200
    

    @app.route('/add', methods=['POST'])
    def add():
        data = request.get_json()
        name = data['name']
        if name=='':
            return json.dumps('Name cannot be empty, please provide valid name !'), 400        
        address = data['address']
        if address == '':
            return json.dumps('Address cannot be empty, please provide valid address !'), 400
        phone = data['phone']
        if phone == '':
            return json.dumps('Phone cannot be empty, please provide valid phone !'), 400
        mobile_phone = data['mobile_phone']
        email = data['email']
        if not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
            return json.dumps('Email is not valid, please provide valid email !'), 400
        mytable = Table('users_db', db.metadata, autoload_with=db.engine)
        db.engine.execute(mytable.insert(), {"name": name , "address": address, "phone": phone, "mobile_phone": mobile_phone, "email": email})
        return json.dumps('User added successfully !'), 200

    @app.route('/edit/<name>', methods=['PUT'])
    def edit(name):
        data = request.get_json()
        address = data['address']
        phone = data['phone']
        mobile_phone = data['mobile_phone']
        email = data['email']
        mytable = Table('users_db', db.metadata, autoload_with=db.engine)
        db.engine.execute(mytable.update().where(mytable.c.name==name),{"address": address, "phone": phone, "mobile_phone": mobile_phone, "email": email} )
        return json.dumps("User edited successfully !"), 200


    @app.route('/remove/<name>', methods=['DELETE'])
    def remove(name):
        mytable = Table('users_db', db.metadata, autoload_with=db.engine)
        db.engine.execute(mytable.delete().where(mytable.c.name==name))
        return json.dumps("User deleted succesfully !"), 200

    


    migrate = Migrate(app,db)

    from .models import Users
    from app import models

    return app
