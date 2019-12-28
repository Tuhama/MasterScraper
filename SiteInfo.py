class SiteInfo:
    def __init__(self, name, rank,
                 # tls, redirected, alg, hsts, pkp,
                 # xss, xcontent, xframe, cookies,
                 # cspMeta, cspHeader, xcspHeader, reportcspHeader,
                 # secureframing,sandboxedframes,csrf_token,
                 # mixedcontent, externaljs, server, poweredBy
                 ):
        self.name = name
        self.rank = rank
        self.tls = None
        self.redirected = None
        self.alg = None
        self.hsts = None
        self.pkp = None
        self.xss = None
        self.xcontent = None
        self.xframe = None
        self.cookies = []
        self.cspMeta = None
        self.cspHeader = None
        self.xcspHeader = None
        self.reportcspHeader = None
        self.secureframing = None
        self.sandboxedframes = None
        self.csrf_token = None
        self.mixedcontent = None
        self.externaljs = None
        self.server = None
        self.poweredBy = None

    def __str__(self):
        return str(self.__dict__)