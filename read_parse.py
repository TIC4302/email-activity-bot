### Connecting to email server.
import imaplib
import imapclient
import pyzmail 
import io
from filter_and_formatting_for_cosine import *
import string

i = imapclient.IMAPClient('imap.gmail.com')
imaplib.MAXLINE= 1000000

### Responses to enquiry. format_string removes stopwords and perform necessary formatting.
responses= {
    format_string("What are the pricing for plan A planA and plan B planB"): "Plan A: $25\nPlan B: $30",
    format_string("Is there a hotline i can call, dial to?") : "123-456-789",
    format_string("May i know your contact please") : "123-456-789",
    format_string("new Windows device") : "Google security notification.",
    format_string("new Linux device") : "Google Security notification."
    }

''' Testing to see if key of dictionary has been correctly formatted '''
#for x in responses:
#    print(f"key: {x} , value: {responses[x]}")

# Logging in.
try:
    i.login('tic4302devops@gmail.com', 'P@ssw0rdNUS')
    print("[+] Successful login.")
except:
    print("[-] Failed to login.") 

# printing our all available folders. 
#for idx in i.list_folders():
#    print(idx)

# Selecting folder. 
# Set read only true to instruct server to not mark the msg as being read.
i.select_folder('INBOX', readonly=True)

# Fetches email in uid
unread_mails = i.search(['UNSEEN'])
print(f"unread_mails: {unread_mails}")

# print each individual msg.
for singlemails in unread_mails:
    # rawmsg that involves the full html.
    print("=================================================================================")
    rawmsgs=i.fetch(singlemails,['BODY[]'])
    msg = pyzmail.PyzMessage.factory(rawmsgs[singlemails][b'BODY[]'])
    customer=msg.get_addresses('from')
    print(f"Unread msg from: {customer[0][0]}")
    print(f"Customer email address: {customer[0][1]}")
    test_msg=msg.text_part.get_payload().decode(msg.text_part.charset)
    #print(test_msg)
    #print(type(test_msg)

    ''' Format to clean email msg '''
    formatted_text=format_email_text(test_msg)
    ''' Format to clean stopwords '''
    print(f"\nEmail Body Content:\n{formatted_text}")
    removed_stopwords = format_string(formatted_text)
    print(f"\nFormatted Text (removed stopwords):\n{removed_stopwords}")


print("=================================================================================")

''' testing data
print("uid 32 mails: ")
rawmsgs=i.fetch(32,['BODY[]']) 
#print(rawmsg)

msg = pyzmail.PyzMessage.factory(rawmsgs[32][b'BODY[]']) 
subject=msg.get_subject()
customer=msg.get_addresses('from')
to_person=msg.get_addresses('to')
cced=msg.get_addresses('cc')
print(subject)
print(customer)
'''

#msg.text_part != None
#print(msg.text_part.get_payload().decode(msg.text_part.charset))


#msg.html_part != None
#print(msg.html_part.get_payload().decode(msg.html_part.charset))
