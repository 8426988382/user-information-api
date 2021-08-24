from flask_restful import Resource, reqparse
from flask import request
from models.user import UserModel


class User(Resource):
    user_parser = reqparse.RequestParser(bundle_errors=True)
    user_parser.add_argument('username',
                             type=str,
                             required=True,
                             help='username is missing')
    user_parser.add_argument('password',
                             type=str,
                             required=True,
                             help='password is missing')

    @classmethod
    def post(cls):
        try:
            # user_data = cls.user_parser.parse_args()
            user_data = request.get_json()
            username = user_data.get('username')
            password = user_data.get('password')

            print('username: ', username, " password: ", password)

            if username is None or password is None:
                return {'message': 'data not sufficient'}, 400

            attribute_updates = {'password': {'Value': password}}

            UserModel.insert_in_table(username, values=attribute_updates, table_name='users')
            UserModel.insert_in_table(username, values={}, table_name='personal_info')
            UserModel.insert_in_table(username, values={}, table_name='contact_info')
            UserModel.insert_in_table(username, values={}, table_name='educational_info')

            return {'message': 'user created successfully'}

        except ErrorException:
            return {'message': 'something went wrong!'}, 500


class ErrorException(Exception):
    pass
