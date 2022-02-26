import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

with open("Hemingway.txt", encoding='utf8') as hemingway:
	hemingway = hemingway.readlines()

with open("Dickens.txt", encoding='utf8') as dickens:
	dickens = dickens.readlines()

punc = ['?', ',', '.', '!', '-', '_', '“', '”', ';']

unique_words = []
words = []

hemingway_words = []
dickens_words = []

for sentence in hemingway:
	word_list = word_tokenize(sentence)
	word_list = [word.lower() for word in word_list if word not in punc]
	word_list = [word for word in word_list if not word.isdigit()]
	word_list = [word for word in word_list if word not in stopwords.words('english')]
	words.extend(word_list)
	hemingway_words.extend(word_list)

for sentence in dickens:
	word_list = word_tokenize(sentence)
	word_list = [word.lower() for word in word_list if word not in punc]
	word_list = [word for word in word_list if not word.isdigit()]
	word_list = [word for word in word_list if word not in stopwords.words('english')]
	words.extend(word_list)
	dickens_words.extend(word_list)

for word in words:
	if word not in unique_words:
		unique_words.append(word)

hemingway_count = 0
dickens_count = 0
hemingway_count_list = []
dickens_count_list = []

for word in unique_words:
	count = hemingway_words.count(word)
	hemingway_count_list.append(count)
	hemingway_count = hemingway_count + count 

for word in unique_words:
	count = dickens_words.count(word)
	dickens_count_list.append(count)
	dickens_count = dickens_count + count

hemingway_frequinces = []
dickens_frequinces = []

for count in hemingway_count_list:
	hemingway_frequinces.append(count/hemingway_count)

for count in dickens_count_list:
	dickens_frequinces.append(count/dickens_count)

hemingway_laplace = []
dickens_laplace = []

for word in unique_words:
	index = unique_words.index(word)
	laplace = (hemingway_count_list[index]+1) / (hemingway_count+len(unique_words))
	hemingway_laplace.append(laplace)

for word in unique_words:
	index = unique_words.index(word)
	laplace = (dickens_count_list[index]+1) / (dickens_count+len(unique_words))
	dickens_laplace.append(laplace)

df = pd.DataFrame({"Unique Words":unique_words,
				"Used in Hemingway":hemingway_count_list,
				"Used in Dickens":dickens_count_list,
				"Frequinces Hemingway":hemingway_frequinces,
				"Frequinces Dickens":dickens_frequinces,
				"Hemingway Laplace":hemingway_laplace,
				"Dickens Laplace":dickens_laplace})

df.to_csv("data.csv",index=False)




