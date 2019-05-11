from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='af23605afdc54110bce1b726f110d18b')

top_headlines = newsapi.get_everything(q='Lyft',
									language='en',
									from_param='2019-04-06')

for article in top_headlines['articles']:
	print("_____________________________________")
	print(article['title'])
	print(article['content'])
	print("_____________________________________")
