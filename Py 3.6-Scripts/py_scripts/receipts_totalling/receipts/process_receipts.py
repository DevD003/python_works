import os
import glob
import json
import shutil

#try to make directory if it doesnt exist
try:
    os.mkdir('./processed')

#If the director already exits
except OSError:
    print('"Processed" - Dir already exists')

#Globbing to call in the receipts
receipts = glob.glob("./generated_receipts/receipt-[0-9]*.json")

#starting up with a subtotal of 0.0
subtotal = 0.0

#iterate over the receipts
for path in receipts:
    #now opening the path of each receipt
    with open(path) as f :
        #json.load X  json.dump - loading receipts, deserialising json to python objects
        content = json.load(f)
        #for each receipt, we cast it as float, add the value of its topic to subtotal - incrementing
        subtotal+= float (content['value'])

    #caling the name of file using split on string WRT '/' char, we need the last split value
    name = path.split("/")[-1]
    #"./new/receipt-1.json".split('/') ---> ['.','new','receipt-1.json'][-1]

    #creating destination...
    destination = f"./processed/{name}"
    shutil.move(path,destination)
    print(f"--- moved --- {path} ---> {destination}")

print("Reciept Subtotal : $ %.2f" %subtotal)
