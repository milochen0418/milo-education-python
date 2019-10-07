

from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECREC_KEY'] = 'thisisthesecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message':'Token is missing' }), 403
        try:
            data = jwt.decode(token, app.config['SECREC_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'This is only avaliable for people with valid token'})


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECREC_KEY'] )
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    print('open http://<HOST>/login and input correct password and username. then the page will return token')
