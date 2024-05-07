# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

#from flask import current_app as app
import msal
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class SecretService:

    def store_secret_byname(keyVaultName, secretName, secretValue):
        '''Stashes a provided secret in keyvault

        Returns:
            Nothing
        ''' 
        response = None
        KVUri = f"https://{keyVaultName}.vault.azure.net"
        
        try:
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=KVUri, credential=credential)
            
            response = client.set_secret(name=secretName, value=secretValue)
            
            return response
        except Exception as ex:
            raise Exception('Error storing secret to keyvault\n' + str(ex))

    def get_secret_byname(keyVaultName,secret):
        '''Retreives a key from keyvault

        Returns:
            string: retreived key
        '''      
        response = None
        KVUri = f"https://{keyVaultName}.vault.azure.net"

        try:
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=KVUri, credential=credential)

            #fetch secrets from keyvault
            secretvalue = client.get_secret(secret).value

            return secretvalue
        except Exception as ex:
            raise Exception('Error retrieving key from keyvalut token\n' + str(ex))



            