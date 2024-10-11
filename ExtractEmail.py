import os
import re

directory = '/Users/annawilliams/Desktop/RegularExpressionsExtractWords/text'
filenames = os.listdir(directory)
all_emails = []
for filename in filenames:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    pattern = '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}'
    email = re.findall(pattern, content)
    all_emails.extend(email)
print(all_emails)
