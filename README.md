# auth0-saml-cert-exp

Script to retrieve SAML signing certificate expiry date from an Auth0 connection

### Usage

```
python cert-exp.py -d {AUTH0_DOMAIN} -c {CONNECTION_ID} -k {APIv2_KEY}
```

For instance:

```
python cert-exp.py -d fadydev.auth0.com -c con_Xme9dQjsUsVvYnXJ -k ...
```

### Resources

- [Instructions to get an APIv2 token](https://auth0.com/docs/api/management/v2/tokens)
- [APIv2 endpoint to list all your connections and retrieve connection ID](https://auth0.com/docs/api/management/v2#!/Connections/get_connections)

### Requirements

- OpenSSL
- Tested on Python 2.7+ or 3.5+

**Note:** macOS comes pre-installed with Python 2.7 and OpenSSL
