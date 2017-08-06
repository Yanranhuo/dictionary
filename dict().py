# dictionary
# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number 
# of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person
## who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary is produced, 
 #the program reads through the dictionary using a maximum loop to find the most prolific committer.
 
 
name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
lm = list()
www=list()
counts= dict()

handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    else:
        lm = line.split()
        www.append(lm[1])
        
for words in www:
    counts[words] = counts.get(words,0)+1
	
Bigcount = None
Bigword = None
for word,count in counts.items():
 	if Bigcount is None or count> Bigcount:
        Bigword = word 
        Bigcount = count
        
print(Bigword,int(Bigcount/2))
            

    
