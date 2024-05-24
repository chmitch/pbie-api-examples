# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class const:

    # Camel casing is used for the member variables as they are going to be serialized and camel case is standard for JSON keys

    resourceGroup = "cgmpbie"  
    subscriptionId = "7258b7d4-3429-4998-815b-8cd6954b7ef9"
    
    #used by notebooks in the capacity examples.
    capacityName = "cgmthisisatest"
    workspaceName = "cgmthisisatest"
    #We use this user so that we can examine what we've created after the fact.
    globalAdminUser = "chmitch@microsoftanalytics.info"
    #We always add these two users, one is our service principal.  This allows us to manipulate the workspace after it's created
    #the other is the app id of our service principal.  This ensures we can assign capacities to worksapces after they are created.
    administrators = [globalAdminUser,'6709b293-4789-477f-aee2-607b7139e63c']

    serverName = "cgmpbiesqlserver"
    tenantRoot = "cgmpbietenant"
    location = "westus2"
    
    keyVault = "cgmmlservicevault"

    #Add another Admin to the database for convenience so you can connect to the database in Azure Data Studio or Query Editor.
    secondaryAdmin = "chmitch@microsoftanalyitcs.info"