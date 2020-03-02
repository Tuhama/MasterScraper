import re


def scrape_files(soup, site_info):
    scripts = soup.find_all('script', {"src": True})
    unsafe_scripts = soup.find_all('script', {"src": re.compile('^http:')})

    external_scripts = []

    for script in scripts:
        if script["src"]:
            extra_args = script.__dict__.get('_rest')
            if extra_args:
                for key in extra_args.keys():
                    if key.lower() == "integrity":
                        site_info.sri = True
                    else:
                        if str(script["src"]).startswith("http") and site_info.name not in script["src"]:
                            external_scripts.append(script)
            else:
                if str(script["src"]).startswith("http") and site_info.name not in script["src"]:
                    external_scripts.append(script)

    if len(external_scripts) > 0:
            site_info.externaljs = True

    if len(unsafe_scripts)> 0 and site_info.https:
        site_info.mixedcontent = True
        #for comparing degrees equality
    if not site_info.https:
        site_info.mixedcontent = True

    #site_info.externaljs = len(external_scripts)

    #site_info.mixedcontent = len(unsafe_scripts)

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
