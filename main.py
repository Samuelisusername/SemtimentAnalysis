# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import string
import nltk
import ssl
from collections import Counter
import matplotlib.pyplot as plot

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')

text = open('read.txt', encoding='utf8 ').read()
lower_case = text.lower()
cleaned_text =  lower_case.translate(str.maketrans('','',string.punctuation)) #do we really need to do that :(
tokenized_text = cleaned_text.split()


from nltk.corpus import stopwords
#print(stopwords.words('english'))
final_words = []
for word in tokenized_text:
    if word in stopwords.words('english'):
        continue
    else: final_words.append(word)
print(final_words)

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
plot.bar(w.keys(),w.values())
plot.savefig('graph.png')
plot.show( )
