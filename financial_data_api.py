from urllib.request import urlopen
import json


class FinancialData(object):

	def __init__(self):
		pass

	def get_quarterly_data(self, ticker):
	    """
	    Receive the content of ``url``, parse it as JSON and return the object.

	    Parameters
	    ----------
	    url : str

	    Returns
	    -------
	    dict
	    """
	    url = ("https://financialmodelingprep.com/api/v3/financial-statement-growth/$TICKER$?period=quarter")
	    url = url.replace('$TICKER$', ticker, 1)
	    response = urlopen(url)
	    data = response.read().decode("utf-8")
	    data = json.loads(data)

	    try: 
	    	return data['growth'][0]
	    except:
	    	return None








