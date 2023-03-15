""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import get_logger, ConnectorError
import dns.resolver
from ipaddress import ip_address, IPv4Address

logger = get_logger('baracuddaRBL')


def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        raise ConnectorError("Invalid Input")


def get_ip_reputation(config, params):
    ip = params.get('iplookup')
    dnsServerIP = config.get('dnsServerIP')
    try:
        if validIPAddress(ip) != 'Invalid':
            resolver = dns.resolver
            resolver.Resolver(configure=False)
            resolver.nameservers = [dnsServerIP]
            reversePTR = ip_address(ip).reverse_pointer
            if validIPAddress(ip) == 'IPv4':
                dnsName = reversePTR.replace("in-addr.arpa", "b.barracudacentral.org")
            else:
                dnsName = reversePTR.replace("ip6.arpa", "b.barracudacentral.org")

            result = resolver.resolve(dnsName, 'A')

            if result.rrset[0].to_text() == '127.0.0.2':
                data = {'Address': ip,
                        'Malicious': True}
                return data
            else:
                data = {'Address': ip,
                        'Malicious': False}
                return data
        else:
            raise ConnectorError("Invalid Input")

    except Exception as e:
        raise ConnectorError(e)


def check_health(config):
    logger.info("health check started")
    dnsServerIP = config.get('dnsServerIP')
    resolver = dns.resolver
    resolver.Resolver(configure=False)
    resolver.nameservers = [dnsServerIP]
    result = resolver.resolve('2.0.0.127.b.barracudacentral.org', 'A')
    test = result.rrset[0].to_text()
    if result.rrset[0].to_text() == '127.0.0.2':
        return True
    else:
        return False


operations = {
    'get_ip_reputation': get_ip_reputation
}
