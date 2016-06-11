from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from account.models import *
from django.views.generic.list import ListView


# Create your views here.
def hello(request, name):
	if not name:
		name = 'world'
	# return HttpResponse(s)

	return render_to_response('t1.html', {'name': name})


class UserListView(ListView):

	template_name = 'userlist.html'
	# context_object_name = 'user_list'
	model = User

	# def get_queryset(self):
	# 	user_list = User.objects.all()
	# 	return user_list
