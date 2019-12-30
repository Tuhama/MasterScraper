import re


def scrapeframes(soup, site_info):

    #all_frames = soup.find_all('iframe'),{"src": re.compile('^http:')}
    all_frames = soup.find_all('iframe')
    sandboxed_frames = soup.find_all('iframe',{"sandbox": True})

    if len(all_frames) == len(sandboxed_frames):
        site_info.sandboxedframes = True

    for iframe in sandboxed_frames:
        print(site_info.name)
        print("sandbox:" + str(iframe["sandbox"]))

    site_info.secureframing = test_secure_framing(site_info)


def test_secure_framing(site_info):
    frame_ancestors = 1 if "frame_ancestors" in site_info.cspMeta or "frame_ancestors" in site_info.cspHeader else None
    if frame_ancestors or site_info.xframe:
        return True
    else:
        return False



