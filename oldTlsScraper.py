# import socket
# #import ssl
# from OpenSSL import SSL
# import OpenSSL
#import sslyze

# def scrape_certs(site_info):
    #     try:
    #         server_tester = ServerConnectivityTester(
    #             hostname='smtp.gmail.com',
    #             port=587,
    #             tls_wrapped_protocol=TlsWrappedProtocolEnum.STARTTLS_SMTP
    #         )
    #         print(f'\nTesting connectivity with {server_tester.hostname}:{server_tester.port}...')
    #         server_info = server_tester.perform()
    #     except ServerConnectivityError as e:
    #         # Could not establish an SSL connection to the server
    #         raise RuntimeError(f'Could not connect to {e.server_info.hostname}: {e.error_message}')
    #
    # command = Tlsv10ScanCommand()
    #
    # synchronous_scanner = SynchronousScanner()
    #
    # scan_result = synchronous_scanner.run_scan_command(server_info, command)
    # for cipher in scan_result.accepted_cipher_list:
    #     print(f'    {cipher.name}')

    #print( Scanner.get_enabled_versions(site_info["name"]))
    # try:
    #     context = SSL.SSLContext()
    #     context = OpenSSL.SSL.SSLContext()
    #     context.maximum_version = ssl.TLSVersion.SSLv3
    #
    #     cert = ssl.get_server_certificate((site_info["name"], 443))
    #     x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    #    # site_info.alg = str(x509.get_signature_algorithm())
    #     print(str(x509.get_signature_algorithm()))
    #     with socket.create_connection((site_info["name"], 443)) as sock:
    #         with context.wrap_socket(sock, server_hostname=site_info["name"]) as ssock:
    #             #site_info.tls = str(ssock.version())
    #             print(str(ssock.version()))
    # except ssl.SSLError as err:
    #    print(err)
###Test
# site={"id":101,"rank":"972969","name":"syriatimes.sy"}
# scrape_certs(site)
    #check for specific ssl versions instead
    # try:
    #
    #     context = ssl.SSLContext()
    #     cert = ssl.get_server_certificate((site_info.name, 443))
    #
    #     x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    #     site_info.alg = str(x509.get_signature_algorithm())
    #
    #
    #     with socket.create_connection((site_info.name, 443)) as sock:
    #         with context.wrap_socket(sock, server_hostname=site_info.name) as ssock:
    #             site_info.tls = str(ssock.version())
    #
    # except ssl.SSLCertVerificationError as err:
    #     print("self signed")
