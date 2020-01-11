# Udacity Item Catalog

## Project Overview
A web application that provides a list of items within a variety of categories and integrate third party user registration with (**Google account**) and authentication.registered users have the ability to add, edit, and delete their own items.Using Flask Python framework.
## Getting started
You need to :
1. Clone the Item catalog project.

2. Install VirtualBox
Download VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

3. Install Vagrant
download Vagrant from [here](https://www.vagrantup.com/).


## Running the Project:
Navigate to the directory that containing the **vagrantfile**
-Vagrantfile containing:
1. Configuration of the VM.
2. Install Python
3. Install Flask
4. Install sqlalchemy

### Steps:
1. Run the following command to start the VM ssh into the vagrant box:
 - `vagrant up`

2. Run the following command to ssh into the VM:
 - `vagrant ssh`

3. Navigate to catalog directory:
 - `cd /vagrant/catalog`

4. Run the following command to setup the and create the database:
 - `python database_setup.py`

5. Run the following command to insert some data into the database:
 - `python lotsofmenus.py`

7. Run Python Program **loganalysis.py** and log analysis will be printed
 - `python2 loganalysis.py`

8. Finally you can visit the web App using your browser [localhost:5000](http://localhost:5000/).













