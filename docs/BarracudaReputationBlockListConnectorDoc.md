## About the connector
Barracuda Reputation System is a real-time database of IP addresses that have a poor reputation for sending valid emails. Barracuda Central maintains and manually verifies all IP addresses marked as "poor" on the Barracuda Reputation System.
<p>This document provides information about the Barracuda Reputation Block List Connector, which facilitates automated interactions, with a Barracuda Reputation Block List server using FortiSOAR&trade; playbooks. Add the Barracuda Reputation Block List Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Barracuda Reputation Block List.</p>
### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-barracuda-reputation-block-list`

## Prerequisites to configuring the connector
- You must have the URL of Barracuda Reputation Block List server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Barracuda Reputation Block List server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Barracuda Reputation Block List</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>DNS Server IP Address<br></td><td>Specify the DNS Server IP Address<br>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get IP Reputation<br></td><td>Uploads a IP to Barracuda Reputation System and retrieves the analysis results.<br></td><td>get_ip_reputation <br/>Investigation<br></td></tr>
</tbody></table>
### operation: Get IP Reputation
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Lookup IPv4 Or IPv6<br></td><td>Specify the IP for which you want to retrieve the reputation information.<br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Address": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "Malicious": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - barracuda-reputation-block-list - 1.0.0` playbook collection comes bundled with the Barracuda Reputation Block List connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Barracuda Reputation Block List connector.

- Get IP Reputation

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
