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


from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from api.models import user , hostsong , djsessions , finalplaylist 

# import spotipy
# import spotipy.util as util

# Create your views here.
z  = ''
p_id = ''
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
	global z 
	z = t['access_token']

	# headers = {'Host' : 'gdata.youtube.com' , 'Content-Type' : 'application/json' , 'Content-Length': 'CONTENT_LENGTH'  ,"Authorization": "Bearer " + z , 'GData-Version': '2' , 'X-GData-Key': 'key=DEVELOPER_KEY' } 
	data  = {
	# 'part' : 'contentDetails' , 
    'snippet': {
      'title': 'Vishrut 123', 
      'description': 'Sample playlist for Data API',
     }
  }

	headers = {'Content-type': 'application/json', 'Accept': 'text/plain' , "Authorization": "Bearer " + z}
	q = requests.post('https://www.googleapis.com/youtube/v3/playlists?part=snippet' , headers = headers , data=json.dumps(data))


	print q 
	a  = json.loads(q.text)
	global p_id
	p_id = a['id']
	s = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q=shape+of+you&type=video&videoDefinition=high' , headers = headers )
	songs  = json.loads(s.text)
	v_id  = songs['items'][0]['id']['videoId']


	data2 =   {
    'snippet': {
      'playlistId': p_id, 
      'resourceId': {
          'kind': 'youtube#video',
          'videoId': v_id
        },
     'position': '0'
      }
   }

	w = requests.post('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet' , headers = headers , data=json.dumps(data2))



	return HttpResponse(q.text)

# https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=33704938095-g3uhslf1enbgg84hb40k0924mgea5arm.apps.googleusercontent.com&redirect_uri=https://djme.herokuapp.com/home&scope=https://www.googleapis.com/auth/youtube
@csrf_exempt
def details_saver(request):
	

	try:
		########################### EITHER YOU WILL HAVE YOUR POST REQUEST DATA IN REQUEST.BODY AND REQUEST.POST FROM WHERE YOU CAN PARSE it #######
		x = json.loads(request.body)
		print json.loads(request.body)
		a = user.objects.get_or_create(hostname = x['hostname'])[0]
		a.hotspot = x['hotspot']
		a.save()

		u = v.djsessions_set.get_or_create()[0]

		u.hostedsession = x['hostedsession']
		u.save()

			
	except Exception as e:
		print e
		return HttpResponse("some error")
	return HttpResponse("Post Succcessful")

@csrf_exempt
def songs_saver(request):
	# Create your views here.


	try:
		########################### EITHER YOU WILL HAVE YOUR POST REQUEST DATA IN REQUEST.BODY AND REQUEST.POST FROM WHERE YOU CAN PARSE it #######
		x = json.loads(request.body)

		print json.loads(request.body)
		f = djsessions.objects.get(hostedsession = x['hostedsession'])
		for i in x['songs']:
			print i 
			

			u = f.hostsong_set.get_or_create(song = i)[0]
			u.song = i
			u.counter = str(int(u.counter) + 1)
			u.save()
		aa = djsessions.objects.all().filter(hostedsession=x['hostedsession'])
		songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter')
		for i in songSorted:
			z = i.song.replace(" ", "+")
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain' , "Authorization": "Bearer " + z}
			s = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&q= '+ z +'&type=video&videoDefinition=high' , headers = headers )
			songs  = json.loads(s.text)
			v_id  = songs['items'][0]['id']['videoId']


			data2 =   {
		    'snippet': {
		      'playlistId': p_id, 
		      'resourceId': {
		          'kind': 'youtube#video',
		          'videoId': v_id
		        },
		     'position': '0'
		      }
		   }

			w = requests.post('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet' , headers = headers , data=json.dumps(data2))






			
	except Exception as e:
		print e
		return HttpResponse("some error")
	return HttpResponse("Post Succcessful")




def song(request):
	# aa = djsessions.objects.all().filter(hostedsession=foo)
	# songSorted = hostsong.objects.all().filter(hostedsession=aa).order_by('counter').reverse
	data2  = {'hostedsession' : 'vishrut1' , 'songs'  : [ 'shape of you' , 'down' , 'one time']}
	w = requests.post('http://127.0.0.1:8000/song_saver' ,  data=json.dumps(data2))
	return HttpResponse("done")
