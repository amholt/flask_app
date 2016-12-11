# yelp api & search documentation:
#	https://github.com/Yelp/yelp-python
#	https://www.yelp.com/developers/documentation/v2/search_api
# enter in terminal: pip install yelp

# in terminal: pip install -U python-dotenv

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os   # use this to import your secret keys

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
	auth = Oauth1Authenticator(
		# consumer_key="Q1MS_LQivTFHlAdBGKGd-A",
		# consumer_secret="8j5w2ZH9sJIvqfofebK4tII-1aA",
		# token="0ltlG4A-6L9p49WUJRkDpVaQB0wuIjuU",
		# token_secret="gZSsP6Ps5A6HP9XWAJQ42oIXqBc"
		consumer_key=os.environ['CONSUMER_KEY'],
		consumer_secret=os.environ['CONSUMER_SECRET'],
		token=os.environ['TOKEN'],
		token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
		'term': 'food',
		'lang': 'en',
		'limit': 3,
	}

	response = client.search(location, **params)

	business_list = []

	for business in response.businesses:     # note businesses is an attribute, not a function
		# print(business.name, business.rating, business.phone)
		business_list.append({"name": business.name,
			"rating": business.rating,
			"phone": business.phone
		})
	
	return business_list

businesses = get_businesses("Oakland",'food')

for business in businesses:
	print(business)