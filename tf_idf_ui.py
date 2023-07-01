#userinput - Press enter to enter new word and Blank enter to stop!
import sys
import math
from collections import defaultdict

# Define function to calculate term frequency
def calculate_tf(document):
    tf = defaultdict(int)
    total_words = 0
    with open(document, 'r') as f:
        for line in f:
            for word in line.strip().split():
                tf[word] += 1
                total_words += 1
    for word in tf:
        tf[word] = tf[word] / total_words
    return tf

# Define function to calculate inverse document frequency
def calculate_idf(document, words):
    idf = defaultdict(int)
    total_documents = 0
    with open(document, 'r') as f:
        for line in f:
            total_documents += 1
            words_in_document = set(line.strip().split())
            for word in words_in_document:
                if word in words:
                    idf[word] += 1
    for word in idf:
        idf[word] = math.log(total_documents / idf[word])
    return idf

# Get command line argument
document = sys.argv[1]

# Get words to calculate TF-IDF for from user input
words = []
while True:
    word = input('Enter a word (make a blank Enter to stop): ')
    if not word:
        break
    words.append(word)

# Calculate tf and print to console
tf = calculate_tf(document)
print('Term Frequency:')
for word in words:
    print(word + ':', tf[word])


idf = calculate_idf(document, words)
print('\nInverse Document Frequency:')
for word in words:
    print(word + ':', idf[word])


tfidf = defaultdict(int)
for word in words:
    tfidf[word] = tf[word] * idf[word]
with open('output.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')
        f.write('TF: ' + str(tf[word]) + '\n')
        f.write('IDF: ' + str(idf[word]) + '\n')
        f.write('TF-IDF: ' + str(tfidf[word]) + '\n\n')
