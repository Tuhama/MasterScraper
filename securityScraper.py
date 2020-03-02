import requests
import json
import urllib3
from bs4 import BeautifulSoup

from tlsScraper import concurrent_scan
from jsScraper import scrape_files
from framScraper import scrapeframes
from formScraper import scrape_tokens
from cspScraper import scrape_csp
from headersScraper import scrape_headers
import scoreCalculator
from SiteInfo import SiteInfo

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
response = 0
soup = 0

if __name__ == '__main__':
    with open('jsonFiles/finalSites.json', 'r') as f:
        all_sites_names = json.load(f)
    #all_sites_names = {"takamol.sy"}
    sites_info = []
    secure_sites = []
    unsecure_sites = []
    i = 0
    for site_name in all_sites_names:
        site_type = None
        if ".edu" in site_name:
            site_type = "edu"
        elif ".gov" in site_name:
            site_type = "gov"
        i = i+1
        _site_info = SiteInfo(site_name, site_type, i)
        sites_info.append(_site_info)
        try:
            response = requests.get('https://' + site_name, verify=False, timeout=(10, 10),
                                    headers={'User-Agent': user_agent})
            _site_info.https = True
            secure_sites.append(site_name)

        except requests.exceptions.HTTPError as errh:
            unsecure_sites.append(site_name)
        except requests.exceptions.SSLError as errssl:
            unsecure_sites.append(site_name)
        except requests.exceptions.Timeout as errt:
            unsecure_sites.append(site_name)
        except requests.exceptions.ConnectionError as errc:
            unsecure_sites.append(site_name)

    sites_info_string = []
    for _site_info in sites_info:

        try:
           # print(site)
            response = requests.get('http://' + _site_info.name, verify=False, timeout=(30, 30),
                                    headers={'User-Agent': user_agent})
            soup = BeautifulSoup(response.text, 'html.parser')

            scrape_headers(soup,response,_site_info)
            scrape_csp(soup,response,_site_info)
            scrape_files(soup, _site_info)
            scrapeframes(soup, _site_info)
            scrape_tokens(soup, _site_info)

            if _site_info.name in secure_sites:
                if _site_info.name not in {"iust.edu.sy"}:
                    concurrent_scan(_site_info)
                #print(site)
        except requests.exceptions.RequestException as err:
            _site_info.broken = True
            print(err)
        #
        sites_info_string.append(_site_info.__dict__)

    f = open("jsonFiles/SyrianSitesSecurityInfo.json", "w")
    f.write(json.dumps(sites_info_string, indent=4))
    f.close()

    scoreCalculator.calculateScore()


