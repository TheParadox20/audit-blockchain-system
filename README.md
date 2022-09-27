# Audit Blockchain System
A simple, open, and robust python-based blockchain system

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
The system strives to accomplish the above three core functions

## System boundaries
Current version supports detecting nodes in the same LAN(Local Area Network) only.

Only one institution can be audited by a cluster of nodes

## Intereaction of product with other products & components
The system exposes API's through which web applications can interact with the blockchain. Some of the exposed utilities include:
<ul>
<li>Account/ Wallet creation</li>
<li>Transaction creation and sending</li>
<li>Blockchain explorer; data extraction</li>
</ul>

## Product features
The system runs a full blockchain node, excluding the mining feature. Modules included:
<ul>
<li>Networking and syncronization</li>
<li>Block creation</li>
<li>Key management</li>
<li>Wallet management</li>
<li>Transaction creation and validation</li>
<li>Data visualization</li>
</ul>

## Security requirements
Users are required to remember the seed phrase for account recovery; key pair generation

Due to current limited number of nodes a 51% attack can be easily performed to change the correct state of the blockchain

The end user should store the private key and seed phrase securely.

## Characteristics of end user
The system is designed to serve three major categories:
<ol>
<li>Auditors</li>
Auditors can use this as a tool to make tests on available financial documents
<li>Authorities</li>
For tax purposes or to prove fraudulent activities. Due to it's open, immulatble nature, a money trail can be easily followed
<li>Investors/stake holders</li>
For both public and private companies, the system acts as the gospel when it comes to evaluating the flow of money into and out of the company
<li>Governments</li>
At a theoretical level, the system may be used at a national scale to track tax payers money through the system and possibly reduce fraud cases
</ol>

## Restrictions
Lack of a complex concencus mechanism; unlike in other blockchain networks such as ethereum which include a poof of work or proof of stake concensus algorithm. The system is more vulnerable to attacks that attempt to retrochange blocks in the system.

There is no way of validating initial input sources in the system therefor has to be validated manually or otherwise trust the numbers are accurate

# Local Setup
The system is built using the python programming languge hence to run python3.* is required.
## Install Dependencies
`pip install -r requirements.txt`

## Run Node
`python3 Main.py`

## Open Graphical User Interface
The human interface is built as a web application using a combination of flask and react that interfaces to the running node<br>
`flask run --host=0.0.0.0`<br>
The link provided after running the server directs to the web application

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