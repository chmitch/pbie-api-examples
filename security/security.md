### Entra
These notebooks illustrate two methods for authenticating to Entra.  Since these processes are highly repetitive they're typically encapsulated in [aadservice.py](../services/aadservice.py) file for all but these notebooks to make them easier to read.

1. [Entra Service Principal Auth](./EntraServicePrincipalAuth.ipynb) - This illustrates the process for authenticating a Service Principal with a shared secret.
1. [Entra Device Code Auth](./EntraDeviceCodeAuth.ipynb) - Since we cannot do an interactive authentication in an Jupyter notebook, this method illustrates how to login as a user with a device code authentication flow.  This method can be used for APIs that don't presently support service principal authentiation.