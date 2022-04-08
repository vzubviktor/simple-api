# Simple-api service example  example

Using Flask to build a Simple API Server with connection to a database .

Integration with Flask-SQLalchemy and SQLite.

### Extension:


- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)


## Installation


Install with pip:

```
$ pip install -r requirements.txt
```



## Run APP
### Run APP for develop
```
$ python simple-api/app.py
```
In flask, Default port is `5000`

Development server by default will run on the localhost:5000

Please check your terminal for the exact address at which application will be running 

### Run with Docker

```
$ docker build -t simple-api.

$ docker run -p 5000:5000 --name simple-api simple-api 
 
```
In image building, the simple-api folder will also add into the image

# API overview

## endpoints overview 


* /partium/echoservice 
* /partium/test 

base url  = localhost:5000

## REST API

The REST API to the example app is described below.

## Put request into a database 

### Request

`POST /partium/echoservice`

    curl -X POST -H "Content-type: application/json" -d "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}"  http://localhost:5000/partium/echoservice

### Response

    {"request": {"firstName": "John", "lastName": "Smith"}, "created_at": 1649432200.0}
    
## View Data Base as HTML table 
### Request

`GET /partium/test`

    curl -v http://localhost:5000/partium/test

### Response

HTTP/1.1 200 OK
Server: Werkzeug/2.1.1 Python/3.8.10
Date: Fri, 08 Apr 2022 15:39:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1013


<table>
  <thead>
    <tr>
        <th>ID</th>
        <th>request</th>
        <th>timestamp</th>
    </tr>
    </thead>    
    <tbody>
         
            <tr>
                <td>1</td>
                <td>{&#39;firstName&#39;: &#39;John&#39;, &#39;lastName&#39;: &#39;Smith&#39;}</td>
                <td>1649427396</td>
            </tr>
            
            <tr>
                <td>2</td>
                <td>{&#39;firstName&#39;: &#39;John&#39;, &#39;lastName&#39;: &#39;Smith&#39;}</td>
                <td>1649429848</td>
            </tr>
            
            <tr>
                <td>3</td>
                <td>{&#39;firstName&#39;: &#39;John&#39;, &#39;lastName&#39;: &#39;Smith&#39;}</td>
                <td>1649432200</td>
            </tr>
        
    </tbody>
</table></body>

## Error handling

Error responses include a common message for the developer

    {
      "message" : "invalid request"
    }


## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```
### Configuring From Files

#### Example Usage

```
app = Flask(__name__ )
app.config.from_pyfile('config.Development.cfg')
```


# Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)
- [Flask restplus](http://flask-restplus.readthedocs.io/en/stable/)
- [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)















