from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import urllib2
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Image
from django.http import HttpResponse
import urllib2
from django.utils.decorators import method_decorator
import json
import requests
import sys
import base64
# import spotipy
# import spotipy.util as util

# Create your views here.

def home(request):
	# OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
	
	# OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

	client_id = '33704938095-g3uhslf1enbgg84hb40k0924mgea5arm.apps.googleusercontent.com'

	client_secret = 'nOylsHNF81OOE5MwdUf2zhLv'

	redirect_uri = 'https://djme.herokuapp.com/home'

	code = request.GET.get('code')
	print code 
	payload = {'grant_type' : 'authorization_code' , 'code':code  ,'redirect_uri' : redirect_uri  , 'client_id':client_id , 'client_secret' : client_secret  }
	# headers = {"Authorization": 'Basic' +  base64.b64encode(bytes( 'f9b9538acdb94eb8ae5fe30216b60b44:09cfe4fd21dd44c9b7fd7cdd672fd751'))}

	r = requests.post('https://www.googleapis.com/oauth2/v4/token' , params = payload)
	print r
	t = json.loads(r.text)
	z = t['access_token']
	headers = {'Host' : 'gdata.youtube.com' , 'Content-Type' : 'application/json' , 'Content-Length': 'CONTENT_LENGTH'  ,"Authorization": "Bearer " + z , 'GData-Version': '2' , 'X-GData-Key': 'key=DEVELOPER_KEY' } 

	q = requests.post('https://www.googleapis.com/youtube/v3/playlists' , headers = headers)


	print q 



	return HttpResponse(q.text)

https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=33704938095-g3uhslf1enbgg84hb40k0924mgea5arm.apps.googleusercontent.com&redirect_uri=https://djme.herokuapp.com/home&scope=https://www.googleapis.com/auth/youtube