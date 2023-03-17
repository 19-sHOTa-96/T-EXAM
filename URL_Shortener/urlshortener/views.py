from django.shortcuts import render, redirect
from django.http import HttpResponse
from hashids import Hashids
from .models import RandomUrl, CustomUrl

hashids = Hashids(min_length=6)

"""
ADMIN-PANEL
user: admin
password: admin
"""

# Home
def home(request):
	return render(request, 'urlshortener/home.html')


# Random
def random_shortener(request):
	random_default = 'Enter URL'

	host = f"http://{request.META.get('HTTP_HOST')}/"

	if request.method == 'POST':
		url_model_object = RandomUrl(random_url_name=request.POST['shortened-url'])
		url_model_object.save()

		random_default = host + 'r/' + hashids.encode(url_model_object.id)
		print('ABSOLUTE-URL', request.build_absolute_uri())

	context = {
				'random_default': random_default,
				}

	return render(request, 'urlshortener/random.html', context)


def random_shortened(request, urlid):
	url_id = hashids.decode(urlid)
	if url_id:
		url = RandomUrl.objects.get(id=url_id[0])
		return redirect(url.random_url_name)

	else:	
		return redirect('random_shortener')


# Custom
def custom_shortener(request):
	custom_default = 'Enter Custom Name'

	host = f"http://{request.META.get('HTTP_HOST')}/"

	if request.method == 'POST':
		original_url = request.POST['original-url']
		custom_name = request.POST['custom-name']

		url_model_object = CustomUrl(original_url_name=original_url, custom_url_name=custom_name)
		url_model_object.save()

		custom_default = host + 'c/' + url_model_object.custom_url_name

	context = {'custom_default': custom_default}
	return render(request, 'urlshortener/custom.html', context)


def custom_shortened(request, custom_name):
	if custom_name:
		url = CustomUrl.objects.filter(custom_url_name=custom_name)
		return redirect(url[0].original_url_name)

	else:
		return redirect('custom_shortener')	

