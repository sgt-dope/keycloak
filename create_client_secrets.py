import json
import os

cmnd = os.popen("gp url 8080")
gitpod_url = cmnd.read().strip()

cmnd2 = os.popen("gp url 5000")
gitpod_url_app = cmnd2.read().strip()

realm_name = "flask-demo"
client_id = "flask-app"


# Client_secret is only required when the client is set to confidential and not public. Otherwise
# It can be ignored. However, its existence doesn't affect anything.

client_secrets = {
    "web":{
        "issuer": gitpod_url + "/auth/realms/" + realm_name,
        "auth_uri": gitpod_url + "/auth/realms/" + realm_name + "/protocol/openid-connect/auth",
        "client_id": client_id,
        "client_secret": "a41060dd-b5a8-472e-a91f-6a3ab0e04714",
        "redirect_uris": [
            gitpod_url_app + "/*"
        ],
        "userinfo_uri": gitpod_url + "/auth/realms/" + realm_name + "/protocol/openid-connect/userinfo",
        "token_uri": gitpod_url + "/auth/realms/" + realm_name + "/protocol/openid-connect/token",
        "token_introspection_uri": gitpod_url + "/auth/realms/" + realm_name + "/protocol/openid-connect/token/introspect"
    }
}
jsonString = json.dumps(client_secrets)
jsonFile = open("client_secrets.json", "w")
jsonFile.write(jsonString)
jsonFile.close()