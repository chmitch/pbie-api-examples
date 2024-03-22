# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

#from flask import current_app as app
import msal
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class SecretService:

    def get_secret_byname(keyVaultName,secret):
        '''Generates and returns Access token

        Returns:
            string: Access token
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