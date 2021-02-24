About
=================================

Hello! I don't have much code to share because most of the code I've written over the years is still on private repositories.
I didn't have much opportunities to work on open source projects either, so I've decided to share these bits of code as a start.

Description
=================================

A few months ago, I've applied to a company for a Software Engineer position.
This is a small project developed for the coding contest provided by this company.
The goal was to create at least 2 endpoints of a basic restful api in order to manage text ressources.
To do that, I've used the python framework called Flask, and sqlite as a database.
I've also used the following libraries: flask_restful, flask_migrate and sqlalchemy.

Most of the code developed is located in the "app" directory.
There are also the Makefile and the content of the "scripts" directory.
You will also find tests in the test.py file. Logs are written in the logs directory.

Requirements
=================================

To make this application work, you need to install the following packages (on Linux):
```
sudo apt-get install python3 python3-pip
```

Setup
=================================
  
Unzip the package then go to the root directory:
```
cd contest
``` 
Then:
```
make install
```
This creates a python virtualenv and everything needed to manage the sqlite database.
If the make command is not installed, just use the following command to install the build-essential package:
```
sudo apt-get install build-essential
```
And finally run the application with the following command:
```
make run
```
The application should be available at the following address:
```
http://127.0.0.1:5000/document
```
The page should be empty as there is no document in the database for now.

There are other commands. To execute the test developed with pytest:
```
make test
```
To open a shell with the virtual environment, use:
```
make shell
```
To clean the installation (virtual env + database) before reinstalling it, use:
```
make clean
```
You will find more details in the "Makefile" file, and in the directory called "scripts"


Current features
==========================================================

1. Posting a text

    You can add one "long" text by using this command:
    ```
    curl --data "text=This+is+a+long+text" http://127.0.0.1:5000/text
    ```
    This command returns a document_id which can be used to use the next commands

1. Getting a text

    You can list a text by using the following command:
    ```
    curl http://127.0.0.1:5000/text/<document_id>
    ```
    You can also use your navigator and go to:
    ```
    http://127.0.0.1:5000/text/<document_id>
    ``` 

1. Getting a summary

    You can list a summary of a document by using this command:
    ```
    curl http://127.0.0.1:5000/summary/<document_id>
    ```
    You can also use your navigator and go to:
    ```
    http://127.0.0.1:5000/summary/<document_id>
    ```
    Warning: current default value of the summary text field is "This is a summary"
   
1. Listing documents

    Not asked but really useful for debugging purposes, you can use the following endpoint to list the documents:
    ```
    http://127.0.0.1:5000/document
    ```
    
Missing technical improvements & comments
=================================

- no size limit or specific constraints specified by the company about the large text sent to the API
- default value given to documents summary
- current tests are basic cases, and are not really "unit" tests as such, 
they are more functional text because the code uses libraries and it's very simple.
- we could create a sqlite test database instead of using the same for dev and tests
- a Docker file could be provided to make the installation easier


