from email.message import EmailMessage

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('tic4302.devops@gmail.com', 'P@ssw0rdNUS')
email = EmailMessage()
email['From'] = 'Sender_Email'
email['To'] = 'dcsacr@nus.edu.sg', 'ssravana@nus.edu.sg'
email['CC'] = 'e0260247@u.nus.edu', 'e0260237@u.nus.edu'
email['Subject'] = 'Email Bot to Generate Email-related Activity'
email.set_content('Hi Aris & Sravana, \r\n'
                  '\r\n'
                  'Please confirm if we are able to proceed with this project. Would to start coding IMAP and SMTP connections. \r\n'
                  'And we would like to commence with our use case of having a webform integrated with the email bot as a automated reply to customers who drop inputs in the form. \r\n'
                  'Also please advise if we are going in the correct direction. Thank you. \r\n'
                  '\r\n'
                  'Regards \r\n'
                  'Desmond & Lucas')
server.send_message(email)
