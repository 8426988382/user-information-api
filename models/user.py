from utils.DB_helper import DatabaseConnection


class UserModel:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<{self.username}, {self.password}>"

    @classmethod
    def find_by_username(cls, username):
        try:
            with DatabaseConnection('dynamodb', 'users') as table:
                key = {'username': username}
                data = table.get_item(Key=key).get('Item')
                print(data)
                if data:
                    user = cls(data.get('username'), data.get('password'))
                else:
                    user = None

                return user
        except ErrorException:
            return -1

    @staticmethod
    def insert_in_table(username, table_name, values=None):
        try:
            key = {'username': username}
            with DatabaseConnection('dynamodb', table_name) as table:
                table.update_item(Key=key, AttributeUpdates=values)
        except ErrorException:
            raise ErrorException()


class ErrorException(Exception):
    pass
