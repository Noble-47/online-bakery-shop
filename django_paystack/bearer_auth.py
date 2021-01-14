import requests

class BearerAuth(requests.auth.AuthBase):
    '''
    Extends requests module to allow
    authentication through brearer
    token as required by paystack
    '''
    def __init__(self, secret_key):
        # https://paystack.com/docs/api/#authentication
        self.secret_key = secret_key
    
    def __call__(self, r):
        r.headers["authorization"] = "Bearer" + " " + self.secret_key
        return r