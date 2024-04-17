# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

#from flask import current_app as app
import msal
from services.secretservice import SecretService

class AadService:

    def get_access_token():
        '''Generates and returns Access token

        Returns:
            string: Access token
        '''
        keyvault = "cgmmlservicevault"
        client_id = SecretService.get_secret_byname(keyvault,"pbieclientid") 
        client_secret = SecretService.get_secret_byname(keyvault,"pbieclientsecret") 
        authority_url = SecretService.get_secret_byname(keyvault,"entraauthority")
        scope_base = [SecretService.get_secret_byname(keyvault,"pbiscope")]
        tenant_id = SecretService.get_secret_byname(keyvault,"entratenant")
        

        response = None
        try:
            authority = authority_url.replace('organizations', tenant_id)
            clientapp = msal.ConfidentialClientApplication(client_id, client_credential=client_secret, authority=authority)

            # Make a client call if Access token is not available in cache
            response = clientapp.acquire_token_for_client(scopes=scope_base)

            try:
                return response['access_token']
            except KeyError:
                raise Exception(response['error_description'])

        except Exception as ex:
            raise Exception('Error retrieving Access token\n' + str(ex))