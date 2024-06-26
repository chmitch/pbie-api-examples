# Code Overview
The following is an organized overview of the various notebooks and supportying Pyton modules in this repo.

## Notebooks

### Entra
These notebooks illustrate two methods for authenticating to Entra.
1. [Entra Service Principal Auth](./EntraServicePrincipalAuth.ipynb) - This illustrates the process for authenticating a Service Principal with a shared secret.
1. [Entra Device Code Auth](./EntraDeviceCodeAuth.ipynb) - Since we cannot do an interactive authentication in an Jupyter notebook, this method illustrates how to login as a user with a device code authentication flow.  This method can be used for APIs that don't presently support service principal authentiation.

### Workspace
One element that might cause some confusion with the Power BI API is the terms Workspace and Group.  In the Power BI portal the term Workspace is used; however in the APIs the term Group is used.   In this documentation we'll use the term "Workspace" exclusively.
1. [List Workspaces](./ListWorkspaces.ipynb) - This retreives a list of all worksapces.
1. [Get Workspace](./GetWorkspace.ipynb) - This retreives a specific workspace given it's id.
1. [Create Workspace](./CreateWorkspace.ipynb) - This creates a new workspace.
1. [Add Workspace User](./AddWorkspaceUser.ipynb) - This addes a user to a specific workspace.
1. [Delete Workspace User](./DeleteWorkspaceUser.ipynb) - This removes a user from a specific workspace.
1. [Delete Workspace](./DeleteWorkspace.ipynb) - This deletes a workspace.

### Capacities

1. [Create Capacity](./CreateCapacity.ipynb) - This creates a new Fabric Capacity on your Azure Subscription.
1. [Pause Capacity](./PauseCapacity.ipynb) - This pauses a running Fabric Capacity.
1. [Start Capacity](./StartCapacity.ipynb) - This starts a paused Fabric Capacity.
1. [Update Capacity](./UpdateCapacity.ipynb) - This changes attributes of an existing capacity, most likely used for resizing the capacity.
1. [List Capacities](./ListCapacities.ipynb) - This returns a list of capacities visible to the tenant.
1. [Assign Capacity to Workspace](./AssignCapacityToWorkspace.ipynb) - This assigns a specific capacity to a workspace.
1. [Remove Capacity from Workspace](./RemoveCapacityFromWorkspace.ipynb) - This unassigns a capacity from a workspace.

### Report

1. [Capacity examples](/capacity/capacity.md) - Examples of creating and managing capacities.
1. [Security examples](/security/security.md) - Examples of both authenticating users and creating service principals.
1. [Import examples](/import/import.md) - Examples of importing Power BI models in different scenarios.
1. [Workspace examples](/workspace/workspace.md) - Examples of creting an managing workspaces.

## Other Resources



### services
This folder contains python modules we use to encapsulate repetitive logic that is frequently used.  This is useful in many ways.  Primarily if we discover a bug we can fix it in one place, plus it keeps the notebooks more readable as they stay focused on the task at hand.
1. [aadservice.py](./services/aadservice.py) - This code encapsulates the call to authentiate an Entra Service Principal
1. [secretservice.py](./services/secretservice.py) - This code encapsulates the call to retreive named secrets from Key Vault

