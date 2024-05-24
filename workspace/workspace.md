

### Workspace
One element that might cause some confusion with the Power BI API is the terms Workspace and Group.  In the Power BI portal the term Workspace is used; however in the APIs the term Group is used.   In this documentation we'll use the term "Workspace" a lot, but just know that these terms might be used interchangeably.  The Power BI only has the ability to work with workspaces based on the guid of the workspace, so all apis will start with https://api.powerbi.com/v1.0/myorg/groups/{worksapceID}.  In order to save consumers of this repo from having to discover the guid of the workspace via the portal and hardcode it in the notebooks all of the examples that require a workspaceId will first retreive a list of workspaces from the API and find the guid of the workspace that matches the name stored in (/services/env.py).  This is for the convenience of the consumer of the repo and by no means required.  

1. [List Workspaces](./ListWorkspaces.ipynb) - This retreives a list of all worksapces.
1. [Get Workspace](./GetWorkspace.ipynb) - This retreives a specific workspace given it's id.
1. [Create Workspace](./CreateWorkspace.ipynb) - This creates a new workspace.
1. [Add Workspace User](./AddWorkspaceUser.ipynb) - This addes a user to a specific workspace.
1. [Delete Workspace User](./DeleteWorkspaceUser.ipynb) - This removes a user from a specific workspace.
1. [Delete Workspace](./DeleteWorkspace.ipynb) - This deletes a workspace.
1. [List Reports in Workspace](./ListReportsInWorkspace.ipynb) - This retreives a list of avaialble reports in the provided workspace.


