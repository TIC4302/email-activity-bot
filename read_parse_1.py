### Connecting to email server.
import imaplib
import imapclient
import pyzmail 
import io
from filter_and_formatting_for_cosine import *
import string
import smtplib
from email.message import EmailMessage


i = imapclient.IMAPClient('imap.gmail.com')
imaplib.MAXLINE= 1000000

'''  Responses to enquiry. format_string removes stopwords and perform necessary formatting.'''

responses= {
    format_string("cost price pricing for plan  planA and plan B planB"): "Plan A: $25\nPlan B: $30",
    format_string("Is there a hotline i can call, dial to?") : "123-456-789",
    format_string("Contact phone number") : "123-456-789",
    format_string("new Windows device") : "Google security notification.",
    format_string("new Linux device") : "Google Security notification."
    }

''' Testing to see if key of dictionary has been correctly formatted '''
#for x in responses:
#    print(f"key: {x} , value: {responses[x]}")

''' Logging in. '''
try:
    i.login('tic4302devops@gmail.com', 'P@ssw0rdNUS')
    print("[+] Successful login.")
except:
    print("[-] Failed to login.") 


''' printing our all available folders. '''
#for idx in i.list_folders():
#    print(idx)


''' Selecting folder. Set read only true to instruct server to not mark the msg as being read.'''
#i.select_folder('INBOX', readonly=True)
i.select_folder('INBOX')


''' Fetches email in uid '''
unread_mails = i.search(['UNSEEN'])
print(f"unread_mails: {unread_mails}")


''' print each individual msg. '''
for singlemails in unread_mails:
    # rawmsg that involves the full html.
    print("=================================================================================")
    rawmsgs=i.fetch(singlemails,['BODY[]'])
    msg = pyzmail.PyzMessage.factory(rawmsgs[singlemails][b'BODY[]'])
    customer=msg.get_addresses('from')
    print(f"Unread msg from: {customer[0][0]}")
    print(f"Customer email address: {customer[0][1]}")
    
    #cust_email_add = customer[0][1]
    #cust_name = customer[0][0]


    test_msg=msg.text_part.get_payload().decode(msg.text_part.charset)

# 4th march 2021
    find_cus_email=test_msg.replace("\r",'')
    find_cus_email=find_cus_email.split("\n")
    customer_email_add=find_cus_email[2]
    customer_email_name=find_cus_email[1]
    #print(find_cus_email)
    #print(customer_email_add)


    print(f"Raw Message:\n{test_msg}\n")
    #print(type(test_msg)

    ''' breaking paragraphs into sentence '''
    list_of_sentences = breaking_paragraph_to_sentence(test_msg)
    #print(list_of_sentences)
    #print()

    for index in range(len(list_of_sentences)):
        ''' Format to clean sentences, remove \r\n '''
        list_of_sentences[index] = format_email_text(list_of_sentences[index])
        ''' Format to remove stop words, remove punctuations and change to lowercase '''
        list_of_sentences[index] = format_string(list_of_sentences[index])

    #print(list_of_sentences)
    
    ''' Perform cosine similarity to on each sentence. Verify if it contains our crafted queries
    in responses '''

    list_of_responses_keys = list(responses.keys())
    length = len(list_of_responses_keys)+1
    # test_data[0] is the sentence we will use to test similiarity with the keys of our dictionary
    test_index = 1
    responses_index = 0
    # here we should are storing a dictionary of  key:sentence, value:array of the different cos sim comparison 
    results = []

    # Create test_data 
    for sentence in list_of_sentences:
        test_data = []
        test_data = [None] * length
        test_index = 1
        responses_index = 0

        while test_index <= len(list_of_responses_keys):
            test_data[0] = sentence
            test_data[test_index] = list_of_responses_keys[responses_index]
            test_index += 1
            responses_index += 1
        
        #print(test_data)
        # Perform cosine similarity here.
        vectors = create_vectorizer(test_data)
        #print(vectors)
        for idx in range(1,len(test_data)):
            similarity = cosine_similarity_vectors(vectors[0], vectors[idx])
            individual_sim_dict = {test_data[idx] : similarity}
            results.append((test_data[0], individual_sim_dict))
        
    #print(results)
    #Viewing the results:
    #print(len(results))
    #for row in results:
    #    for keys,value in row[1].items():
    #        print(row[0] , keys , '-->', value)

    cos_sim_key = identify(results)
    #print(cos_sim_key)

    response_to_client = retrieve_response(cos_sim_key, responses)
    #print(f"response to client:\n{response_to_client}")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tic4302.devops@gmail.com', 'P@ssw0rdNUS')
    # not def..
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = customer_email_add
    email['CC'] = 'e0260247@u.nus.edu', 'e0260237@u.nus.edu',
    email['Subject'] = 'TIC4302 Telecommuncation responses to your enquiry'

    content="Hello " + customer_email_name + "!  Thank you for your enquires, kindly see below for the response\n\n" + response_to_client + "\n\nThanks!\nTIC4302 Telecom"
    email.set_content(content)
    server.send_message(email)


print("=================================================================================")

#print(customer_email_add)
#print(customer_email_name)


