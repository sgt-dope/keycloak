from flask import Flask
from flask_oidc import OpenIDConnect
import os

app = Flask(__name__)


cmnd = os.popen("gp url 5000")
app_url = cmnd.read().strip()

app.config.update({
    'SECRET_KEY': '86a621e9fa20b43512728114aee763879efd3803e84a2034',
    'OVERWRITE_REDIRECT_URI' : app_url+"/oidc_callback",
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'flask-demo',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

oidc = OpenIDConnect(app)

@app.route("/")
def index():
    return "<a href='/login'>login please</a>"

@app.route("/login")
@oidc.require_login
def login():
    return "Welcome to this top secret page"


@app.route('/logout')
def logout():
    oidc.logout()
    return 'Hi, you have been logged out! <a href="/">Return</a>'

if __name__ == "__main__":
    app.run()