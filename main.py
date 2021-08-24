from flask import Flask, redirect, request, jsonify
from flask_awscognito import AWSCognitoAuthentication
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['AWS_DEFAULT_REGION'] = 'eu-east-1'
app.config['AWS_COGNITO_DOMAIN'] = 'https://tusharpooldemo.auth.us-east-1.amazoncognito.com'
app.config['AWS_COGNITO_USER_POOL_ID'] = 'us-east-1_81A0DTZfd'
app.config['AWS_COGNITO_USER_POOL_CLIENT_ID'] = '6ul1h63v5td11ja4581v6a3qa8'
app.config['AWS_COGNITO_USER_POOL_CLIENT_SECRET'] = 'fdlosvceqlmgd5e70gub5skp4cr0s4aommk83hiuh7alduhdk9u'
app.config['AWS_COGNITO_REDIRECT_URL'] = 'http://localhost:5000/aws_cognito_redirect'

aws_auth = AWSCognitoAuthentication(app)


@app.route('/')
@aws_auth.authentication_required
def index():
    claims = aws_auth.claims  # also available through g.cognito_claims
    return jsonify({'claims': claims})


@app.route('/aws_cognito_redirect')
def aws_cognito_redirect():
    access_token = aws_auth.get_access_token(request.args)
    return jsonify({'access_token': access_token})


@app.route('/sign_in')
def sign_in():
    return redirect(aws_auth.get_sign_in_url())


if __name__ == '__main__':
    app.run(debug=True)
