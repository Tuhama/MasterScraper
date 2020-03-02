import re


def scrapeframes(soup, site_info):

    #all_external_frames = soup.find_all('iframe'),{"src": re.compile('^http')}
    all_frames = soup.find_all('iframe', {'src': re.compile('^http')})
    print(len(all_frames))
    print(all_frames)
    sandboxed_frames = soup.find_all('iframe',{'sandbox': True})
    print(len(sandboxed_frames))
    print(sandboxed_frames)
    if len(all_frames) != 0 and len(all_frames) == len(sandboxed_frames):
        site_info.sandboxedframes = True
    elif len(all_frames) != 0 and len(all_frames) != len(sandboxed_frames):
        site_info.sandboxedframes = False

    for iframe in sandboxed_frames:
        print(site_info.name)
        print("sandbox:" + str(iframe["sandbox"]))

    site_info.secureframing = test_secure_framing(site_info)


def test_secure_framing(site_info):
    frame_ancestors = None
    if site_info.cspMeta and "frame_ancestors" in site_info.cspMeta:
        frame_ancestors = True
    elif site_info.cspHeader and "frame_ancestors" in site_info.cspHeader:
        frame_ancestors = True

    if frame_ancestors or site_info.xframe:
        return True
    else:
        return False



