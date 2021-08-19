from keycloak import KeycloakAdmin
import os

# When creating realms, users or otherwise, make sure that they are enabled.

cmnd = os.popen("gp url 8080")
gitpod_url = cmnd.read().strip() + "/auth/"


keycloak_admin = KeycloakAdmin(server_url=gitpod_url,
                               username='admin',
                               password='admin',
                               realm_name="master",
                               verify=True)



realm_name = "flask-demo"
keycloak_admin.create_realm(payload={"realm": "flask-demo",
                                    "enabled" : True}, skip_exists=False)

keycloak_admin.realm_name = realm_name

client_name = "flask-app"
keycloak_admin.create_client(payload={"clientId": client_name,
                                        "enabled" : True,
                                        "directAccessGrantsEnabled" : True,
                                        "redirectUris":["*"],
                                        "protocol": "openid-connect"}, skip_exists=False)

# Setting up the protocol to be openid-connect will automatically make the Access Type Public
# It'll also set the Backchannel Logout Session Required to ON

new_user = keycloak_admin.create_user({"email": "kenannakola@hotmail.com",
                    "username": "kenannakola@hotmail.com",
                    "enabled": True,
                    "firstName": "Kenan",
                    "lastName": "Alnakoula"})