# Setup
In order to use these sample notebooks there is some Azure Infrastructure required.  This section documents the expected resources required to leverage the code as written, and will refer to existing docuemntation wherever possible.

### Power BI Tenant & Entra Configuration
Several of the APIs require specific access to a Power BI Tenant.  This docuemnt: https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal covers the process of creating a Service Principal, and configuring the Power BI Tenant to allow the Service Principal to execute APIs.  Note: we highly recommend using a Service Principal wherever possible for two reasons:
1. A service principal will not require a Power BI Pro license to execute the necessary APIs.
1. It is exceptioanlly common for Entra Admins to require users to do multi-factor authentication, this makes it impossible to call the API because the authentication reqeusts are not interactive.

### Key Vault
In order to avoid checking in secrets to GitHub, and requiring hard coded passwords and secrets these notebooks all assume you'll be storing senitive data in Azure Key Vault.  You can find the general documentation for setting up KeyVault here:  https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal.  For the purposes of this code we'll need the folloiwng secrets added to keyvault:
1. pbieclientid - This is the Application (client) Id for the application registration created in Entra.
1. pbieclientsecret - This is the certificate created for the application.
1. entraauthority - For teh purposes of this code it will typically be: 'https://login.microsoftonline.com/organizations'
1. pbiscope - this is the permissions scope for your application.  For the purposes of this code it is typically  'https://analysis.windows.net/powerbi/api/.default'
1. entratenant - this is the guid of your Entra Tenant, you can find this on the overview page of your tenant.

As you may have noticed.  Several of these components are not true "Secrets", but rather just configuration information.   We added several of these configuration items to Key Vault for simplicity reasons.

### Power BI / Fabric Capacity
Many of the APIs we're exercising will only work when there is a Power BI Capacity, in the interest of getting the full benefit of these notebooks it assumes that at least a minimum capacity exists.  You can find instructions for creating an assigning a capacity here:  https://learn.microsoft.com/en-us/fabric/admin/service-admin-portal-capacity-settings
