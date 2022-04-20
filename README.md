# Corona Archive: Sprint 3 Docs

Find older docs below

**Contributors:** 

#### Utkrist Karky, Sinem Bilge Güler
## About the Project


### Description  

Corona Archive is a web service for tracking, displaying, evaluating, and archiving of the Corona infections in a particular location. There are four different types of users: visitors, establishments, hospitals and the agent. Visitors are the users that visit an establishment and their visits will be tracked by the application. Hospitals have control over the infection status of visitors and the agent has access to all archived information. Detailed explanations about which functionality is available for each one of these users can be found further in this document.

### Built with

- HTML
- CSS
- JS
- Python3
- Flask




## Getting Started

### Guide for installing and getting it to work on your local machine


**Prerequisites**  
-Python 3


### Installation Guide

```

#Clone the repo (git clone <repo's_URL> )

#Create virtial environment
$ python3 -m venv /path/to/venv

# Start virtual environment
$ source venv/bin/activate

# Install all the dependencies
$ pip3 install -r requirements.txt


# Run python server
$ python3 run.py

```

### Links

##### Home page: http://127.0.0.1:5000/
##### Agent login: email: admin, password: password
##### Visitor Login: email:r.geller@gmail.com , password: password:
##### Refer to create_new_db.py file to see all accounts that are created
These are some of the accounts we have
```
agent =Agent(email = 'admin', password = password)
email = 'm.geller@gmail.com'  password= password
nemail = 'r.geller@gmail.com' password= password= password
email = 'r.green@gmail.com' password= password= password
email = 'c.bing@gmail.com' password=password= password


place1 = Place(name='Pizza Protein', email = 'p.protein@gmail.com', phoneNumber = '76458975', password= password= password)
place2 = Place(name='Mcdonalds', email = 'mickeyd@gmail.com', phoneNumber = '43298412', password= password= password)
place3 = Place(name='Ogalo', email = 'og@gmail.com', phoneNumber = '943290473', password= password= password)

hospital = Hospital(name='Hospital1', email = 'hospital@gmail.com', phoneNumber = '5522641404', password= password= password)
```
## Usage
Upon loading the site, the user is brought to a landing page, where old users can sign in[Only one time required]  and new users can chose to sign up
#### Sign up
If the sign up option is chosen, the user will be brought to the sign-up-landing page. Here the user is presented with sign up options for all three types of users, 
the user must choose the account type and create it. However, a user cannot create a hospital account as that is only possible to do through the admin account

#### login

Once account has been created, the user may now login to the account. There is only one login portal and this serves all four types of users. The user only need to login once, after which
through the use of cookies, the user is logged in automatically. 

#### Visitor
If the user is logged in as visitor, The user can scan qr codes. However, if the current status of the user is positve, the user may not scan qr codes. Once the user scans a qr code, a visitation session is started. The user cannot start another visitaion session while there is an active visitation session, even if the user logs out and logs back in. Furthermore, the visior has a dashboard, where the visitor can see the list of visitations and the duration of those vistations  

#### Places
If the user is logged in as a place, the qr code, which is dowloadable is displayed. Furthermore a dashboard feature is also provided that allows the users to check the number of users coming in, their status and the duration of each visit. 

#### Hospitals
The functionality of hosptials are very simple. A hospital can set any user as infected or not infected, using the portal that is in the hospital homepage

#### Admin
Admin, also called the agent, has access to all the visitation that have been made in the app in the admin-dashboard. The admin dashboard shows all the visitations that happened and the staus of the users. Furthermore, the admin can also add new hospitals. 



## Change Log
In this sprint we have implemended a vast array of features that were not there before.  
#### Frontend
A brand new front end has been developed for the whole app that gives it modern asthetics. Each page contains sufficient information about the usage of the app, such that the user no longer needs to refer to the documentation
#### New Landing Page
The landing page is now a login page upon first launch. After the first log in, user will no longer be prompted to login again. The landing page also has a link to the new registrattion page where the user can register as either a visitor or a place. To be registered as a hospital, an agent account is required.
#### New login procedure
login is done with an email address and a password. All users including visitors, places and hospitals have an email address that they register with and use to sign in. The same login in page is used for all users and upon a successful authenticatios are redirected to their respective home pages.
#### Functionality of hospitals
Hopital can now set users as infected when they are tested positve. The hospital homepage has input field for a user email which can be used to set someone as infected.
#### QR codes and active visitation sessions
All places have a unique qr-code based on their email address. This can be used to check in to place by users. When users check in to a place, by manually inputing the email, for now, a visitation session is started. The visitor must end the visitation session for other features to be availible. 

#### New Dashboards
Agents, Visitors and places all have their own dashboards. Agents can see all activities on their dasboard, see infected visitors and see who has come into contact with whome, visitors can see the places they have been in and users and places can see the visitors that have come in. 

#### Place List
There is a new list of places that can be viewed by anyone, including users that are not logged in. This shows the QRcodes, the name and the email, which can be used for manual input. 

#### Packaging 
The app has been pacakged to CoronaArchive so as to prevent any circular imports


# Sprint 2

**Contributors:** Julia Ramos Alves and Arton Jakupi

## About the Project Received

This is a short description of the application developed by the previous team in sprint 1 that was received for our sprint. The home page displays an instruction to scan a QR code and the QR below it, which is associated to the string "You are registered". The register page includes fields for entering "Citizen_ID", address, phone number, email address, and "Device_ID". At the bottom, there is a button which says "Register". There exists a third page which contains a disclaimer.


## About our Project

### Description

Corona Archive is a web service for tracking, displaying, evaluating, and archiving of the Corona infections in a particular location. There are four different types of users: visitors, establishments, hospitals and the agent. Visitors are the users that visit an establishment and their visits their visits will be tracked by the application. Hospitals have control over the infection status of visitors and the agent has access to all archived information. Detailed explanations about which functionality is available for each one of these users can be found further in this document.

### Built with

- HTML
- CSS
- Python3
- Bootstrap
- JS
- Flask
- MySQL


### File Structure

```

```

# SE-Sprint01-Team11

MYSQL tables
-- added databases based on the five classes shown in the UML document
-- Added insert queries to check the database 
-- changed the UML for VisitorToPlaces entry_time & exit_time to TIME format
-- changed the UML for all string variables into varchar variables

Index page
-- sample qr code is generated

Register page
-- user can register their visit here

Disclaimer page
-- shows disclaimer

Installation Guide

## Clone the repo

 git clone git@github.com:Magrawal17/SE-Sprint01-Team11.git

 ## Create virtual environment
 $ virtualenv env

 ## Activate virtual environment
 For Windows-> $.\env\Scripts\activate
 For MacOS/Linux-> $source env/bin/activate

 ## Install all the dependencies
 $ pip install -r requirements.txt
 // Use pip3 for Python3.

 ## Import MySQL Database

 $ mysql -u username -p -h localhost Corona_Archive < Corona_Archive.sql
// Replace username with local database username.

## Run python server
For Python3-> $ python3 app.py
For other versions-> $ python app.py runserver

## Only if error 'mysqlclient' or 'mysql.h' not found

$ pip install .\env\mysqlclient-1.4.6-cp37-cp37m-win32.whl


  
  
  



