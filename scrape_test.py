from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter

from final_test import TwitterClient
def start_work(user):
	twitterclient=TwitterClient()
	consumer_key="jqibaucxKcrxc4WkezhPGCkT3"
	consumer_secret="Yw1ZGOQ2mGIIAIrzWFdEnCHQVNMnnH0WbppN4EhKy3fbQa7JqG"
	access_token="792270234543620096-rnTmvYp4nELdXECTx9MKGiy78ZxkjTs"
	access_token_secret="D4lp8a73KB1TUvNmG0WbMO7D4t2WZSSR3OmnpFKLj1hjD"

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	auth_api = API(auth)
	end_date = datetime.utcnow() - timedelta(days=45)
	
	l1=[]
	for status in Cursor(auth_api.user_timeline, id=user).items():
		l1.append(str(status.id))
		if status.created_at < end_date:
			break
	mn=[]
	mn.append(l1)
	print (mn)
	delt=twitterclient.working_code(mn)
	return(delt)	
