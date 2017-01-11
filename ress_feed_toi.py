import feedparser

urls = []

config = open("config.txt","r")

feed_urls = config.readlines()
if feed_urls [-1] == "\n" :

	feed_urls.pop()

for feed_url in feed_urls :

	urls.append (feed_url.split("\n")[0].split("=")[1])
 	
for url in urls :

	myfeed = feedparser.parse (url)
	
	for post in myfeed.entries :

		print (post.title)
	
	print ("-------------------------")


		



	
	








		  

	













	 
