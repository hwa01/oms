from django.shortcuts import render
from django.http import HttpResponse
import os
import commands
# Create your views here.

def index(request):
    return render(request, 'play.html')

def execute(request):
	#a = request.GET['a']
	#type = request.GET.get('type',None)
	#server = request.GET.get('server',None)
	#branch = request.GET.get('branch',None)
	#scriptpath = request.GET.get('scriptpath',None)
	#callback = simplejson.loads(request.raw_post_data)
	#callback ="";
	#if request.is_ajax() and request.method == 'POST':
	#	for key in request.POST:
	#		print key
	#		callback = request.POST.getlist(key)
	#		print callback
	#	return HttpResponse(callback)
	#print callback
	#return render(request,'play.html',{'callback':callback})
	
			
	type = request.POST.get('type',None)
	server = request.POST.get('server',None)
	branch = request.POST.get('branch',None)
	
	
	(status,output) = runShell(type,server,branch)
	#saverecord()
	
		
	return HttpResponse(status,output)
	
	
def runShell(type,server,branch):
	os.environ['type']=str(type)
	os.environ['server']=str(server)
	os.environ['branch']=str(branch)
	(status,output) =commands.getstatusoutput('bash'+'  /home/hw/Desktop/django/test.sh $type $server $branch')

	return status,output
	
def saverecord():
	
	print aaa
	
	
	
	
	