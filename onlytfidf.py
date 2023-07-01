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

# Define function to calculate tf-idf
def calculate_tfidf(tf, idf):
    tfidf = defaultdict(int)
    for word in tf:
        tfidf[word] = tf[word] * idf[word]
    return tfidf

# Get command line arguments
document = sys.argv[1]
words = sys.argv[2:]

# Calculate tf, idf, and tf-idf
tf = calculate_tf(document)
idf = calculate_idf(document, words)
tfidf = calculate_tfidf(tf, idf)

# Write tf-idf to file
with open('output.txt', 'w') as f:
    for word in words:
        f.write(word + ' ' + str(tfidf[word]) + '\n')

# Print tf-idf to console
for word in words:
    print(word + ':', tfidf[word])
