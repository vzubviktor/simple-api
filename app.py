import os
from datetime import datetime as dt
from flask import request, Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import json
from flask_migrate import Migrate, migrate



app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# # Settings for migrations
migrate = Migrate(app, db)

app = Flask(__name__)


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
    created_at = created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"DataTable : {self.request}"

db.create_all()


def createRecord(data):
    try:
        new_record = DataTable(
            request = data,
            created_at = dt.now()
        )
        return new_record
    except:
        pass
    




@app.route('/')
def index():
    return 'Flask running'


# routing config
@app.route('/test', methods=['POST'])
def process_json():
    try:
        data = json.loads(request.data)
        print('1st try')
        # db.session.add(new_user)
        return data
    except:
        pass
    try:
        data = request.data
        print('2nd try')
        return  data
    except:
        return json.dumps({'message': 'invalid request'})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')