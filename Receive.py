import email
import imaplib

EMAIL = 'tic4302.devops@gmail.com'
PASSWORD = 'P@ssw0rdNUS'
SERVER = 'imap.gmail.com'

def get_inbox():
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)

    mail.select('inbox')

    status, data = mail.search(None, 'ALL')

    mail_ids = []
    my_message = []
    for block in data:

        mail_ids += block.split()

    for i in mail_ids:

        status, data = mail.fetch(i, '(RFC822)')


        for response_part in data:
            email_data = {}
            if isinstance(response_part, tuple):

                message = email.message_from_bytes(response_part[1])

                mail_from = message['from']
                mail_subject = message['subject']

                for header in ['from', 'subject', 'to', 'date']:
                    print("{}: {}".format(header, message[header]))
                    email_data[header] = message[header]

                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():

                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:

                    mail_content = message.get_payload()

                email_data['body'] = mail_content

                print(f'From: {mail_from}')
                print(f'Subject: {mail_subject}')
                print(f'Content: \n{mail_content}')

            my_message.append(email_data)
    return my_message

if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)

# print(search_data)