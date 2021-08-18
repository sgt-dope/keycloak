from keycloak import KeycloakAdmin
import os

# When creating realms, users or otherwise, make sure that they are enabled.

cmnd = os.popen("gp url 8080")
gitpod_url = cmnd.read().strip() + "/auth/"


keycloak_admin = KeycloakAdmin(server_url="https://8080-gold-fish-93s37204.ws-eu15.gitpod.io/auth/",
                               username='admin',
                               password='admin',
                               realm_name="master",
                               verify=True)


realm_name = "flask-demo"
keycloak_admin.create_realm(payload={"realm": "flask-demo"}, skip_exists=False)

keycloak_admin.realm_name = realm_name

keycloak_admin.create_client(payload={"clientId": "hello_app"}, skip_exists=False)

new_user = keycloak_admin.create_user({"email": "kenannakola@hotmail.com",
                    "username": "kenannakola@hotmail.com",
                    "enabled": True,
                    "firstName": "Kenan",
                    "lastName": "Alnakoula"})