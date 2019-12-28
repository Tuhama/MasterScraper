import requests
import json
headers = {
    'apikey': '61fd9270-2881-11ea-af1f-df9daa794bbc',
}

params = (
    ('q', 'site: .sy'),
    ('location', 'United States'),
    ('search_engine', 'google.com'),
    ('gl', 'US'),
    ('hl', 'en')
)

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)

f = open("jsonFiles/ZenSyrianSites.json", "w")
f.write(json.dumps(response.json(), indent=4, sort_keys=True))
f.close()

