# Dan's Bagels (by The Rat Clan)

## Organization and Name Scheme

Files will be organized separately between the front and backend of the web tool. They will be placed in folders that allow for a clear modular organizational structure and will include a doc directory detailing other project information. This directory will include the project plan, requierments and any other necessary documentation. 

There will be a standardized name scheme for the project to ensure uniformity and cohesion. This Scheme will adhere to the following conventions: 
* Variable names will be written in `snake_case`
* Class names will be in `UpperCamelCase` 
* File names (excluding source code files) will be all lower case words separated by hyphens like `bagel-lovers.txt`
* All class, variable and file names wil be descriptive and intituive to their purpose 

## Version Control Procedures

To assure that the project maintains the highest level of proficiency and professionalism we will be using a remote git repository hosted on github.com. All project members are following a strict policy of pulling project notes and changes before editing any documents or files. All project members will be notified via direct message with the 🐀 emoji when changes have been made to the project. This will remind all project members that changes have been made and a pull request will need to be completed before any other changes can be made. This assures everyone having access to the same files that are up to date. 

In the event that merge conflicts arise, project members will trace the code that is causing the conflict and restore it to a previous merge state. All changes will be pushed and the changes can then be added back in. 

Because git is a version control system, it will track previous versions of all our files and code. This will assure our ability to return to previous versions of the project and track all changes and edits. It also enables us to simultaneously work on our project and return the files to one another in a state where they are all up to date and current with the project. 

## Tool Stack Description and Setup
The client-side component of this project will be developed using Hypertext Markup Language (HTML) in conjunction with Cascading Style Sheets(CSS). HTML will determine how content is organized and CSS will style that content. We will additionally use Vue.js and JavaScript to add interactivity to the web page.

The server-side of this project will be implemented using Python with the Django(v3.0)  web framework. Merging and version control will be set up and maintained using git in conjunction with our version control procedures. 


## Build Instructions
There are no build instructions. We are implementing this project in Django, which is a framework written in Python. Because all code will be written in Python, an interpreted language, no compilation is necessary. In addition, Django also automatically checks for changes within a project and essentially builds itself. To run the server, the instructions are as follows
1. Clone this repository
2. Navigate into `bagel_shop` directory
3. At your terminal run

        $ python manage.py migrate
4. Run 

        $ python manage.py runserver

You can now poke around the different URLs of the site. As of now, we have a prototype for account creation at `/accounts/create` and password resetting at `/accounts/reset-password`. 

## Unit Testing Instructions
Unit testing will be utilized to ensure continuous functionality and project integrity. All major functions and classes will have an associated unit test which can be employed in regression testing when adding new functionality. 
An instance that exemplifies this goal is writing a unit test for a function to update an order status. That unit test would be run before merging the associated branch with the main branch.

## System Testing Instructions
We will employ system testing in our project to verify continuous functionality and project integrity. Any significant project changes will be accompanied by a system test to verify the application performs tasks as designed.  

An instance that exemplifies this goal is implementing a systems test for a new feature that allows application users to change their user role within the application. After adding this feature, the related system test will ensure that the all user roles can be viewed and used correctly after switching. 

## Other Notes
Rats for life.  

