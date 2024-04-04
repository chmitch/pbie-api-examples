# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class Credential:
    credentialType = None
    credentials = None
    encryptedConnection = None
    privacyLevel = None 

class credentialDetails:

    credentialDetails = None

    def __init__(self, credential_type, credential_body, encrypted_connection, privacy_level):
        cred = Credential()
        cred.credentialType = credential_type
        cred.credentials = credential_body
        cred.encryptedConnection = encrypted_connection
        cred.privacyLevel = privacy_level
        
        self.credentialDetails = cred
        
