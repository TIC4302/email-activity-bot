## Email Activity Bot

### Overview 
This bot is an automated marketing tool that will be beneificial for companies which leverage 
on web activities to interact with their customers. It micmicks that of a conversation AI assistant, 
which helps to provide automated response to customers queries through our pre-programmed and structured
queries and responses. Ultimately automating the delivery process.

This email bot is intricately designed to work for telecommunication organisations to enhance and automate
the correspondence between the organisation and their customers. Email bots are becoming increasingly common
within multiple companies due to its multiple benefits that ends up saving cost as well as time productivity 
within its processes. 

3 of the most common benefits for the usage of Email Bots include: 
* Costs reduction within the organisation with reduced manpower allocated to answering email queries from customers 

* Increased Time efficiency & Productivity with email automation as it ends up saving a great deal of 
  time within the organisation as the bot will be able to handle repetitive queries which would have otherwise
  been time intensive for the organisation 
  
* Increased Brand Awareness with clear concise email responses as email automation provides a consistent response
  to the customers, therefore constructing an increasingly organised appearance to its customers 

### Objective 
The purpose of an email bot has the ability to automate the process of responding to various customer enquiries
using the existing organisations email service along with the brand, by using contextual analysis. In the case
of a telecommunications company, the email bot would be able to handle queries in relation to the various services, 
contract plans as well as other telecommunication products that are provided by the company with customised email response.

With the usage of email bots in telecommunication organisations, the overall productivity and efficiency within 
the company will increase, leaving additional time and manpower for additional tasks.We aim to value-add 
businesses by increasing efficiency, saving time for businesses that can be used in more productive areas.

### Design 
Prior to the communication with the email bot, a webform will be used as the platform to bridge the 
correspondence between the customers and the users. The webform would provide the customers the ability 
to input their enquiries in related to the contract plans, services as well as products provided by the telecommunication organisation. 

Once submitting their enquiries, the email bot will be able to parse in the content based on the subject header as 
well as the body of the email for contextual analysis. Based on the contextual analysis done by the email bot, 
the response will be constructed in a customised fashion to respond to the queries posed by the customer. 

### Feature 
* Automated responses on different types of plans, contracts and services.

### Implementation 
* Using Django Framework as our CI/CD pipelines as well as web form creation.
* Using GitHub as a version control platform.
* Using GitHub as a tracker for outstanding issues. 
* Using python as our desired programming languages.

### Consideration. 
* We assume that in the context of telcommuncation, one bot is sufficient to handle the customer's queries. 
* We are handling queries only in context of contracts and services. 
* Complaints will not be considered in our scope.

### Installation guide. 
* cd (desired folder)
* wget https://raw.githubusercontent.com/TIC4302/email-activity-bot/main/download_install_script.sh
* chmod +x download_install_script.sh
* ./download_install_script (This should pull all the remaining installation script.)
* chmod +x ./*.sh (This will give permissions to execute all of the remaining installation script
* ./install.sh (This script will create a virtual environment, pull all code dependencies relating to the bot.)
* ./run_server.sh (This will start the django webserver for you.) 
* ./run_bot.sh (This will run the email automation bot which checks for emails periodically every 30 seconds until terminated.)
*
*  after the above step, navigate to 127.0.0.1:8000/contact/   
*  you may use a legit email as well as a posting an enquiry. It should automatically send you a response. 

### Security Checks.
* To run security checks. Under <desired folder> 
* ./bandit_check.sh (This script runs the email automation script and check for security issues.) 
*  (To check for the whole folder, you may change the script to include the file path, or to run bandit -r <folder or script manually> 

### Customization.
* Customization can be found a the following path: 
* To change email credentials --> <desired folder>/FINAL_TEST/email-activity-bot/config/settings.py
* To change or add fields required for the web page --> <desired folder>/FINAL_TEST/email-activity-bot/sendemail/forms.py
* To add further paths such as /contact --> <desired folder>/FINAL_TEST/email-activity-bot/sendemail/urls.py
* To change or enhance the webpage to your liking --> <desired folder>/FINAL_TEST/email-activity-bot/sendemail/views.py

