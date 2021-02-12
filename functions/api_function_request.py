import lastpass
import io
import requests
import numpy as np 
import pandas as pd 

"""
Using lastpass to fetch secrets and connect to an API.
"""
class ApiRequest():
    def keys_invault(self,user,secret):
        vault = lastpass.Vault.open_remote(username=user,password=secret)
        for i in vault.accounts:
            print(i.name)
            if i.name == 'fixer.io':
                return i.url,i.password

