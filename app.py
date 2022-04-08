import os
import time
from datetime import datetime as dt
from flask import request, Flask, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import json
from flask_migrate import Migrate, migrate



app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# # Settings for migrations
migrate = Migrate(app, db)




class DataTable(db.Model):
    
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    request = db.Column(
        db.String(), 
        unique=False, 
        nullable=False
    )
    created_at = db.Column(
        db.Integer,
        unique=False,
        nullable=True
    )
 
  
    def __init__(self, request, created_at):
        self.request  = request
        self.created_at = created_at
        

db.create_all()

@app.route('/')
def index():
    return 'Test project for partium'


# routing config
@app.route('/partium/echoservice', methods=['POST'])
def process_json():
    try:
        data = json.loads(request.data)
        timestamp = dt.now()
        timestamp = time.mktime(timestamp.timetuple())
        record = DataTable(request =str(data), created_at =  timestamp )
        db.session.add(record)
        db.session.commit()
        
        return json.dumps({'request': data, 'created_at' : timestamp})
    except:
        return json.dumps({'message': 'invalid request'})

@app.route('/partium/test')
def view_db():
    try:
              
        return render_template('test.html', data = DataTable.query.all())
    except:
        return json.dumps({'message': 'invalid request'})


    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')