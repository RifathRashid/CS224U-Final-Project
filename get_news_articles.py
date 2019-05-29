
'''
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='secret_key')

top_headlines = newsapi.get_everything(q='Lyft',
									language='en',
									from_param='2019-04-26')

for article in top_headlines['articles']:
	print("_____________________________________")
	print(article['title'])
	print(article['content'])
	print("_____________________________________")
'''


import newspaper

cnn_paper = newspaper.build('http://cnn.com')

for article in cnn_paper.articles:
	print(article.url)


for category in cnn_paper.category_urls():
	print(category)
