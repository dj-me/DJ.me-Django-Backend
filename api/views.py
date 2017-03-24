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
	OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
	
	OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

	client_id = 'f9b9538acdb94eb8ae5fe30216b60b44'

	client_secret = '09cfe4fd21dd44c9b7fd7cdd672fd751'

	redirect_uri = 'https://djme.herokuapp.com/home'

	code = request.GET.get('code')
	print code 
	payload = {'grant_type' : 'authorization_code' , 'code':code  ,'redirect_uri' : redirect_uri  }
	headers = {"Authorization": 'Basic' +  base64.b64encode(bytes(client_id +':' + client_secret, 'utf-8'))}

	r = requests.post(OAUTH_TOKEN_URL , params = payload, headers = headers)
	print r





	return HttpResponse(r.text)
