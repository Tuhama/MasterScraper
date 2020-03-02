class SiteInfo:
    def __init__(self, name, site_type, sit_id
                 # tls, redirected, alg, hsts, pkp,
                 # xss, xcontent, xframe, cookies,
                 # cspMeta, cspHeader, xcspHeader, reportcspHeader,
                 # secureframing,sandboxedframes,csrf_token,
                 # mixedcontent, externaljs, server, poweredBy
                 ):
        self.name = name
        self.site_type = site_type
        self.sit_id = sit_id
        self.broken = False
        self.https = None
        self.redirected = None
        self.cert_trusted = None
        self.sslv2 = None
        self.sslv3 = None
        self.tlsv1 = None
        self.tlsv11 = None
        self.tlsv12 = None
        self.tlsv13 = None
        self.heartbleed = None
        # self.tls = None
        # self.alg = None
        self.hsts = None
        self.pkp = None
        self.xss = None
        self.xcontent = None
        self.xframe = None
        self.cookies = []
        self.secure_used = None
        self.samesite_used = None
        self.httponly_used = None
        self.cspMeta = None
        self.cspHeader = None
        self.xcspHeader = None
        self.reportcspHeader = None
        self.secureframing = None
        self.sandboxedframes = None
        self.csrf_token = None
        self.sri = None
        self.mixedcontent = None
        self.externaljs = None
        self.server = None
        self.poweredBy = None

    def __str__(self):
        return str(self.__dict__)
