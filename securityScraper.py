import requests
import json
import urllib3

from bs4 import BeautifulSoup
#import certifi
# from tlsScraper import scrape_certs
from jsScraper import scrape_files
from framScraper import scrapeframes
from formScraper import scrape_tokens
from cspScraper import scrape_csp
from headersScraper import scrape_headers
from SiteInfo import SiteInfo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
response = 0
soup = 0


with open('jsonFiles/finalSites.json', 'r') as f:
    sites = json.load(f)

sites_info = []
secure_sites = []
unsecure_sites = []

for site in sites:
    try:
        print(site)
        response = requests.get('https://' + site, verify=False, timeout=(10, 10),
                                headers={'User-Agent': user_agent})
        secure_sites.append(site)

    except requests.exceptions.HTTPError as errh:
        unsecure_sites.append(site)
    except requests.exceptions.SSLError as errssl:
        unsecure_sites.append(site)
    except requests.exceptions.Timeout as errt:
        unsecure_sites.append(site)
    except requests.exceptions.ConnectionError as errc:
        unsecure_sites.append(site)

for site in sites:
    site_type = None
    if ".edu" in site:
        site_type = "edu"
    elif ".gov" in site:
        site_type = "gov"

    _site_info = SiteInfo(site,site_type)

    try:
        print(site)
        response = requests.get('http://' + site, verify=False, timeout=(30, 30),
                                headers={'User-Agent': user_agent})
        soup = BeautifulSoup(response.text, 'html.parser')

        scrape_headers(soup,response,_site_info)
        scrape_csp(soup,response,_site_info)
        scrape_files(soup, _site_info)
        scrapeframes(soup, _site_info)
        scrape_tokens(soup, _site_info)

        #if site in secure_sites:
            #scrape_certs(_site_info)
            #print(site)
    except requests.exceptions.RequestException as err:
        print(err)
    sites_info.append(_site_info.__dict__)

f = open("jsonFiles/SyrianSitesSecurityInfo.json", "w")
f.write(json.dumps(sites_info, indent=4))
f.close()




