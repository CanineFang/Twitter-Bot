import tweepy
#Do not share these keys with anyone
api_key="WVRWcERkb185NVVOUi1NQWlmNDc6MTpjaQ"
api_secret= "zD3gjGtUGjjEUEhB7WQzwcMEKMWmP0zPF_eg7UCFdxPTO2ZNyC"
bearer_token= r"AAAAAAAAAAAAAAAAAAAAALRKrQEAAAAAhvPfM0W4Hc46oMiFNBP64xjTNSU%3DwJmWQ5GS9rxDZw1mcoEpOSVyM7RsZetaYaDTbxbwfLu86lxMmT"
access_token= "901870380062789637-3V4VJ1OfCbRgAyFzDnruZYYJDRquNLU"
access_secret= "wXdMEN3mXSULG25LdWhHxl2xTfuP0qFPh1HigBWHvZcn5"

client=tweepy.Client(api_key,api_secret, bearer_token, access_token, access_secret)
auth= tweepy.OAuthHandler(api_key, api_secret, access_token, access_secret)
api= tweepy.API(auth)