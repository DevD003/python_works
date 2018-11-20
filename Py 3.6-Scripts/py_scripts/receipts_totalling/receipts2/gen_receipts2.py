import random
import os
import json

#using os package with try,except to make dir or confirm existing
try:
    os.mkdir("./generated_receipts")
except OSError:
    print(" 'generated_receipts' ---- Folder already exists")

#using os package to input no. of files to be read, with a max value of 100
count=int(os.getenv("file_count") or 100)

#opening stripped words fom the words in /usr/share/dict/words
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

#Generating the Data set -by iterating through count creating dict
for identifier in range(count):
    #generating random amount in range of 500
    amount =random.uniform(1.0, 500)
    #creating a dict with random topic and float value of the amount
    content= {
            'topic':random.choice(words),
            'value':"%.2f" %amount
            # % indicates calling var, .2 indicates the float is 2 decimals
            }

    #Open a file, with name name-{identifier} and is a json file,write mode
    with open(f"./generated_receipts/receipt-{identifier}.json",'w') as f:
#to write the contents to the file followed by the writable obj - the file
        json.dump(content,f)

        print(f"---Generated receipt-{identifier}.json---")
