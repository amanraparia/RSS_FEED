import feedparser



urls = []

config = open("config.txt","r")

feed_urls = config.readlines()
feed_urls.pop()

for feed_url in feed_urls :

	feed_url = feed_url.split("=")[1]
	urls.append (feed_url.split("\n")[0])

for url in urls :

	myfeed = feedparser.parse (url)
	
	for post in myfeed.entries :

		print (post.title)


		



	
	








		  

	













	 
