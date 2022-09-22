# "Baby" Blockchain
Creating a simple, open, and robust python-based blockchain system

# Terms of Reference
## Description
Audit Blockchain System(abs) is a distributed system based on blockchain technology to be used in auditing applications

## Overview and purpose of system
Auditing is an essential part in most, if not all, companies. It's used in the evaluation of money and answering three main questions about the money:
<ul>
<li>Where it's coming from</li>
<li>Where it's going</li>
<li>What it does each step of the way</li>
</ul>

## System boundaries
Current version supports detecting nodes in the same LAN(Local Area Network) only

## Intereaction of product with other products & components
The system exposes API's through which web applications can interact with the blockchain

## Product features
The system run a full blockchain node but without the mining feature. Modules included:
<ul>
<li>Networking and syncronization</li>
<li>Block creation</li>
<li>Key management</li>
<li></li>
</ul>

## Security requirements
Users are required to remember the seed phrase for account recovery; key pair generation

Due to limited number of nodes a 51% attack can be easily performed to change the correct state of the blockchain

The end user should store the private key and seed phrase securely.

### Threat Model
### Violator Model

## Characteristics of end user
The system is designed to serve three major categories:
<ol>
<li>Investors/stake holders</li>
For both public and traded companies, the system acts as the gospel when it comes to evaluating the flow of money into and out of the company
<li>Auditors</li>
Auditors can use this as a tool 
<li>Authorities</li>
For tax purposes or to 
<li>Governments</li>
At a theoretical level, the system may be used at a national scale to track tax payers money through the system and possibly reduce fraud cases
</ol>

## Restrictions

# Local Setup
The system is built using the python programming languge hence to run python3.* is required.
## Install Dependencies
`pip install -r requirements.txt`

## Run Node
`python3 Main.py`

## Open Graphical User Interface
The human interface is built as a web application using a combination of flask and react that interface to the running node<br>
Navigate to <a href="/UI/">`/UI`</a> directory and run: <br>
`flask run --host=0.0.0.0`<br>


## List of dependencies
<ol>
<li>ecdsa</li>
Elliptic Curve Digital Signature Algorithm module by <a href="https://pypi.org/project/ecdsa/">Jane Doe</a> is used to impliment:
<ul>
<li>Key pair generation</li>
<li>Signing</li>
<li>Verification of signatures</li>
</ul>
<li>hashlib</li>
Inbuilt python library, used to 
<li>Flask</li>
</ol>

## Directory Structure
## Sample Usecase

# Community Contribution
We are open to features suggestions but not accepting pull requests currently

# Version History
0.0.0