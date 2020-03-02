from sslyze.server_connectivity_tester import ServerConnectivityTester
from sslyze.server_connectivity_tester import ServerConnectivityError
from sslyze.plugins.openssl_cipher_suites_plugin import Sslv20ScanCommand, Sslv30ScanCommand, \
    Tlsv12ScanCommand, Tlsv10ScanCommand, Tlsv11ScanCommand, Tlsv13ScanCommand
from nassl._nassl import WantReadError
from sslyze.plugins.certificate_info_plugin import CertificateInfoPlugin, CertificateInfoScanCommand
from sslyze.synchronous_scanner import SynchronousScanner
from sslyze.plugins.heartbleed_plugin import HeartbleedPlugin, HeartbleedScanCommand
from sslyze.concurrent_scanner import ConcurrentScanner
from sslyze.concurrent_scanner import PluginRaisedExceptionScanResult
from sslyze.ssl_settings import TlsWrappedProtocolEnum
from cryptography.x509.oid import NameOID
import pytest
from sslyze.plugins.utils.certificate_utils import CertificateUtils
from SiteInfo import SiteInfo


def server_connectivity_tester(_hostname):
    try:
        server_tester = ServerConnectivityTester(
            hostname=_hostname,
        )
        print(f'\nTesting connectivity with {server_tester.hostname}:{server_tester.port}...')
        server_info = server_tester.perform(10)
        return server_info
    except ServerConnectivityError as e:
        # Could not establish an SSL connection to the server
        print(f'Could not connect to {e.server_info.hostname}: {e.error_message}')


def concurrent_scan(site_info):
    # Setup the server to scan and ensure it is online/reachable
    server_info = server_connectivity_tester(site_info.name)

    if server_info:
        synchronous_scanner = SynchronousScanner()

        cert_info_plugin = CertificateInfoPlugin()
        plugin_result = cert_info_plugin.process_task(server_info, CertificateInfoScanCommand())
#not plugin_result.verified_certificate_chain or
        #not plugin_result.leaf_certificate_subject_matches_hostname some sites' certs CN is with "www." so the result here is false
        if plugin_result.verified_certificate_chain and site_info.name not in str(plugin_result.verified_certificate_chain[0].subject):
            site_info.cert_trusted = "False"
            print("not trusted: " + site_info.name)
            print(plugin_result.__dict__)
        # elif not plugin_result.verified_certificate_chain:
        #     site_info.cert_trusted = "False"
        #     print("not trusted: " + site_info.name)
        #     print(plugin_result.__dict__)
        else:
            site_info.cert_trusted = "True"
            scan_result1 = synchronous_scanner.run_scan_command(server_info, Sslv20ScanCommand())
            if len(scan_result1.accepted_cipher_list) > 0:
                site_info.sslv2 = "True"
            scan_result2 = synchronous_scanner.run_scan_command(server_info, Sslv30ScanCommand())
            if len(scan_result2.accepted_cipher_list) > 0:
                site_info.sslv3 = "True"
            scan_result3 = synchronous_scanner.run_scan_command(server_info, Tlsv10ScanCommand())
            if len(scan_result3.accepted_cipher_list) > 0:
                site_info.tlsv1 = "True"
            scan_result4 = synchronous_scanner.run_scan_command(server_info, Tlsv11ScanCommand())
            if len(scan_result4.accepted_cipher_list) > 0:
                site_info.tlsv11 = "True"
            scan_result5 = synchronous_scanner.run_scan_command(server_info, Tlsv12ScanCommand())
            if len(scan_result5.accepted_cipher_list) > 0:
                site_info.tlsv12 = "True"
            scan_result6 = synchronous_scanner.run_scan_command(server_info, Tlsv13ScanCommand())
            if len(scan_result6.accepted_cipher_list) > 0:
                site_info.tlsv13 = "True"

            recheck_cert(site_info)


#a lot of sites have invalid certificate for alot of reasons which we wan't cover here
def recheck_cert(site_info):
    if not (site_info.sslv2 or site_info.sslv3 or site_info.tlsv1 or site_info.tlsv11 or site_info.tlsv12 or site_info.tlsv13):
        print("noooooo")
    # else:
    #     site_info.https = True


if __name__ == '__main__':
    _site_info = SiteInfo("hiast.edu.sy", "gov", 0)
    concurrent_scan(_site_info)
    print(_site_info)


    #
    # plugin = HeartbleedPlugin()
    # plugin_result = plugin.process_task(server_info, HeartbleedScanCommand())
    # site_info.heartbleed = plugin_result.is_vulnerable_to_heartbleed

    # scan_result7 = synchronous_scanner.run_scan_command(server_info, HeartbleedScanCommand())
    # site_info.heartbleed = scan_result7.is_vulnerable_to_heartbleed
    # concurrent_scanner.queue_scan_command(server_info, CertificateInfoScanCommand())

    # Process the results
    # print('\nProcessing results...')
    # for scan_result in synchronous_scanner.get_results():
    #     # All scan results have the corresponding scan_command and server_info as an attribute
    #     # print(f'\nReceived result for "{scan_result.scan_command.get_title()}" '
    #     #       f'on {scan_result.server_info.hostname}')
    #
    #     # A scan command can fail (as a bug); it is returned as a PluginRaisedExceptionResult
    #     if isinstance(scan_result, PluginRaisedExceptionScanResult):
    #         print(f'Scan command failed: {scan_result.scan_command.get_title()}')
    #         # raise RuntimeError(f'Scan command failed: {scan_result.scan_command.get_title()}')
    #     else:
    #         # Each scan result has attributes with the information yo're looking for
    #         # All these attributes are documented within each scan command's module
    #         # print("here")
    #         # if isinstance(scan_result.scan_command, Sslv20ScanCommand):
    #         #     if len(scan_result.accepted_cipher_list) > 0:
    #         # #         site_info.sslv2 = True
    #         # if isinstance(scan_result.scan_command, Sslv30ScanCommand):
    #         #     if len(scan_result.accepted_cipher_list) > 0:
    #         #         site_info.sslv3 = True
    #         # if isinstance(scan_result.scan_command, Tlsv10ScanCommand):
    #         #     if len(scan_result.accepted_cipher_list) > 0:
    #         #         site_info.tlsv1 = True
    #         # if isinstance(scan_result.scan_command, Tlsv11ScanCommand):
    #         #     if len(scan_result.accepted_cipher_list) > 0:
    #         #         site_info.tlsv11 = True
    #         # if isinstance(scan_result.scan_command, Tlsv12ScanCommand):
    #         #     if len(scan_result.accepted_cipher_list) > 0:
    #         #         site_info.tlsv12 = True
    #         if isinstance(scan_result.scan_command, Tlsv13ScanCommand):
    #             if len(scan_result.accepted_cipher_list) > 0:
    #                 site_info.tlsv3 = True
    #         if isinstance(scan_result.scan_command, HeartbleedScanCommand):
    #             site_info.heartbleed = scan_result.is_vulnerable_to_heartbleed

# except Exception as e:
# template = "An exception of type {0} occurred. Arguments:\n{1!r}"
# message = template.format(type(e).__name__, e.args)
# print(message)