# Practice Docker Django Project

This repository is a practice project for setting up and running a Django application using Docker and Docker Compose.

Installation Guide

Requirements
To run this project, you will need to have the following things installed:


Python 3.9 +
Docker and Docker Compose
Django 
MySQL ( database used in this project)




Installation
1. first clone the repository
go to terminal and do following
Copy 
git clone https://github.com/Nirav-Zignuts/practice.git


2. now Set up a virtual environment

Copy below command 
python3 -m venv denv
source denv/bin/activate  
3. Install dependencies
Install the required Python packages :

Copy
pip3 install -r requirements.txt
4. Set up the database

configre database credentials 
dbname,user,password,host,port 
inlude all this thing in database field in docker compose file's db section




5. Run the containers using below command server

docker-compose up --build 

application will be served at http://127.0.0.1:8000/


Features:
--> The main objective of this project is get hands on of how to use docker and docker compase to build multi container application.
--> project is based on simple crud rest api for student.
--> Get all student details
--> Get specific student details
--> create a new student
--> update existing student details
--> delete existing student 


