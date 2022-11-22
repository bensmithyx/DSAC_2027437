import os, colours, re, pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from pickle import load, dump

def refine_text(text):
    words = ' '.join([WordNetLemmatizer().lemmatize(word) for word in re.sub('[^a-zA-Z]',' ',text).lower().split() if word not in set(stopwords.words('english'))])
    return words

def predict_spam(text):
    return text_svm.predict([refine_text(text)])


while True:
    getinput = colours.menu(['Menu','Train dataset','Test model','Exit'])

    if getinput == 1:
        dataset = pd.read_csv('../datasets/spam.csv', sep=',', names=['label','message','a','b','c'])

        dataset['message'] = [refine_text(dataset['message'][index]) for index in range(0, len(dataset))]

        X = dataset['message']
        y = dataset['label']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

        text_svm = Pipeline([('tfidf',TfidfVectorizer()),('svm',LinearSVC())])
        text_svm.fit(X_train,y_train)

        dump(text_svm, open('model.pkl', 'wb'))

    elif getinput == 2:
        text_svm = load(open('model.pkl', 'rb'))
        '''for file in os.listdir('../datasets/enron4/spam/'):

            with open(f'../datasets/enron4/spam/0008.2003-12-18.GP.spam.txt', 'r') as data:
                data = data.readlines()
            print(predict_spam(' '.join(data[1:]))[0])
            break'''

        data = ['Congratulations, you have won a lottery of $5000. To Won Text on,555500 ','Hey mate how are you doing?','Can I borrow some prime for tomrrow please',"You have won £3000! To claim your prize go to http://clickme.com"]

        [print(predict_spam(text)[0]) for text in data]
        print(predict_spam(input('>'))[0])
    elif getinput == 3:
        break
