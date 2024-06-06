# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license

class const:

    resourceGroup = "cgmpbie"  
    subscriptionId = "7258b7d4-3429-4998-815b-8cd6954b7ef9"
    entraTenant = "9f01a99c-6282-465a-94e6-fa7e97720b22"
    pbiClientId = "58c356c7-d4da-4d54-949c-29033fe85400"
    pbiScope = "https://analysis.windows.net/powerbi/api/.default"
    entraAuthority = "https://login.microsoftonline.com/organizations"

    
    #used by notebooks in the capacity examples.
    capacityName = "cgmthisisatest"
    workspaceName = "cgmthisisatest"

    #We use this user so that we can examine what we've created after the fact.
    globalAdminUser = "chmitch@microsoftanalytics.info"

    #We always add these two users, one is our service principal.  This allows us to manipulate the workspace after it's created
    #the other is the app id of our service principal.  This ensures we can assign capacities to worksapces after they are created.
    administrators = [globalAdminUser,'6709b293-4789-477f-aee2-607b7139e63c']

    #Name of the database server where you can create databases
    serverName = "cgmpbiesqlserver"
    tenantRoot = "cgmpbietenant"

    #default azure region
    location = "westus2"
    
    #name of the keyvault to use for storing and retreiving secrets
    keyVault = "cgmmlservicevault"

    #Add another Admin to the database for convenience so you can connect to the database in Azure Data Studio or Query Editor.
    secondaryAdmin = "chmitch@microsoftanalyitcs.info"