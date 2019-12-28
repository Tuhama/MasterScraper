import re


def scrapeframes(soup, site_info):

    #all_frames = soup.find_all('iframe'),{"src": re.compile('^http:')}
    all_frames = soup.find_all('iframe')
    sandboxed_frames = soup.find_all('iframe',{"sandbox": True})

    if len(all_frames) == len(sandboxed_frames):
        site_info.sandboxedframes = True

    for iframe in sandboxed_frames:
        print(iframe["sandbox"])

def test_secure_framing(site_info):
    if "frame_ancestors" in site_info.csp or site_info.xframe:
        site_info.secureframing = True



