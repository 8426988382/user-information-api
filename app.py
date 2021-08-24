from flask_lambda import FlaskLambda
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS
import datetime
from datetime import timedelta

from resources.user import User
from resources.information import Info
from utils.security import authenticate, identity

app = FlaskLambda(__name__)
app.config['SECRET_KEY'] = 'secret1233hello12there'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=300)
app.config['JWT_NOT_BEFORE_DELTA'] = timedelta(seconds=0)
api = Api(app)

CORS(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)


@jwt.jwt_payload_handler
def make_payload(identity):
    iat = datetime.datetime.utcnow()
    exp = iat + app.config.get('JWT_EXPIRATION_DELTA')
    nbf = iat + app.config.get('JWT_NOT_BEFORE_DELTA')
    return {
        'username': identity.username,
        'role': 'user',
        'iat': iat,
        'exp': exp,
        'nbf': nbf
    }


api.add_resource(User, '/user')
api.add_resource(Info, '/info')  # /info?info=personal

if __name__ == '__main__':
    app.run(debug=True)
