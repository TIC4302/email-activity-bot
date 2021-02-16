import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
#from nltk.corpus import stopwords
import nltk
from nltk.corpus import stopwords
import string

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

stopwords = stopwords.words('english')

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
    formatted_string = text.replace('\r','')
    formatted_string = formatted_string.split("\n")
    formatted_string = ' '.join(formatted_string)
    return formatted_string
   #print(formatted_string)


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
