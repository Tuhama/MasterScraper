
import requests

api="https://zonefiles.io/a/yvrkdpplafpamwm852k2/full/2772/"
response = requests.get(api, timeout=3)
print(response.text)
