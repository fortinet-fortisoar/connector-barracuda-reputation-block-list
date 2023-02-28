from connectors.core.connector import get_logger, ConnectorError
from socket import gaierror
import socket

logger = get_logger('baracuddaRBL')
def IP_Domain_rbllookup(config, params):
    ip = params.get('iplookup')
    reverseip = str(ip).split('.')
    address = reverseip[3] + '.' + reverseip[2] + '.' + reverseip[1] + '.' + reverseip[0] + '.b.barracudacentral.org'
    try:
        result = socket.gethostbyname(address)
        if result == '127.0.0.2':
            data = {'Address': address,
                    'Malicious': {'Vendor': 'Barracuda',
                                  'Description': 'IP was found to be on the Barracuda(BRBL) block list'}}
            return data
        else:
            data = {'Address': address,
                    'NotMalicious': {'Vendor': 'Barracuda',
                                  'Description': 'IP was NOT found to be on the Barracuda(BRBL) block list'}}  
            return data        
    except gaierror:
        data = {'Address': address}
    except Exception as e:
        return (f'Error from Barracuda - {str(e)}.')

def _check_health(config):
    logger.info("health check started")
    return True

operations = {
    'IP_Domain_rbllookup': IP_Domain_rbllookup
}
