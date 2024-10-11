import os
import re


directory = '/Users/annawilliams/Desktop/RegularExpressionsExtractWords/text'
filenames = os.listdir(directory)

all_sentences = []
for filename in filenames:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    pattern = r'[A-Za-z0-9,;"\'\s\-()]+[.!?]'
    sentences = re.findall(pattern, text)
    all_sentences.append(sentences)

for sentence in all_sentences:
    print(sentence)