import json

with open('jsonFiles/edu_items.json', 'r') as f:
    edu_results = json.load(f)

with open('jsonFiles/gov_items.json', 'r') as f:
    gov_results = json.load(f)

sy_gov_sites = []
sy_edu_sites = []

# for result in edu_results:
#     url = result["url"]
#     if ".sy" in url and "google" not in url:
#         if str(url).startswith("http://"): url = url[7:]
#         elif str(url).startswith("https://"): url = url[8:]
#
#         if str(url).startswith("www."): url = url[4:]
#         sy_edu_sites.append(url)

for result in gov_results:
    url = result["url"]
    if ".sy" in url and "google" not in url:
        if str(url).startswith("http://"): url = url[7:]
        elif str(url).startswith("https://"): url = url[8:]

        if str(url).startswith("www."): url = url[4:]
        sy_gov_sites.append(url)

# f = open("jsonFiles/eduSites.json", "w")
# f.write(json.dumps(sy_edu_sites, indent=4))
# f.close()
# f = open("jsonFiles/govSites.json", "w")
# f.write(json.dumps(sy_gov_sites, indent=4, sort_keys=True))
# f.close()