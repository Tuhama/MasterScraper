import json
import pandas

with open('syrianSitesSecurityInfo.json', 'r') as f:
    sites = json.load(f)
sites_with_score = []
for site in sites:
    positive_score = 0
    negative_score = 0

#secure comm.
    https = 1 if site["https"] else 0
    hsts = 1 if site["hsts"] else 0
    secure = 0
    for cookie in site["cookies"]:
        if cookie["secure"]:
            secure = 1
            break
    pkp = 1 if site["pkp"] else 0

    communication_score = 40/100 * https + 25/100 * hsts + 25/100 * secure + 10/100

#xss mitigation
    csp = 1 if site["cspMeta"] or site["cspHeader"] or site["xcspHeader"] else 0
    httponly=0
    for cookie in site["cookies"]:
        if cookie["httponly"]:
            httponly = 1
            break
    samesite=0
    for cookie in site["cookies"]:
        if cookie["samesite"]:
            samesite = 1
            break
    xcto = 1 if site["xcontent"] else 0
    sri = 1 if site["sri"] else 0
    sandbox = 1 if site["sandbox"] else 0
    xss_score = 30/100 * csp + 20/100 * httponly + 20/100 * samesite + 10/100 * xcto + 10/100 * sandbox + 10/100 * sri

    #secur Framing
    xframe = 1 if site["xframe"] else 0
    frame_ancestors = 1 if "frame_ancestors" in site["cspMeta"] or "frame_ancestors" in site["cspHeader"] else 0

    secure_framing_score = 50/100 * xframe+ 50/100 * frame_ancestors

    positive_score = 40/100 * communication_score + 40/100 * xss_score + 30/100 * secure_framing_score

    # if len(site["cookies"]) == 0:
    #     for cookie in site["cookies"]:
    #         #SameSite COOKIES
    #         if cookie["samesite"]:
    #             if cookie["samesite"].lower() != 'none':
    #                 positive_score += 32.40
    #         #SECURE COOKIES
    #         if cookie["secure"]:
    #             positive_score += 31.84
    #         #HTTPONLY COOKIES
    #         if cookie["httponly"]:
    #             positive_score += 28.21

    # #X-Content-Type-Options
    # if site["xcontent"]:
    #     positive_score += 8.02


############################################################

    #Vulnerable remote JavaScript inclusion
    if site["externaljs"]:
        negative_score += 67.50

    #X-XSS-Protection
    if site["xss"]:
        negative_score += 28.33

    #Insecure SSL implementation
    if site["tls"]:
        if site["tls"] != 'TLSv1.2' or site["tls"] != 'TLSv1.3':
            negative_score += 18.10
    else:
        negative_score += 18.10

    #Mixed-content inclusions
    if site["mixedcontent"]:
        negative_score += 13.420

    site["p_score"] = positive_score
    site["n_score"] = negative_score
    sites_with_score.append(site)

f = open("SyrianSitesInfo.json", "w")
f.write(json.dumps(sites_with_score))
f.close()


pandas.read_json("SyrianSitesInfo.json").to_excel("SyrianSitesInfo.xlsx")





