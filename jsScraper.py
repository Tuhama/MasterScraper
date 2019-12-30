import re


def scrape_files(soup, site_info):
    scripts = soup.find_all('script', {"src": True})
    unsafe_scripts = soup.find_all('script', {"src": re.compile('^http:')})

    external_scripts = []

    for script in scripts:
        if script["src"]:
            if str(script["src"]).startswith("http") and site_info.name not in script["src"]:
                external_scripts.append(script)
                print(script["src"])

    site_info.externaljs = len(external_scripts)

    site_info.mixedcontent = len(unsafe_scripts)

    # links = soup.find_all('link', {"href": True})
    #
    # images = soup.find_all('img', {"src": True})
    #
    # print(len(scripts))
    # print(len(unsafe_scripts))

    # check for mixed content
    # check for external files
    # check for img src
    # {sitename,numberofscriptfiles,numberoflinks}
    # for script in scripts:
    #      print(script)
    #         print(safe_scripts.length)
    # text = script.find('src')
    # if text:
    #     print(str(text))
