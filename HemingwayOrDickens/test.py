import pandas as pd
import nltk 
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import math
import warnings
warnings.filterwarnings("ignore")

with open("hemingway_test.txt", encoding='utf8') as hemingway_test:
	hemingway_test = hemingway_test.read()
	hemingway_sentences = nltk.sent_tokenize(hemingway_test)

with open("dickens_test.txt", encoding='utf8') as dickens_test:
	dickens_test = dickens_test.read()
	dickens_sentences = nltk.sent_tokenize(dickens_test)

punc = ['?', ',', '.', '!', '-', '_', '“', '”', ';', '[', ']']
data = pd.read_csv("data.csv")

correct_hemingway = 0 
wrong_hemingway = 0

correct_dickens = 0 
wrong_dickens = 0

for sentence in hemingway_sentences:
	word_list = []
	word_list = word_tokenize(sentence)
	word_list = [word.lower() for word in word_list if word not in punc]
	word_list = [word for word in word_list if word not in stopwords.words('english')]
	word_list = [word for word in word_list if not word.isdigit()]

	result = 0

	for word in word_list:
		try:
			index = data.loc[data['Unique Words'] == word].index[0]
			log_prior = math.log(data["Hemingway Laplace"][index]/data["Dickens Laplace"][index])
			result = result + log_prior
		except:
			pass

	if result > 0:
		correct_hemingway = correct_hemingway + 1
	else:
		wrong_hemingway = wrong_hemingway + 1

for sentence in dickens_sentences:
	word_list = []
	word_list = word_tokenize(sentence)
	word_list = [word.lower() for word in word_list if word not in punc]
	word_list = [word for word in word_list if word not in stopwords.words('english')]
	word_list = [word for word in word_list if not word.isdigit()]

	result = 0

	for word in word_list:
		try:
			index = data.loc[data['Unique Words'] == word].index[0]
			log_prior = math.log(data["Hemingway Laplace"][index]/data["Dickens Laplace"][index])
			result = result + log_prior
		except:
			pass

	if result < 0:
		correct_dickens = correct_dickens + 1
	else:
		wrong_dickens = wrong_dickens + 1

accuracy_dickens = correct_dickens / (wrong_dickens+correct_dickens)
accuracy_hemingway = correct_hemingway / (wrong_hemingway+correct_hemingway)

print("Accuracy for Ernest Hemingway: ", accuracy_hemingway)
print("Accuracy for Charles Dickens: ", accuracy_dickens)

