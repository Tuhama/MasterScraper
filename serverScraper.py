import socket
import ssl
import OpenSSL
import json

hostname = 'www.yahoo.com'

# with open('syrianSites.json', 'r') as f:
#     sites = json.load(f)

sites = [
    {'id': 2, 'rank': '34039', 'name': 'www.sana.sy'}, {'id': 4, 'rank': '61098', 'name': 'www.job.sy'}, {'id': 22, 'rank': '161298', 'name': 'www.best-assistance.net'}, {'id': 27, 'rank': '198247'
    , 'name': 'www.takamol.sy'}, {'id': 34, 'rank': '230908', 'name': 'www.samanet.sy'},
         {'id': 41, 'rank': '284351', 'name': 'mts.sy'}, #removed www. because of certificate host mismach error
         {'id': 49, 'rank': '333922', 'name': 'www.alepuniv.edu.sy'},
        {'id': 64, 'rank': '496155', 'name': 'www.hpu.sy'}]

for site in sites:
    if site['id'] != 10 and site['id'] != 17 and site['id'] != 32:
        print(str(site['id']) + " " + site['name'] + ": ")
        context = ssl.create_default_context()

        cert = ssl.get_server_certificate((site['name'], 443))

        with socket.create_connection((site['name'], 443)) as sock:
            with context.wrap_socket(sock, server_hostname=site['name']) as ssock:
                print(ssock.version())

        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        x509.get_signature_algorithm()
        print(x509.get_signature_algorithm())



