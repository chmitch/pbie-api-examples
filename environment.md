
# Environment
These notebooks are designed to build conceptually, but also be self contained.  That means you're not expected to run them in a specific sequence; however, more complex notebooks often obfuscate a concept addressed in an earlier notebook for simplicity reasons.  For example, all the notebooks require authenticating against Entra to get a bearer token to pass to the rest APIs.  The process for doing that authentication is demonstrated in the EntraServicePrincipalAuth and EntraDeviceCodeAuth notebooks.   However later on that process is encapsulated in the /services/aadservice.py file so that the notebooks can avoid having a lot of highly repetitive code.

In order to run these notebooks it assumes you have a notebook server for execution.   While any notebook server should be able to run this code, we've not tested every possible scenario.  Two scenarios have been tested.

## In Azure Compute
1. Azure Machine Learning - you can run notebooks on Azure Machine Learning compute instances.

## Locally
1. Azure Data Studio - Azure Data Studio has a notebook capability, that assumes you have a local install of python.
