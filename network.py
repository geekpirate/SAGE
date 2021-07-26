import pandas as pd
import csv
import re
import string
import xlrd
import nltk
import pandas as pd
import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# uncomment below lines when the code is compiled for the first time
nltk.download('stopwords')
nltk.download('words')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

stopword = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopword += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopword += ['already', 'also', 'although', 'always', 'am', 'among']
stopword += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopword += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopword += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopword += ['because', 'become', 'becomes', 'becoming', 'been']
stopword += ['before', 'beforehand', 'behind', 'being', 'below']
stopword += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopword += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopword += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopword += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopword += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopword += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopword += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopword += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopword += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopword += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopword += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopword += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopword += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopword += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopword += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopword += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopword += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopword += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopword += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopword += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopword += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopword += ['off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or']
stopword += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopword += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopword += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopword += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopword += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopword += ['some', 'somehow', 'someone', 'something', 'sometime']
stopword += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopword += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopword += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopword += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopword += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopword += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopword += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopword += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopword += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopword += ['whatever', 'when', 'whence', 'whenever', 'where']
stopword += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopword += ['wherever', 'whether', 'which', 'while', 'whither', 'who', 'aom']
stopword += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'year']
stopword += ['within', 'without', 'would', 'yet', 'you', 'your', 'pray', 'monday', 'tuesday', 'wednesday', 'thursday',
             'friday', 'saturday', 'sunday']
stopword += ['yours', 'yourself', 'yourselves', 'knows', 'know', 'aot', 'type', 'time']

contractions = {
    "Id": "I would",
    "ain't": "am not / are not",
    "aren't": "are not / am not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had / he would",
    "he'd've": "he would have",
    "he'll": "he shall / he will",
    "he'll've": "he shall have / he will have",
    "he's": "he has / he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how has / how is",
    "i'd": "I had / I would",
    "i'd've": "I would have",
    "i'll": "I shall / I will",
    "i'll've": "I shall have / I will have",
    "i'm": "I am",
    "i've": "I have",
    "isn't": "is not",
    "it'd": "it had / it would",
    "it'd've": "it would have",
    "it'll": "it shall / it will",
    "it'll've": "it shall have / it will have",
    "it's": "it has / it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she had / she would",
    "she'd've": "she would have",
    "she'll": "she shall / she will",
    "she'll've": "she shall have / she will have",
    "she's": "she has / she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as / so is",
    "that'd": "that would / that had",
    "that'd've": "that would have",
    "that's": "that has / that is",
    "there'd": "there had / there would",
    "there'd've": "there would have",
    "there's": "there has / there is",
    "they'd": "they had / they would",
    "they'd've": "they would have",
    "they'll": "they shall / they will",
    "they'll've": "they shall have / they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had / we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what shall / what will",
    "what'll've": "what shall have / what will have",
    "what're": "what are",
    "what's": "what has / what is",
    "what've": "what have",
    "when's": "when has / when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where has / where is",
    "where've": "where have",
    "who'll": "who shall / who will",
    "who'll've": "who shall have / who will have",
    "who's": "who has / who is",
    "who've": "who have",
    "why's": "why has / why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had / you would",
    "you'd've": "you would have",
    "you'll": "you shall / you will",
    "you'll've": "you shall have / you will have",
    "you're": "you are",
    "you've": "you have"
}

symptomBag = []
s = set(stopwords.words('english'))
words = set(nltk.corpus.words.words())
newWords = {"burping", "aches", "ache", "coughing"}
words.update(newWords)
# nlp = spacy.load('en_core_web_sm')
s = s.union(set(stopword))


def patternRecogniton(inputText):
    txt = " ".join(w.lower() for w in nltk.wordpunct_tokenize(inputText) if w.isalpha())
    # w.lower() in words and
    for word in txt.split():
        if word in contractions:
            txt = txt.replace(word, contractions[word])
    txt = re.sub(r'[^\w]', ' ', txt)
    txt = unidecode.unidecode(txt)
    text_tokens = word_tokenize(txt)
    text_tokens = [word for word in text_tokens if not word in string.punctuation]
    bigram = [pd.Series(nltk.ngrams(text_tokens, 2))]
    trigram = [pd.Series(nltk.ngrams(text_tokens, 3))]
    for i in range(len(text_tokens) - 1):
        # skeptical = ["RB"+"JJ", "CC"+"NN", "JJ"+"NN"+"3", "JJ"+"NN"+"NN", "IN"+"NN"]
        # ignore = ["PRP$"]
        # ignoreWords = ["someone", "please", "thanks"]
        # maybe = ["DT"+"NNS"]
        bipattern = ["NN" + "NN", "NNS" + "NNS", "VBD" + "NN", "VBP" + "NN", "NNP" + "NN", "VBG" + "NNS", "RB" + "NNS",
                     "NN" + "CC", "VBG" + "NN", "NNP" + "NNP", "VB" + "NNS", "VB" + "NN", "RB" + "VBG", "CC" + "VBG",
                     "NN" + "NNS", "RB" + "VBN", "JJ" + "NN", "DT" + "NNS",
                     "TO" + "VB", "VBP" + "VBD", "VBP" + "VBG", "VBG" + "VBG"]
        tripattern = ["NN" + "RB" + "VBZ", "CC" + "NN" + "VBD", "CC" + "CD" + "NN"]
        if ((nltk.pos_tag(bigram[0][i])[0][1]) + (nltk.pos_tag(bigram[0][i])[1][1])) in bipattern:
            if i > 0:
                finalWord = nltk.pos_tag(bigram[0][i])[0][0] + " " + nltk.pos_tag(bigram[0][i])[1][0]
                finalWord = " ".join([word for word in word_tokenize(finalWord) if word not in s])
                if len(finalWord) > 1:
                    symptomBag.append(finalWord)
                # if (nltk.pos_tag(bigram[0][i])[0][0] not in s) and (nltk.pos_tag(bigram[0][i])[1][0] not in s):
                #   print(nltk.pos_tag(bigram[0][i])[0][0] + " ," + nltk.pos_tag(bigram[0][i])[1][0])
                #   symptomBag.append(nltk.pos_tag(bigram[0][i])[0][0] + " " + nltk.pos_tag(bigram[0][i])[1][0])
                # elif (nltk.pos_tag(bigram[0][i])[0][0] not in s) and (nltk.pos_tag(bigram[0][i])[1][0] in s):
                #   print(nltk.pos_tag(bigram[0][i])[0][0])
                #   symptomBag.append(nltk.pos_tag(bigram[0][i])[0][0])
                # elif (nltk.pos_tag(bigram[0][i])[0][0] in s) and (nltk.pos_tag(bigram[0][i])[1][0] not in s):
                #   print(nltk.pos_tag(bigram[0][i])[1][0])
                #   symptomBag.append(nltk.pos_tag(bigram[0][i])[1][0])
        if i < len(text_tokens) - 3:
            if ((nltk.pos_tag(trigram[0][i])[0][1]) + (nltk.pos_tag(trigram[0][i])[1][1]) + (
                    nltk.pos_tag(trigram[0][i])[2][1])) in tripattern:
                finalWord = nltk.pos_tag(trigram[0][i])[0][0] + " " + nltk.pos_tag(trigram[0][i])[1][0] + " " + \
                            nltk.pos_tag(trigram[0][i])[2][0]
                finalWord = " ".join([word for word in word_tokenize(finalWord) if word not in s])
                if len(finalWord) > 1:
                    symptomBag.append(finalWord)
                # print(nltk.pos_tag(trigram[0][i])[0][0] + " " + nltk.pos_tag(trigram[0][i])[1][0] + " " +
                # nltk.pos_tag(trigram[0][i])[2][0]) symptomBag.append(nltk.pos_tag(trigram[0][i])[0][0] + " " +
                # nltk.pos_tag(trigram[0][i])[1][0] + " " + nltk.pos_tag(trigram[0][i])[2][0])


# load excel with its path
wb = xlrd.open_workbook(
    "C:/Users/sairo/Documents/ark/Project/DE/Posts_csv/Survior Corps_Posts/1_1 - 1_2 Survivor Corp.xls")
finalSymptoms = []
# sh = wb.sheet_names()
sh = wb.sheet_by_name("1_1 - 1_2 Survivor Corp")
# iterate through excel and display data
count = 0
for i in range(sh.nrows):
    if count == 10:
      break
    count += 1
    print(sh.cell_value(i, 0))
    patternRecogniton(sh.cell_value(i, 0))
    # fname = "C:/Users/sairo/Documents/ark/Project/DE/Posts_csv/Survior Corps_Posts/Symptoms_1_1 - 1_2 Survivor
    # Corp.csv"
    finalSymptoms.append(symptomBag)
    symptomBag = []
# print(finalSymptoms)
# for words in finalSymptoms:
#  print(",".join([i for i in words]))

file1 = open("/Users/abhinavreddy/Documents/Masters/Fb Long Haulers/DE/Posts_csv/Survior Corps_Posts/"
             "Symptoms_1_1 - 1_2 Survivor Corp.txt", "w")
# with open('/Users/abhinavreddy/Documents/Masters/Fb Long Haulers/DE/Posts_csv/Survior Corps_Posts/'
#           'Symptoms_1_1 - 1_2 Survivor Corp.csv',
#           'w') as outfile:
#   writer = csv.writer(outfile)
for row in finalSymptoms:
    # writer.writerow(row)
    file1.writelines(",".join([i for i in row]))
    file1.writelines("\n")
# /file1.close()
