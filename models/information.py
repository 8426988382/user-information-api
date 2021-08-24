from utils.DB_helper import DatabaseConnection
from models.user import UserModel


class Information:
    def __init__(self, username: str, type_of_information: str):
        self.type_of_information = type_of_information
        self.username = username

    def update_table(self, values):
        check_for_username = UserModel.find_by_username(username=self.username)
        if check_for_username == -1:
            return 0
        key = {'username': self.username}
        try:
            table_name = self.type_of_information + "_info"  # try to put in env variable
            with DatabaseConnection('dynamodb', table_name) as table:
                table.update_item(Key=key, AttributeUpdates=values)
                return 1
        except ErrorException:
            return -1

    def get_from_table(self):
        check_for_username = UserModel.find_by_username(username=self.username)
        if check_for_username is None:
            return 0
        information_type = INFO_TYPES.get(self.type_of_information)  # try to put in env variable
        if information_type:
            key = {'username': self.username}
            return information_type(key)

        return -1

    @staticmethod
    def personal_info(key):
        try:
            with DatabaseConnection('dynamodb', 'personal_info') as table:
                data = table.get_item(Key=key).get('Item')
                if data:
                    return data  # make separate classes for information

            return -1
        except ErrorException:
            return -1

    @staticmethod
    def contact_info(key):
        try:
            with DatabaseConnection('dynamodb', 'contact_info') as table:
                data = table.get_item(Key=key).get('Item')
                if data:
                    return data  # make separate classes for information

            return -1
        except ErrorException:
            return -1

    @staticmethod
    def educational_info(key):
        try:
            with DatabaseConnection('dynamodb', 'educational_info') as table:
                data = table.get_item(Key=key).get('Item')
                if data:
                    return data  # make separate classes for information

            return -1
        except ErrorException:
            return -1


INFO_TYPES = {
    'personal': Information.personal_info,
    'contact': Information.contact_info,
    'educational': Information.educational_info,
}


class ErrorException(Exception):
    pass
