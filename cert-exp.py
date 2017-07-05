import argparse
import json
import uuid
import subprocess
import base64
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument('-c', help='Connection ID')
parser.add_argument('-d', help='Auth0 Domain (e.g.: fadydev.auth0.com)')
parser.add_argument('-k', help='Auth0 APIv2 Key')
args = parser.parse_args()

conn_endpoint = 'https://{}/api/v2/connections/{}'.format(args.d, args.c)

try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2

req = Request(conn_endpoint)
req.add_header('Authorization', 'Bearer {}'.format(args.k))
res = urlopen(req).read()

conn_details = json.loads(res.decode('utf-8'))
cert = '{}'.format(base64.b64decode(conn_details['options']['signingCert']).decode('ascii'))

temp_cert_file = '{}.pem'.format(uuid.uuid4())
with open(temp_cert_file, 'w+') as f:
    f.write(cert)

output = subprocess.check_output(
    'openssl x509 -inform pem -in {} -noout -text'.format(temp_cert_file),
    shell=True
)

match = re.search('Not After : (.*)', output.decode('ascii'))

print('The signing certificate expires at: {}'.format(match.group(1)))

os.remove(temp_cert_file)
