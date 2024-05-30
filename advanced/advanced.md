# Advanced Scenarios
While several of the notebooks in this repo focus on the basic mechanics of executing a call to the Power BI REST API.  The vast majority of these scnarios are a basic two step process:
1. Authenticate to Entra
1. Execute the PUT/POST/GET call to the endpoint with the appropriate parameters and/or body.

However, there are several more sophisticated scenarios that imply a longer sequence of steps.  All these scenarios are built upon the building blocks of the earlier demonstrated API calls; however, these notebooks are designed to illustrate these more complex sequences of steps.

## Notebooks

1. [Create Service Principal](./CreateServicePrincipal.ipynb) - Creating a service principal is a multi step process via graph api, and you need to consider capturing sescrets as well.  This illustrates that process.
1. [Create New Tenant](./CreateNewTenant.ipynb) - In a Power BI Embedded multi-tenant solution creating a new tenant involves many pieces and many APIs (Power BI, Azure, Graph), this illustrates a coordinates process of creating all the necessary resources in order and granting the necessary security permissions.
1. [Create SQL DB](./CreateSQLDB.ipynb) - this is really part of Power BI at all, but included in this repo because a common pattern for multi-tennant solutions involves a multi-step process that involves creating new tenant databases in addition to creating the necessary capacities, workspaces, etc. in Power BI.