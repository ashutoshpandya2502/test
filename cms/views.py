from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import SignUpForm
from .models import Client,Agent
from django.views.generic import TemplateView
"""this functions is used to for home page"""
def index(request):
	return render(request,'cms/index.html')
"""this functions is used to show about us page on main web"""
def about_us(request):
	return render(request,'cms/about_us.html')
"""this functions is used for signup of agent in web"""
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the agent instance created by the signal
			user.agent.first_name = form.cleaned_data.get('first_name')
			user.agent.last_name = form.cleaned_data.get('last_name')
			user.agent.email =form.cleaned_data.get('email')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			client_object_list = Client.objects.filter(agent=user.agent)
			return render(request,'cms/show_client_list.html',{'client_object_list':client_object_list,'agent_id':user.agent.id})
	else:
		form = SignUpForm()
	return render(request, 'cms/signup.html', {'form': form})
"""this functions is used for login agent on web"""
def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None :
			login(request,user)
			client_object_list = Client.objects.filter(agent=user.agent)
			return render(request,'cms/show_client_list.html',{'client_object_list':client_object_list,'agent_id':user.agent.id})
	return render(request,'cms/login.html')

"""this functions is used for showing client edit option in add client"""
def show_client_edit(request,agent_id):
	return render(request,'cms/add_client.html',{'agent_id':agent_id})

"""this functions is used to add client and agent_id is keyword argument here"""
def add_client(request,agent_id):
	if request.method == 'POST':
		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		address = request.POST.get('address')
		agent_object=Agent.objects.get(id=agent_id)
		Client.objects.create(first_name=first_name,last_name=last_name,address=address,agent=agent_object)
		client_object_list = Client.objects.filter(agent=agent_object)
		return render(request,'cms/show_client_list.html',{'client_object_list':client_object_list,'agent_id':agent_id})


