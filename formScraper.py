def scrape_tokens(soup,site_info):
    headen_input = soup.find_all('input', type="hidden")
    for h_input in headen_input:
        if not h_input.text:
            if "name" in h_input:
                if "token" in h_input["name"] or "csrf" in h_input["name"] or "nonce" in  h_input["name"]:
                    site_info.csrf_token = True
                print("Token" + str(h_input["name"]))




