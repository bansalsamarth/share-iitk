from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

import dropbox
from share.models import FileData

"""app_key = '4z2auu2o4v1ms76'
app_secret = '8c29694u73eb515'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()
code = 'P870X6WAn0cAAAAAAAASdK9LmT_Vrd_md9OhhcPwhYI'
access_token, user_id = flow.finish(code)"""

token = 'P870X6WAn0cAAAAAAAASc3c-hsgqIOsdo5crALuuL5e6dyMffAyCznBJjvz9Cp1r'

client = dropbox.client.DropboxClient('P870X6WAn0cAAAAAAAASc3c-hsgqIOsdo5crALuuL5e6dyMffAyCznBJjvz9Cp1r')
#print client.account_info()
#response = client.put_file('/magnum-opus.txt', f)
MAX_UPLOAD_SIZE = 5242880

def upload_page(request):
	#return HttpResponse("upload page")
	return render_to_response('upload.html', {}, context_instance = RequestContext(request))

def about(request):
	return render_to_response('about.html', {}, context_instance = RequestContext(request))

def landing(request):
	return render_to_response('landing.html', {}, context_instance = RequestContext(request))

def contact(request):
	return render_to_response('contact.html', {}, context_instance = RequestContext(request))

def home(request):
	file_list = FileData.objects.filter(approved = 'Y')
	return render_to_response('index.html', {'list':file_list}, context_instance = RequestContext(request))

def moderator(request):
	file_list = FileData.objects.filter(approved = 'N')
	return render_to_response('index.html', {'list':file_list}, context_instance = RequestContext(request))

def file_submit(request):
	if request.method == "POST":
		#return HttpResponse(request.POST)
		course_name = request.POST['course-name']
		department_code = request.POST['dept']
		course_code = request.POST['course-code']
		category = request.POST['category']
		f = request.FILES['file']
		if len(f) > 5242880:
			return render_to_response('upload.html', {'error': 'File should be under 5 MB'}, context_instance = RequestContext(request))		
		name = '/'+f.name 
		response = client.put_file(name, f)
		url = dropbox.client.DropboxClient(token).share(name)
		url = url['url']
		#url = 'a'
		a = FileData(course_name = course_name, department_code = department_code, course_code = course_code, category = category, file_url = url)

		if request.POST['year']!='':
			a.year = int(request.POST['year'])

		"""if request.POST['prof']!='':
			a.year = request.POST['prof']"""

		"""if request.POST['description']!='':
			a.year = request.POST['description']"""

		a.save()
		return render_to_response('upload.html', {'success':'Thanks. File would be availabe after admin approval'}, context_instance = RequestContext(request))
