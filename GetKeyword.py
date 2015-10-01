import nltk
import os
import string
import textmining
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import Counter
from collections import OrderedDict
from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

#import GensimTopic
stop_word= stopwords.words('english')
doc=''
wc={}
bi_wc={}
unigram=[]
def term_doc(file):
     bigrams=bi_wc.keys()
     #print unigram
     for line in file:
         text=line.translate(string.maketrans("!~$/#@%':+?).,{}-(;*&\\\"","                       "), string.digits)
         text=text.lower()
         text=text.split()
         pos_tag=nltk.pos_tag(text)
         for word in text:
                 if word not in stop_word and word not  in unigram and word!='skills' and word!='etc' and word!='must':
                     word=lmtzr.lemmatize(word)
                     if word not in wc:
                          wc[word] = 1 
                     else: 
                         wc[word] += 1
#print wc 


def find_unigram(bi_wc):
     global unigram
     for k,v in bi_wc.items():
         if v>=2:
             #print k, 'corresponds to', v
             word=k.split()
             word=word[0].split("_")
             #print word[0],word[1]
             unigram.append(word[0])
             unigram.append(word[1])
     return unigram

def bigrams(file):
     doc=''
     global unigram
     for line in file:
         text=line.translate(string.maketrans("!~$/#@%'{:+?).},-(;*&\\\"","                       "), string.digits)
         text=text.lower()
         text=text.split()
         global bi_wc
         if len(text)!=0:
             for i in range(len(text)-1):
                 if text[i] not in stop_word and text[i+1] not in stop_word :
                     bigram=text[i]+'_'+text[i+1]
                     if bigram not in bi_wc:
                          bi_wc[bigram] = 1 
                     else: 
                         bi_wc[bigram] += 1
         
for i in os.listdir(os.getcwd()):
     if i.endswith(".txt"): 
         #print i
         file= open(i, 'r')
         bigrams(file)
         find_unigram(bi_wc)
         file= open(i, 'r')
         term_doc(file)
         continue
     else:
         continue

test='Experience in Java is a must. Knowledge of Spring, Struts, Hibernate . Should be good with algorithms, data structures. Should have working knowledge of GIT. Should have worked in an agile environment. Communication skills should be great'
test=test.lower()
test=test.split()
pos_tag=nltk.pos_tag(test)

new_text=[]
for i in range(len(pos_tag)):
     #print pos_tag[i][1],pos_tag[i][0]
     if (pos_tag[i][1].startswith('NN') or pos_tag[i][1].startswith('NNP')):
                 #print pos_tag[i+2][0],'1'
         new_text.append(pos_tag[i][0])
#print new_text
for i in range(len(pos_tag)-2):
     if (pos_tag[i][1].startswith('NN') and pos_tag[i+1][1].startswith('IN') and pos_tag[i+2][1].startswith('NN')):
         #print new_text
         new_text.remove(pos_tag[i][0])
        # print new_text
#print new_text
test=' '.join(new_text)
test=test.translate(string.maketrans("!~$/#@%'{:+?).},-(;*&\\\"","                       "), string.digits)
test=test.split()
for word in test:
     if word in stop_word:
         test.remove(word)
output=[]
for i in range(len(test)-1):
     #print test[i],'222'
     if  bi_wc.get(test[i]+'_'+test[i+1],None)>1:
         print test[i]+'_'+test[i+1],bi_wc.get(test[i]+'_'+test[i+1])
         #output.append(test[i]+'_'+test[i+1])
for pre_word in test:
     word=lmtzr.lemmatize(pre_word)
     #print word
     if  wc.get(word,None)>=2:
         print pre_word,wc.get(word)
#print test
