 #Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
 #You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
 #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
 #Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
 
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
www = list()
ww1 = list()
ccc = list()
counts = dict()
i = 0
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
       	continue
    www = line.split()  
    www = www[5]
    ww, minutes, seconds = www.split(":") #split the hour min and seconds
    ww1.append(ww) #add hour to a new list only
    
    
for words in ww1: 
    if words in counts:
        counts[words] += 1
    else:
        counts[words] = 1
    #counts[words] = counts.get(words,0)+1
   
for key in sorted(counts):
    print(key, counts[key])
    
    
	#print(sorted([(key,val) for key, val in counts.items()]))

    
                   
   		
