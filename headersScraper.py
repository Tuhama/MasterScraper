def has_http_only(temp_cookie):
    extra_args = temp_cookie.__dict__.get('_rest')
    if extra_args:
        for key in extra_args.keys():
            if key.lower() == 'httponly':
                return extra_args.get(key)
    return None


def has_samesite(temp_cookie):
    extra_args = temp_cookie.__dict__.get('_rest')
    if extra_args:
        for key in extra_args.keys():
            if key.lower() == 'samesite':
                return extra_args.get(key)
    return None


def scrape_headers(soup,response,site_info):
    _cookies = []
    # first check for https
    if response.url.startswith("https"):
        site_info.redirected = True

    site_info.hsts = response.headers.get('strict-transport-security')

    site_info.pkp = response.headers.get('Public-Key-Pins')

    site_info.xss = response.headers.get('x-xss-protection')

    site_info.xcontent = response.headers.get('x-content-type-options')

    site_info.xframe = response.headers.get('X-Frame-Options')

    site_info.server = response.headers.get('server')
    site_info.poweredBy = response.headers.get('X-Powered-By')

    if not response.cookies:
        site_info.cookies = []

    else:
        for cookie in response.cookies:
            _cookie = {"name": cookie.name, "secure": cookie.secure, "httponly": has_http_only(cookie),
                       "samesite": has_samesite(cookie)}
            _cookies.append(_cookie)
        site_info.cookies = _cookies
