import json
import pandas


def calculateScore():
    with open('jsonFiles/syrianSitesSecurityInfo.json', 'r') as f:
        sites = json.load(f)
    sites_with_score = []
    for site in sites:
        positive_score = 0
        negative_score = 0

        # secure comm.
        https = 1 if site["https"] else 0
        hsts = 1 if site["hsts"] else 0
        secure = 0
        for cookie in site["cookies"]:
            if cookie["secure"]:
                secure = 1
                break
        pkp = 1 if site["pkp"] else 0

        communication_score = 40 / 100 * https + 25 / 100 * hsts + 25 / 100 * secure + 10 / 100

        # xss mitigation
        csp = 1 if site["cspMeta"] or site["cspHeader"] or site["xcspHeader"] else 0
        httponly = 0
        for cookie in site["cookies"]:
            if cookie["httponly"]:
                httponly = 1
                break
        samesite = 0
        for cookie in site["cookies"]:
            if cookie["samesite"]:
                samesite = 1
                break
        xcto = 1 if site["xcontent"] else 0
        sri = 1 if site["sri"] else 0
        sandbox = 1 if site["sandboxedframes"] else 0
        xss_score = 30 / 100 * csp + 20 / 100 * httponly + 20 / 100 * samesite + 10 / 100 * xcto + 10 / 100 * sandbox + 10 / 100 * sri

        # secur Framing
        xframe = 1 if site["xframe"] else 0
        frame_ancestors = 1 if "frame_ancestors" in str(site["cspMeta"]) or "frame_ancestors" in str(
            site["cspHeader"]) else 0

        secure_framing_score = 50 / 100 * xframe + 50 / 100 * frame_ancestors

        positive_score = 40 / 100 * communication_score + 40 / 100 * xss_score + 20 / 100 * secure_framing_score


        ############################################################

        # Vulnerable remote JavaScript inclusion
        if site["externaljs"]:
            negative_score += 67.50

        # X-XSS-Protection
        if site["xss"]:
            negative_score += 28.33

        # Insecure SSL implementation
        if not site["https"] or not site["cert_trusted"]:
            negative_score += 18.10
        elif not site["redirected"]:
            negative_score += 18.10

        if site["sslv2"] or site["sslv3"] or site["tlsv1"] or site["tlsv11"]:
            negative_score += 18.10

        # Mixed-content inclusions
        if site["mixedcontent"]:
            negative_score += 13.420

        # outdated server software
        if site["server"]:
            sever_name = site["server"].lower()
            if "iis/" in sever_name:
                _version = sever_name[sever_name.find("iis/") + 4:sever_name.find("iis/") + 8]
                # the version of iis is a sign of the used server version
                # >>> iis/7.5 is used in windows7 and Windows Server 2008 R2 wich is no longer supported by microsoft starting 2020
                if "1.0" in _version or "2.0" in _version or "3.0" in _version or "4.0" in _version or "5.0" in _version or "5.1" in _version or "6.0" in _version or "7.0" in _version or "7.5" in _version:
                    negative_score += 8.71
            elif "nginx/" in sever_name:
                _version = sever_name[sever_name.find("nginx/") + 6:sever_name.find("nginx/") + 10]
                if not ("1.17" in _version or "1.16" in _version):
                    negative_score += 8.71
            elif "apache/" in sever_name:
                _version = sever_name[sever_name.find("apache/") + 7:sever_name.find("apache/") + 11]
                if not("2.4." in _version):
                    negative_score += 8.71

        site["p_score"] = positive_score
        site["n_score"] = negative_score
        sites_with_score.append(site)

    f = open("SyrianSitesInfo.json", "w")
    f.write(json.dumps(sites_with_score))
    f.close()

    pandas.read_json("SyrianSitesInfo.json").to_excel("SyrianSitesInfo.xlsx")


def outdated_software():
    with open('jsonFiles/syrianSitesSecurityInfo.json', 'r') as f:
        sites = json.load(f)
    sites_with_score = []
    counter = 0
    for site in sites:
        # outdated server software
        if site["server"]:
            sever_name = site["server"].lower()
            if "iis/" in sever_name:
                _version = sever_name[sever_name.find("iis/") + 4:sever_name.find("iis/") + 8]
                # the version of iis is a sign of the used server version
                # >>> iis/7.5 is used in windows7 and Windows Server 2008 R2 wich is no longer supported by microsoft starting 2020
                if "1.0" in _version or "2.0" in _version or "3.0" in _version or "4.0" in _version or "5.0" in _version or "5.1" in _version or "6.0" in _version or "7.0" in _version or "7.5" in _version:
                    counter += 1
            elif "nginx/" in sever_name:
                _version = sever_name[sever_name.find("nginx/") + 6:sever_name.find("nginx/") + 10]
                if not ("1.17" in _version or "1.16" in _version):
                    counter += 1
            elif "apache/" in sever_name:
                _version = sever_name[sever_name.find("apache/") + 7:sever_name.find("apache/") + 11]
                if not("2.4." in _version):
                    counter += 1
    return counter


if __name__ == '__main__':
 calculateScore()
