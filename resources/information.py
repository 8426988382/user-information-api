from flask_restful import Resource
from flask import request
from flask_jwt import jwt_required, current_identity

from models.information import Information
from utils.fields import check_for_values


class Info(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        information_type = request.args.get('info')

        identity = current_identity
        print("identity", identity)

        if information_type is None or identity is None:
            return {'message': 'insufficient arguments'}, 400

        data_object = Information(username=identity.username, type_of_information=information_type)
        data = data_object.get_from_table()

        if data == -1:
            return {'message': 'error fetching the data'}, 500
        if data == 0:
            return {'message': 'please login with valid credentials'}, 401

        return {information_type: data}, 200

    @classmethod
    @jwt_required()
    def put(cls):
        try:
            information_type = request.args.get('info')
            identity = current_identity

            values = request.get_json()

            if information_type is None or identity.username is None:
                return {'message': 'insufficient arguments'}, 400

            value_check = check_for_values(values.keys(), information_type)

            print(value_check)
            if value_check == -1:
                return {'message': 'unexpected data'}, 400
            elif value_check == 0:
                return {'message': 'some error has occurred'}, 500

            if values:
                data_object = Information(username=identity.username, type_of_information=information_type)

                attribute_updates = {key: {'Value': value, 'Action': 'PUT'}
                                     for key, value in request.get_json().items()}

                result = data_object.update_table(values=attribute_updates)

                if result == 0:
                    return {'message': 'please login with valid credentials'}, 401

                if result == 1:
                    return {'message': 'data updated successfully'}
                else:
                    return {'message': 'error in updating the values'}, 500

            return {'message': 'provide some values to update'}, 400
        except:
            return {'message': 'cannot update values'}, 400
