import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
#from nltk.corpus import stopwords
import nltk
#from nltk.corpus
nltk.download('punkt')

'''
to install stopwords resource:
python3.8 -m nltk.downloader stopwords
'''

'''
Stopwords are those common words such as "i", me", "my, "that", "this" 
which commonly interferes with the real contents that we are making 
comparison with. These words are extracted from the user sentence so that
we can have quality comparison. 

eg: [customer] This is a car and the brand is Toyota 
    (stripped off stopwords: car brand Toyota)

eg: [carshop]  We have a car model that is Toyota.
    (stripped off stopwords: car model Toyota)

Comparing "car brand Toyota" and "car model Toyota" yields better results
in terms of comparing sentences for the actual content we are interested in.
'''

#stopwords = stopwords.words('english')
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
#print(stopwords)


def format_string(text):
    text = ''.join([word for word in text if word not in string.punctuation])
   # print(f"Removed punctuations: {text}")
    text = text.lower()
   # print(f"Text in lowercase: {text}")
    text = ' '.join([word for word in text.split() if word not in stopwords])
   # print(f"Removed stopwords: {text}")
    return text

'''
Converting 1D array to 2D array for computation of consine similarity.
The functions require the input to be 2D array.
'''
def cosine_similarity_vectors(vector1, vector2):
    vector1 = vector1.reshape(1,-1)
    vector2 = vector2.reshape(1,-1)
    # Verifying
    #print(vector1)
    return cosine_similarity(vector1,vector2)[0][0]

''' 
Removing Carraiage return, splitting the email content by new line 
and reconstruct the sentence
'''
def format_email_text(text):
   # formatted_string = text.replace('\r','')
   # formatted_string = text.replace('\n','.')
    formatted_string =  text.replace('\r\n','. ')
    #formatted_string = formatted_string.split("\n")
    #formatted_string = ' '.join(formatted_string)
    return formatted_string
   #print(formatted_string)

'''Turning those text into vectors in preparation for cos sim computation'''
def create_vectorizer(list_of_formatted_text):
    vectorizer = CountVectorizer().fit_transform(list_of_formatted_text)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim

''' Breaking the email content into array of sentence '''
def breaking_paragraph_to_sentence(paragraph):
    document = nltk.tokenize.sent_tokenize(paragraph)
    return document


''' checking if there is a cosine similarity of more than 0.5, if yes, return the key for verification against the response dictionary '''
def identify(results_array):
    max_value = 0;
    for row in results_array:
        for key,value in row[1].items():
            if value > 0.5:
                if value > max_value:
                    max_value = value
                    print(f"Highest cosine simliarity value: {max_value}\n")
                    max_value_key = key
                    print(f"Matching key:\n{max_value_key}\n")
            else:
                # Assign None if there is no cosine similarity value
                max_value_key = None
        return max_value_key

''' verification of key against response dictionary and return the reply '''
def retrieve_response(key, response_dict):
    if key == None:
        reply_this="Please contact us at 123-456-789"
    else:
        for dict_key,value in response_dict.items():
            if key is dict_key:
                return value
    return reply_this
    
''' Testing breaking_paragraph_to_sentence function 

paragraph = "The first step in most text processing tasks is to tokenize the input into smaller pieces, typically paragraphs, sentences and words. In lexical analysis, tokenization is the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements called tokens. The list of tokens becomes input for further processing such as parsing or text mining. Tokenization is useful both in linguistics (where it is a form of text segmentation), and in computer science, where it forms part of lexical analysis."

test = breaking_paragraph_to_sentence(paragraph)
i = 1
for item in test:
    print (f"line {i} : {item}")
    i += 1

'''

''' testing data 
sentences = [
    'This is a foo bar sentence',
    'This sentence is similar to a foor bar sentence.',
    'This is another string, but it is not quite similar to the previous one.',
    'I am also just another string.'
    ]

'''

''' For testing

for i in sentences: 
    test = clean_string(i)
    print(test)
'''

'''
formatted = list(map(format_string, sentences))
print(formatted)

vectorizing = CountVectorizer().fit_transform(formatted)
vectors = vectorizing.toarray()
print(vectors)
cosine_sim = cosine_similarity(vectors)
#print(cosine_similarity_vectors(cosine_sim[0]))
sim1 = cosine_similarity_vectors(cosine_sim[0], cosine_sim[1])
sim2 = cosine_similarity_vectors(cosine_sim[0], cosine_sim[2])
sim3 = cosine_similarity_vectors(cosine_sim[0], cosine_sim[3])
print(sim1)
print(sim2)
print(sim3)
'''
