from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,Http404

from .models import *
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Q
from .form import createForm,registerUser,createauthor,commentForm,Ccategory,postForm,Pcomment,U_about
from  django.contrib import messages
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .token import account_activation_token

# Create your views here.

def index(request):
      if request.user.is_authenticated:
          u = get_object_or_404(author, pk=request.user.id)
          post = article.objects.all()
          cat = category.objects.all()


          context = {
              "post": post,
              "user_p": u,
              "category": cat,


          }
          return render(request, 'index.html', context)
      else:
          return redirect('login')




def search(request):
    if request.method=="POST":
        srch=request.POST['q']

        if srch:
            match=article.objects.filter(Q(title__icontains=srch)| Q (body__icontains=srch))

            if match:
                return render(request,'index.html',{'sr':match})
            else:
             messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'index.html')



def getauthor(request,name):
    post_author=get_object_or_404(User,username=name)
    auth=get_object_or_404(author,name=post_author.id)
    post=article.objects.filter(article_author=auth.id)
    context={
        "auth":auth,
        "post":post,
    }
    return render(request,'profile.html',context)

def getsingle(request,id):
    post=get_object_or_404(article,pk=id)
    first = article.objects.first()
    last = article.objects.last()
    getcomment=comment.objects.filter(post=id)
    related=article.objects.filter(category=post.category).exclude(id=id)[:4]
    form=commentForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=post
        instance.save()

    context={
        "post":post,
        "first": first,
        "last": last,
        "related":related,
        "form":form,
        "comment":getcomment,
    }
    return render(request,'single.html',context)

def getcategory(request,name):
    cat=get_object_or_404(category,name=name)
    post=article.objects.filter(category=cat)
    return render(request,'category.html',{"post":post,"cat":cat})


def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get('user')
            password = request.POST.get('pass')

            auth = authenticate(request, username=user, password=password)

            if auth is not None:
                login(request, auth)
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'username or password is incorrect.')
                return render(request,'login.html')
    return render(request,'login.html')

def getlogout(request):
    logout(request)
    return redirect('login')

def getcreate(request):
    if request.user.is_authenticated:
        u=get_object_or_404(author,name=request.user.id)
        form = createForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=u
            instance.save()
            return redirect('index')
        return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')

def getupdate(request,id):
    if request.user.is_authenticated:
        u=get_object_or_404(author,name=request.user.id)
        post=get_object_or_404(article,id=id)
        form = createForm(request.POST or None, request.FILES or None,instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=u
            instance.save()
            messages.success(request, 'Article update successfully.')
            return redirect('profile')
        return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')

def getdelete(request,id):
    if request.user.is_authenticated:
        post=get_object_or_404(article,id=id)
        post.delete()
        messages.success(request, 'Article delete successfully')
        return redirect('profile')
    else:
        return redirect('login')
def getprofile(request):
    if request.user.is_authenticated:
        user=get_object_or_404(User,id=request.user.id)
        author_profile=author.objects.filter(name=user.id)
        if author_profile:
            authoruser=get_object_or_404(author,name=request.user.id)

            post=article.objects.filter(article_author=authoruser.id)
            return render(request, 'profile10.html',{"post":post,"user":authoruser})
        else:
            form=createauthor(request.POST or None,request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name=user
                instance.save()
                return redirect('profile')
            return render(request,'createauthor.html',{"form":form})
    else:
        return redirect('login')

def getregister(request):
    form=registerUser(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.is_active=False
        instance.save()
        site=get_current_site(request)
        mail_subject="confirmation message for blog."
        message=render_to_string('confirm_email.html',{

            "user":instance,
            "domain":site.domain,
            "uid":instance.id,
            "token":account_activation_token.make_token(instance)

        })
        to_email=form.cleaned_data.get('email')
        to_list=[to_email]
        from_email=settings.EMAIL_HOST_USER
        send_mail(mail_subject,message,from_email,to_list,fail_silently=True)

        return HttpResponse("<h1>Thanks for your Registrations. A confirmation link was sent to your email.</h1>")



    return render(request,'register.html',{"form":form})



def activate(request):
    return render_to_string()





def getTopic(request):
    topic=category.objects.all()
    return render(request,'topic.html',{"topic":topic})

def createCategory(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            form = Ccategory(request.POST or None)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, "category successfully created!")
                return redirect("topic")
            return render(request, "create_topic.html", {"form": form})
        else:
            return HttpResponse("you are not a valid person.")

    else:
        return redirect("login")




def chating(request):
    if request.user.is_authenticated:
        image = post.objects.all().order_by('-id')
        all_user = author.objects.all()
        cat = category.objects.all()
        return render(request, 'instagram.html', {"image": image, "all_user": all_user, "category": cat})
    else:
        return redirect('login')

def create_post(request):
    if request.user.is_authenticated:
        authoruser = get_object_or_404(author, name=request.user.id)
        form=postForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.post_author=authoruser
            instance.save()
            return redirect('chat')
    return render(request,'creat_post.html',{"form":form})


def edit_post(request,id):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        u_post = get_object_or_404(post, id=id)
        form = postForm(request.POST or None, request.FILES or None, instance=u_post)
        if request.user != u_post.id:

            if form.is_valid():
                instance = form.save(commit=False)
                instance.post_author = u
                instance.save()
                messages.success(request, 'post edit successfully.')
                return redirect('chat')
            return render(request, 'creat_post.html', {"form": form})
        else:
            return HttpResponse("you are not edit this post")
    else:
        return redirect('login')

def myprofile(request,id):
    auth=get_object_or_404(author,pk=id)
    all=author.objects.all()
    user_a=About.objects.filter(u_name=auth.id)

    u_post= post.objects.filter(post_author=auth).order_by('-id')

    return render(request,'myprofile.html',{"auth":auth,"u_post":u_post,"all_user":all})



def get_comment(request,id):
    if request.user.is_authenticated:
        g_comment = post_comment.objects.filter(comment=id)
        profile=get_object_or_404(author,pk=id)
        form = Pcomment(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('chat')
        return render(request, 'instagram.html', {"form":form,"comment":g_comment,"pic":profile})
    else:
        return redirect('login')


def maintenence(request):
    return render(request,'maintanence.html')



def user_about(request):
    user = get_object_or_404(author, pk=request.user.id)
    form=U_about(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.u_name=user
        instance.save()
        return redirect('chat')
    return render(request,'about.html',{"form":form})