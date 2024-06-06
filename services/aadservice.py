# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

#from flask import current_app as app
import msal
from services.secretservice import SecretService
import azure.identity as aid
from services.env import const

class AadService:

    def get_access_token(scope=None):
        '''Generates and returns Access token

        Returns:
            string: Access token
        '''
        keyvault = const.keyVault
        
        if scope is not None:
            scopeBase = [scope]
        else:
            #scope_base = [SecretService.get_secret_byname(keyvault,"pbiscope")]
            scopeBase = [const.pbiScope]

        clientId = const.pbiClientId
        authorityUrl = const.entraAuthority
        tenantId = const.entraTenant
        clientSecret = SecretService.get_secret_byname(keyvault,"pbieclientsecret") 
        
        response = None
        try:
            authority = authorityUrl.replace('organizations', tenantId)
            clientapp = msal.ConfidentialClientApplication(clientId, client_credential=clientSecret, authority=authority)
            
            # Make a client call if Access token is not available in cache
            response = clientapp.acquire_token_for_client(scopes=scopeBase)

            try:
                return response['access_token']
            except KeyError:
                raise Exception(response['error_description'])

        except Exception as ex:
            raise Exception('Error retrieving Access token\n' + str(ex))


    def get_credential():
            '''Generates and returns a credentail object
            #https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.clientsecretcredential?view=azure-python

            Returns:
                string: Access token
            '''
            keyvault = const.keyVault
            
            clientId = const.pbiClientId
            authorityUrl = const.entraAuthority
            tenantId = const.entraTenant
            clientSecret = SecretService.get_secret_byname(keyvault,"pbieclientsecret") 

            response = None
            try:
                credential = aid.ClientSecretCredential(tenantId, clientId, clientSecret)
                
                try:
                    return credential
                except KeyError:
                    raise Exception(response['error_description'])

            except Exception as ex:
                raise Exception('Error retrieving Access token\n' + str(ex))

    def get_tenant_credential(tenantName):
            '''Generates and returns a credentail object
            #https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.clientsecretcredential?view=azure-python

            Returns:
                string: Access token
            '''
            keyvault = const.keyVault
            tenantAppKey = tenantName+"Id"
            tenantSecretKey = tenantName+"Secret"
            
            authorityUrl = const.entraAuthority
            tenantId = const.entraTenant
            clientId = SecretService.get_secret_byname(keyvault,tenantAppKey) 
            clientSecret = SecretService.get_secret_byname(keyvault,tenantSecretKey)
            

            response = None
            try:
                credential = aid.ClientSecretCredential(tenantId, clientId, clientSecret)
                
                try:
                    return credential
                except KeyError:
                    raise Exception(response['error_description'])

            except Exception as ex:
                raise Exception('Error retrieving Access token\n' + str(ex))                            