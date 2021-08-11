from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation

text = "Natural language processing (NLP) is a field " + \
       "of computer science, artificial intelligence " + \
       "and computational linguistics concerned with " + \
       "the interactions between computers and human " + \
       "(natural) languages, and, in particular, " + \
       "concerned with programming computers to " + \
       "fruitfully process large natural language " + \
       "corpora. Challenges in natural language " + \
       "processing frequently involve natural " + \
       "language understanding, natural language" + \
       "generation frequently from formal, machine" + \
       "-readable logical forms), connecting language " + \
       "and machine perception, managing human-" + \
       "computer dialog systems, or some combination " + \
       "thereof."
words=word_tokenize(text)
print(sent_tokenize(text))
print(words)
words_wo_punc=[]
tokens={}
tokens_wo_punc={}
for i in words:
    x=''
    for j in i:
        if j not in punctuation:
            x+=j
    if x!='':
        words_wo_punc.append(x)

for i in words:
    if i.lower() not in tokens:
        tokens[i.lower()]=1
    else:
        tokens[i.lower()]+=1
        
for i in words_wo_punc:
    if i.lower() not in tokens_wo_punc:
        tokens_wo_punc[i.lower()]=1
    else:
        tokens_wo_punc[i.lower()]+=1

print("With Punctuation: ", len(tokens))
for i in tokens:
    print("{}:\t{}".format(i, tokens[i]))

print('\n----------------------------')
print("\nWithout Punctuation: ", len(tokens_wo_punc))

for i in tokens_wo_punc:
    print("{}:\t{}".format(i, tokens_wo_punc[i]))

chara={}
chara_wo_punc={}

for i in text:
    if i not in punctuation:
        if i.lower() not in chara_wo_punc:
            chara_wo_punc[i.lower()]=1
        else:
            chara_wo_punc[i.lower()]+=1
    if i.lower() not in chara:
        chara[i.lower()]=1
    else:
        chara[i.lower()]+=1
print("With Punctuations: ", len(chara))
print(chara)

print("Without Punctuations: ", len(chara_wo_punc))
print(chara_wo_punc)