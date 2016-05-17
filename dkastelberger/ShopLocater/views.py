from django.shortcuts import render,  get_object_or_404
from django.contrib.auth import authenticate, login,  logout
from django.http import HttpResponse,  HttpResponseRedirect
from Locator import settings
from django.contrib.auth.decorators import login_required
from .models import Task
from rest_framework import viewsets
from .Serializers import TaskSerializers
from .forms import ShopForm
from django.shortcuts import redirect,  render_to_response
from django.template import RequestContext

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index/login.html", {'redirect_to': next})
    
@login_required
def Home(request):
    form = ShopForm()
    if request.POST:
        form = ShopForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            if request.FILES == 'pictures':
                instance = Task(pictures=request.FILES['pictures'])
                instance.save()
    #return redirect('/home/')
    return render_to_response('home.html', {
    'form': form
    }, context_instance=RequestContext(request))
    
def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)
    

def Blog(request):
    #return render(request, "index/blog.html", {})
    shops = Task.objects.all()
    return render_to_response('blog.html',  {'shops': shops}, context_instance=RequestContext(request))
    
def Detail(request,  id):
    shop = get_object_or_404(Task,  id=id)
    return render_to_response('detail.html',  {'shop': shop}, context_instance=RequestContext(request))

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers
