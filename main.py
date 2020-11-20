import redis
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
          'SERVICE_NAME': 'FlaskApp',
          'SECRET_TOKEN': '',         
          'SERVER_URL': 'http://localhost:8200'
}
apm = ElasticAPM(app)

redis = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    redis.incr('visitor')
    return 'Hello, World!'



@app.route('/visitor')
def visitor():
    redis.incr('visitor')
    visitor_num = redis.get('visitor').decode("utf-8")
    return "Visitor: %s" % (visitor_num)


@app.route('/visitor/reset')
def reset_visitor():
    redis.set('visitor', 0)
    visitor_num = redis.get('visitor').decode("utf-8")
    return "Visitor is reset to %s" % (visitor_num)



@app.route('/erro')

def index():
 return "Quebra!"

@app.errorhandler(404)
def not_found_error(error):
 return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
 return render_template('500.html'), 500

@app.route('/divbyzero')          
def divbyzero():             
    num = 2 / 0              
    return "Quebra - " + str(num)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
