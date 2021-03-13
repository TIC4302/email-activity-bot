from email.message import EmailMessage

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('tic4302.devops@gmail.com', 'P@ssw0rdNUS')
email = EmailMessage()
email['From'] = 'Sender_Email'
email['To'] = 'tic4302.devops@gmail.com'
#email['CC'] = 'e0260247@u.nus.edu', 'e0260237@u.nus.edu'
email['Subject'] = 'Email Bot to Generate Email-related Activity'
email.set_content('Hi TIC4302 Telecommunications, \r\n'
                  'May I know what is the pricing for plan B?' 
                  '\r\n\n'
                  'Regards \r\n'
                  'Test customer')
server.send_message(email)
