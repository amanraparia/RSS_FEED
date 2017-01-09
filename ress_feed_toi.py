import feedparser
import sqlite3



stories= []
count = 0
i = 0
count = int (count)


myfeed = feedparser.parse ("http://timesofindia.indiatimes.com//rssfeedstopstories.cms")


length = len (myfeed.entries)




while (length > count) :

		stories.append(myfeed.entries[count].title)
		count = count + 1



print (stories)
print ("------------------------------------------------")
 
while (i == 0) :

	for post in myfeed.entries :

		if post not in stories :

			stories.append (post.title)
			break


print ("---------------- Block 2--------------------------")
print (stories)
		  

	













	 
