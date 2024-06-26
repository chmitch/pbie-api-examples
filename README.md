# Power BI REST API Examples
This repository is intended to demo various scenarios leveraging the Power BI REST APIs.  The documentation for these APIs can be found here:  https://learn.microsoft.com/en-us/rest/api/power-bi/.  While this docuemntation does cover the capabilities of the APIs, having a functional code example of the APIs in action can be helpful.  Furthermore when addressing advanced scenarios, understanding how to sequence execution of the APIs can also be useful.  This repo strives to illustrate the core concepts of leveraging these APIs in Python.  We chose Python as the language to do this for three reasons:
1. There are published SDKs for C# and Java, both of wich wrap the APIs and obfuscate some of the complexities you may encounter using the APIs directly.
1. Python makes dealing with JSON quite simple and since many of these APIs accept JSON as inputs it makes the code clean and easy to read.
1. There was a distinct lack of Python examples at the time we authored this.

## General resources
1. [Setup](setup.md) - covers what infrastructure is required in azure
1. [Environment Configuration](environment.md) - covers how to setup your development environment
1. [Advanced Scenarios](advanced.md) - digs into complex scenarios that involve orchestration of multiple apis to complete

## Notebooks
In the interest of making this readme easier to consume, we've broken it into sub sections.
1. [Capacity examples](/capacity/capacity.md) - Examples of creating and managing capacities.
1. [Embed examples](/embed/embed.md) - Examples of different embed scenarios.
1. [Security examples](/security/security.md) - Examples of both authenticating users and creating service principals.
1. [Import examples](/import/import.md) - Examples of importing Power BI models in different scenarios.
1. [Workspace examples](/workspace/workspace.md) - Examples of creting an managing workspaces.
1. [Dataset examples](/dataset/dataset.md) - Examples of working with dataset settings.

## Other
This folder contains some files to illustrate the process of deploying models to Power BI via the API.
1. [files](/files/files.md) - power bi model files used for examples.
1. [services](/services/services.md) - a collection of python classes that are reused across multiple notebooks
1. [models](/models/models.md) - a collection of class wrappers to support json serialization/deserialization for api calls.


## Other considerations and reminders
* The resources these examples use are fairly inexpensive in Azure terms, but they do cost money.  If you're using these libraries for learning purposes, it is prudent to develop the habit of pausing resources when they are not in use.
* In order to do all the actions demonstrated in these notebooks it does assume that you have administrative permissions on a Power BI tenant.  If you do not have those permissions it will be necessary to collaborate with a Power BI tenant Admin to complete some of the setup steps.  Once those steps have been completed you should be able to leverage the Service Principal to perform the majority of the Power BI API calls.

## Contributors
- Chris Mitchell
- Mike Shelton