import re
import string
from collections import Counter

import xlrd
from nltk.tokenize import word_tokenize
import nltk
import numpy as np
import matplotlib.pyplot as plt
import unidecode
import pandas as pd
import runsage
nltk.download('punkt')
allgrams = []
unigram = []
bigram = []
trigram = []
def patternRecogniton(inputText):
  txt = " ".join(w.lower() for w in nltk.wordpunct_tokenize(inputText) if w.isalpha())
  txt = re.sub(r'[^\w]', ' ', txt)
  txt = unidecode.unidecode(txt)
  text_tokens = word_tokenize(txt)
  text_tokens = [word for word in text_tokens if not word in string.punctuation]
  unigram.append(pd.Series(nltk.ngrams(text_tokens, 1)))
  bigram.append(pd.Series(nltk.ngrams(text_tokens, 2)))
  trigram.append(pd.Series(nltk.ngrams(text_tokens, 3)))



def getCountDict(filename):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name("Sheet1")
    for i in range(sh.nrows):
        patternRecogniton(sh.cell_value(i, 0))
        allgrams = unigram + bigram + trigram
        return {word: int(count) for word, count in [line.rstrip().split() for line in sh.cell_value(i, 0).readlines()]}

def getCountDictBase(filename):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name("Sheet1")
    for i in range(sh.nrows):
        return {word: int(count) for word, count in [line.rstrip().split() for line in sh.cell_value(i, 0).readlines()]}

base_counts = getCountDict('/Users/abhinavreddy/Documents/Masters/Fb Long Haulers/Results/NonSymptomRelated.xls')
print(base_counts)
exit()
# counts for author Lydia Maria Child
child_counts = getCountDict('/Users/abhinavreddy/Documents/Masters/Fb Long Haulers/Results/SymptomRelated.xls')

print(child_counts)
exit()
# counts for all 1840s letters in the corpus

vocab = [word for word, count in Counter(child_counts).most_common(5000)]

x_child = np.array([child_counts[word] for word in vocab])
x_base = np.array([base_counts[word] for word in vocab]) + 1.

mu = np.log(x_base) - np.log(x_base.sum())
# print(mu.tolist())

eta = runsage.estimate(x_child, mu)
print(runsage.topK(eta, vocab))

print(runsage.topK(-eta, vocab))

