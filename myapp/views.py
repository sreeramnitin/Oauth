# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import urllib2
import urllib
import json
client_id="MgPENXXEuGu1lfDTx0U5lJUg7iHGZv3GuKTaoGeE1jiWG15d0j"
client_secret="r7StDRUU6AU0AwVhiz3M6nsTP3mtpesUTFJYwkI8593TK1f4ES"
def index(request):
	return render_to_response('index.html')
def auth(request):
	client_id=request.POST['client_id']
	client_secret=request.POST['client_secret']
	return redirect('http://join.agiliq.com/oauth/authorize?client_id='+client_id+'&redirect_uri=http://localhost:8000/agiliq')
def agiliq(request):
	#return HttpResponse(request.GET['code'])
	code = request.GET['code']
	url = 'http://join.agiliq.com/oauth/access_token?'
	values = {'client_id' : client_id,
			  'redirect_uri' : 'http://localhost:8000/agiliq',
			  'client_secret' : client_secret,
			  'code': code,}
	#return HttpResponse(client_secret)
	#data = urllib.urlencode(values)
	req = urllib2.Request(url+urllib.urlencode(values))
	response = urllib2.urlopen(req)
	the_page = response.read()
	obj = json.loads(the_page)
	token=obj['access_token']
	return render_to_response('inp.html', {
            'access_token': token,
        },)