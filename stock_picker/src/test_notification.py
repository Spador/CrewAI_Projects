import os, requests

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
message = "Test push from Stock Picker 🚀"

r = requests.post(
    "https://api.pushover.net/1/messages.json",
    data={"user": pushover_user, "token": pushover_token, "message": message}
)

print(r.status_code, r.text)