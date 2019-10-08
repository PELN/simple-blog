from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

# import models 
from .models import *

# Create your views here.
# give the view function parameter 'request' -  django will send a request to the view
@login_required
def index(request):
# if we get a GET req we should show what we have in the db
# if we get a POST req we should save the item in the db
    if request.method == 'GET':
        # get list of blog items from db - objects.all() will give ALL items in db
        blog_items = BlogItem.objects.filter(user=request.user)
      
        context = {
            'blogs': blog_items
        }
        # use render import  - give the request
        return render(request, 'blogapp/index.html', context)
    
    if request.method == 'POST':
        blog_item = BlogItem()
        blog_item.title = request.POST['title']
        blog_item.post = request.POST['post']
        # blog_item.date = request.POST['date']
        blog_item.user = request.user
        blog_item.save()
        return HttpResponseRedirect(reverse ('blogapp:index'))
    
    # will return a bad requeest to the user - better than sending back a server fault error
    return HttpResponseBadRequest()

@login_required
# convention to call ID for primary key
def details(request, pk):
    # get todo item from database - testing if the user is the one from the request
    blog = get_object_or_404(BlogItem, pk=pk, user=request.user)
    # print(todo.user)
    
    # if a user has clicked on a item-link and goes to the details page
    if request.method == 'GET':
        context = {
            'blog': blog
        }
        # render the template
        return render(request,'blogapp/details.html', context)

    if request.method == 'POST':
        # the user is on details page and hits submit button, get a post request with changes
        blog.title = request.POST.get('title')
        blog.post = request.POST.get('post')
        blog.save()
        # return/redirect to index view
        return HttpResponseRedirect(reverse ('blogapp:index'))

    return HttpResponseBadRequest()


