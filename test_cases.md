## Testing Plan for Email Bot AI

### Test Case: 01 - Automated Functionality Test in GitHub
### Description: Testing of the Email Bot through automated YAML scripts using Django. 

### Steps: 
* Creation of the testing workflow using YAML
* Install Python and Dependent Libraries 
* Start up Django Server
* Run test cases within test_file.py

Input: python manage.py runserver
output: Server successfully up and running


### Test Case: 02 - Email Bot Functionality	
### Description: Email Bot Functionality Test. This unit test is to mimic a conversation between a customer and the Email Bot itself. 

### Steps: 
* Run test cases within test_result.py
* IMap libraries to pull emails from allocated gmail mailbox
* Email Analyser to run on existing unread email
* Cosine similarities libraries to run to aid email analysis 
* Keywords are picked up and appropriate responses are to be sent back to the original sender
* Confirm successful results within github action 

Input: May i know what is the price for plan A ?

Thank you

Output: Thank you for your enquires, kindly see below for the response

Plan A: $25
Plan B: $30
