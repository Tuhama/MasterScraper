def scrape_csp(soup,response,site_info):
    site_info.cspMeta = soup.find_all('meta', {'http-equiv': 'Content-Security-Policy'})
    # request headers dictionary is case insensitive
    site_info.cspHeader = response.headers.get('Content-Security-Policy')
    site_info.xcspHeader = response.headers.get('X-Content-Security-Policy')
    site_info.reportcspHeader = response.headers.get('Content-Security-Policy-Report-Only')

