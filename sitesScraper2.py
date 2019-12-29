import json

with open('jsonFiles/eduSites.json', 'r') as f:
    edu_results = json.load(f)

with open('jsonFiles/govSites.json', 'r') as f:
    gov_results = json.load(f)

with open('jsonFiles/syrianSites.json', 'r') as f:
    alexa_results = json.load(f)

all_sites = edu_results + gov_results

for site in alexa_results:
    for s in all_sites:
        if site["name"] in s:
            break
    else:
        all_sites.append(site["name"])

f = open("jsonFiles/finalSites.json", "w")
f.write(json.dumps(all_sites, indent=4, sort_keys=True))
f.close()

