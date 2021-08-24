from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)

    # first method
    # password = password + secret_key
    # hashed_password = sha1(password.encode('utf-8')).hexdigest()

    print(user)
    if user and user.password == password:
        return user


def identity(payload):
    username = payload['username']
    return UserModel.find_by_username(username)
