import requests
from requests.auth import HTTPBasicAuth
from scheduler.app.libs.omnidesk_new.omnidesk_core.endpoints import ENDPOINTS


class OmnideskAPI:
    def __init__(self, sub_domain, domain, email, api_key):
        self.host = 'https://' + sub_domain + '.' + domain
        self.auth = HTTPBasicAuth(email, api_key)

    def send_request(self, method, endpoint, **params):
        if method == 'get':
            result = requests.get(self.host + ENDPOINTS[endpoint], params=params, auth=self.auth).text
        elif method == 'post':
            result = requests.post(self.host + ENDPOINTS[endpoint], params=params, auth=self.auth).text
        else:
            result = ''
        return result
