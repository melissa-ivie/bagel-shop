# The Rat Clan's Development of Inventory System for Dan's Bagels

## Project Overview
Dan, the owner of Dan's Bagel Shop, has contracted with The Rat Clan to develop an interactive web app. Dan has given the project team a list of requirements and also optional features to implement if time provides. Customers will use the app to place orders and view the orders' status, and Dan's team will be able to view and manage the orders. The project will be delivered on December 5<sup>th</sup> for final review and approval prior to the shop's opening for business. This document provides an overview of the project and of the development team's organization, processes, and procedures. 

Dan requires that his future potential customers will be able to use the web app to order any of the bagel products offered by the shop in a easy, straightforward way. Any friction the customers encounter could have massive negative implications if customers abandon the ordering and checkout process. As this website is business's only point of sale, there will be significant amount of time spent on user experience optimization. After placing an order, customers will view its preparation status and be alerted when it's ready to be picked up. Each order can have one of the following statuses:

* Ordered
* Preparation (Chef)
* Preparation (Cashier)
* Ready for Pickup
* Completed
* Canceled

Employees of Dan's Bagel Shop will use an internal part of the system to view the status of all open orders, track inventory levels, and view various sales reports. A roles based access control system will ensure that employees can only work with the digital tools relevant to their job. The different roles include:

* **Owner** - Update inventory, view sales reports, and access all tools available to other employees
* **Chef** - View new orders and see which bagels and sandwich toppings are needed
* **Cashier** - View orders the chef has completed and see which spread and drinks are needed

## Team Organization
All team members will be involved in the high-level design of the project. This is necessary to ensure that all team members have the same overall vision. Low-level design and implementation will be divided between two groups: back-end and front-end. The back end group will create the database and develop the system for handling all incoming HTTP requests to the web server. The front end group will be responsible for UI and UX development, planning page layout, and writing the client-side HTML, CSS, and JavaScript. Collaboration between the two groups is necessary as both teams will need to agree on the values to be passed to Django templates and the information included in HTTP requests/responses.

## Software Development Process
The development will be broken up into five phases.  Each phase will be a little like a Sprint in an Agile method and a little like an iteration in a Spiral process.  Specifically, each phase will be like a Sprint, in that work to be done will be organized into small tasks, placed into a “backlog”, and prioritized.   Then, using on time-box scheduling, the team will decide which tasks each phase (Sprint) will address.  The team will use a Scrum board to keep track of tasks in the backlog, tasks in the current Sprint, tasks in progress, and completed tasks.

Each phase will also be a little like an iteration in a Spiral process, in that each phase will include some risk analysis and that any development activity (requirements capture, analysis, design, implementation, etc.) can be done during any phase.  Early phases will focus on understanding (requirements capture and analysis), and subsequent phases will focus on design and implementation.  Each phase will include a retrospective.

| Phase | Iteration |
| ----- | --------- |
| 1 | Requirements Capture |
| 2 | Analysis, Architectural, UI, and DB Design |
| 3 | Implementation and Unit Testing |
| 4 | More Implementation and Testing  |

The Unified Modeling Language (UML) will be used to document user goals, structural concepts, component interactions, and behaviors.

## Communication policies, procedures, and tools
Our collaboration procedures are as follows: 
* Always do a `git pull` before beginning new work
* Always do a `git push` after doing any work (i.e., don't keep your local changes local any longer than necessary)
* After each push, send a Saturn emoji (🪐) to the group chat with all development team members
* Never resolve merge conflicts on your own if it involves any code written by somebody else as determined by `git blame`. Communication will primarily be accomplished via group text message as this is fast, easy, and highly accessible.

## Risk Analysis

#### User Authentication

* Likelihood: Medium. We've never designed a system that requires us to manage any sort of user permissions. 
* Severity: High. This is absolutely necessary for the application to function correctly
* Consequences: Just about everything will be broken if this isn't done right. 
* Work-arounds: There is definitely a way to do this, it might just be hard to do elegantly.

#### Profile Management

* Likelihood: Low. This only requires changing the state of local data. 
* Severity: Medium. This is an important feature, but there are some workarounds. 
* Consequences: It will be more work on the user's end to change account information. 
* Work-arounds: Accounts could simply be deleted and recreated if account information needed to be changed. 

#### Order Placing

* Likelihood: Low. This is nothing more than a standard web request. 
* Severity: High. This is basically the point of the system. 
* Consequences: Everything. Dan can't sell bagels if people can't order them. 
* Work-arounds: None. Has to be done. 

#### Owner Inventory Management

* Likelihood: Low. This only requires changing the state of local data.
* Severity: High. Dan needs to know how many bagels he can sell 
* Consequences: Dan will never know if an order can really be fulfiled.
* Work-arounds: None. Has to be done.

#### Reports

* Likelihood: Low. This is basically a print statement in a for loop
* Severity: Low. Dan can still sell bagels without reports.
* Consequences: Almost none. No other part of the software relies on reports. 
* Work-arounds: If nice reports can't be generated we could print the whole database table and let Dan sort through it. 

#### Database Design
* Likelihood: Medium. It shouldn't be a problem but we've never done this before
* Severity: High. Without the database, nothing else will work
* Consequences: The web app will not be interactive and orders will not be able to be placed or received
* Work-arounds: Customers can write down their orders on paper and send them into the shop via carrier pigeon


## Configuration Management 
Refer to the [README](../README.md)
