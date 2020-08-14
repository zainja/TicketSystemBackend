import http.client
import json

conn = http.client.HTTPConnection("localhost", 5000)
headers = {'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.emFpbmphMw.j7nE5Vw1RjV8jrC6STvGDe3oJgouU2oMdvChZgMydNo",
           "Content-Type": "application/json"}
reqInfo = {
    "teamName": "ffff22 team"
}
reqInfo = json.dumps(reqInfo)
conn.request("POST", "/team-users/get-all-users", reqInfo, headers)

response = conn.getresponse()
data = response.read().decode()
users = json.loads(data)["users"]
print(users)
for u in users:
    dToSend = {"teamName": "ffff22 team", "teamMember": u["username"]}
    reJSON = json.dumps(dToSend)
    conn.request("POST", "/team/add-member", reJSON, headers)
    response = conn.getresponse().read().decode()
    print(response)