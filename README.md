# Linus Server Configuration - FSND Project
For this project, a Ubuntu Linux server was launched on the Amazon Lightsail platform. The web app is an item catalog that allows users to create 'categories' and post 'items' within them. It uses Google and Facebook Oauth2 authentication to validate and manage users as well a PostgreSQL database to handle data. All and only logged in users can create, edit, and delete their own entries.

## Specifications for Graders
The IP address of the web app is `34.212.235.166` and can be reached using the following url: `http://ec2-34-212-235-166.us-west-2.compute.amazonaws.com/`. It allows for SSH connections via `port 2200`, HTTP via `port 80`, and NTP via `port 123`. SSH is enforced by private RSA key.

## Software Used
Most of the Flask and SQLAlchemy code was written for a previous project; however, SQLite was replaced with the more robust PostgreSQL. Python 2.7 was used rather than 3. The project was developed and debugged using a Virtual Box and Vagrant. Now the code is hosted using Amazon Lightsail. The following were done to accomplish this:
* Create new instance in Lightsail
* Make a private key on a local machine using `keygen`
* Login via SSH from local machine and create a new user with sudo allowances
* Using `sudo ufw` commands update the port configuration to allow incoming traffic on ports 80, 123, and 2200,
* Set local timezone to UTC
* Installed Git and cloned files from personal repository, made the .git directly inaccessible to public users
* Disabled
* Created a user `catalog` with permission to create database
* Created `catalog.db`, initialized it with `database_setup.py`, and populated it with `populate_db.py`
* Installed Apache 2, python, virtualenv, PostgreSQL, all of the dependent libraries for the web app
* Updated registration on Google and Facebook developer pages

## References
In terms of setup and configuration, github user `stueken`'s README file (`https://github.com/stueken/FSND-P5_Linux-Server-Configuration`) came in quite handy given the relative lack of detailed course material on key parts of the project. I referred to the Digital Ocean tutorial (`https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps`) for structuring files. I did refer to many Udacity posts on the discussion boards, and while they did give me some context to issues at hand, none of them offered a solution to my particular bugs, Facebook access credentials in particular. Nonetheless they were worthwhile.
