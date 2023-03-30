import os, subprocess
wordlist = "Steganography/Output/wordlist" #Change me

print("===A_Openstego_Cracker===\n*Welcome", os.getlogin(),"\nWordlist selected:", wordlist,"\n=========================\n")
wordlist = open(wordlist, "r")
for i in wordlist:
	cmd = ""
	print("Testing : ", i)
	path = "java -jar ./openstego\(1\).jar extract -sf Steganography/Output/Stego_Image.bmp -p " #Change me
	cmd = path + i
	print(cmd)
	os.system(cmd)
print("Created by: Richard Fare")

