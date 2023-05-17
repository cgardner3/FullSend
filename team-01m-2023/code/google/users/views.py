from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
from .models import Contact, Post, FilesUpload, Comment, Matches
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, "home.html")

def main(request): 
	#uploading profile info code changes
	if request.method=="POST":
		profInfo=Post()
		#pfp=request.POST.get('pfp')
		#file1=request.FILES['file']
		name=request.POST.get('name')
		pron=request.POST.get('pron')
		desc=request.POST.get('desc')
		gymLocations=request.POST.getlist('checks[]')
		climbType=request.POST.getlist('checks1[]')
		expLevel=request.POST.get('experience')
		availability=request.POST.getlist('checks2[]')
		username=request.POST.get('username')
		#skills=request.POST.get('skills')
		#profInfo.pfp=pfp
		#profInfo.file=file2
		profInfo.name=name
		profInfo.pron=pron
		profInfo.desc=desc
		profInfo.gymLocations=gymLocations
		profInfo.climbType=climbType
		profInfo.expLevel=expLevel
		profInfo.availability=availability
		profInfo.username=username
		#profInfo.skills=skills
		profInfo.save()
		return redirect('/discovery/')
	else:
		return render(request, "main.html")

def discovery(request):
	user_list = Post.objects.all()
	return render(request, "discovery.html",
	       {'user_list': user_list})
	#return render(request, "discovery.html")

def matches(request):
	if request.method == "POST":
		match1=Matches()
		user=request.POST.get('user')
		match=request.POST.getlist('match')
		match1.user = user
		match1.matches = match
		match1.save()
		return redirect('/message/')
	else: 
		matches_list = Post.objects.all()
		return render (request, "matches.html",
		 		{'matches_list': matches_list})

def message(request):
	if request.method=="POST":
		comment=Comment()
		name=request.POST.get('name')
		subject=request.POST.get('subject')
		comment.name=name
		comment.subject=subject
		comment.save()
		return redirect('/message/')
	else: 
		comment_list = Comment.objects.all()
		return render (request, "messages.html",
		 		{'comment_list': comment_list})

def settings(request):
	if request.method=="POST":
		contact=Contact()
		name=request.POST.get('name')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		contact.name=name
		contact.email=email
		contact.subject=subject
		contact.save()
		return render(request, "thankyou.html")
	else: 
		return render(request, "settings.html")

def thanks(request):
	return render(request, "thankyou.html")

def signup(request):
	return render(request, "signup.html")

def logout_view(request):
	logout(request)
	return redirect("/")

