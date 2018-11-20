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

#starting up with a subtotal of 0.0
subtotal = 0.0

#iterate over the receipts
for path in glob.iglob("./generated_receipts/receipt-[0-9]*.json"):
    #now opening the path of each receipt
    with open(path) as f :
        #json.load X  json.dump - loading receipts, deserialising json to python objects
        content = json.load(f)
        #for each receipt, we cast it as float, add the value of its topic to subtotal - incrementing
        subtotal+= float (content['value'])

    #using the str.replace to replace the destination path of the folder
    destination = path.replace('generated_receipts','processed')
    shutil.move(path,destination)
    print(f"--- moved --- {path} ---> {destination}")

print("Reciept Subtotal : $ %.2f" %subtotal)
