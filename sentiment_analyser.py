from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize


sentence = '''The platform provides worst very bad aweful.'''



def analSentiment(text):
    
    text_tokens = word_tokenize(text)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    text_without_sw = " ".join(tokens_without_sw)
    print("Cleaned text: "+text_without_sw)
    analysis = TextBlob(text_without_sw).sentiment
    #print(analysis.polarity) 
    return analysis.polarity   



