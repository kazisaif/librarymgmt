from django.shortcuts import render,redirect

from django.contrib.auth import login,logout,authenticate
from .models import LoginForm,UserInfoForm, books,bookissue
from django.contrib import messages as m
from .form import BooksForm, BooksIssueForm
from django.contrib.auth.models import User

import datetime
#from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    blist=books.objects.all()
    context={'blist':blist}
    return render(request,"home.html",context)

####### Book Section ############

def add_book(request):
    if request.method=="POST":
        bookid=request.POST.get('bookid')
        bookname=request.POST.get('bookname')
        book_author=request.POST.get('bookauthor')
        publish_date=request.POST.get('publishdate')
        bookdescription=request.POST.get('bookdescription')
        bookimage=request.FILES.get('bookimage')

        bs=books()
        bs.bookid=bookid
        bs.bookname=bookname
        bs.book_author=book_author
        bs.publish_date=publish_date
        bs.book_description=bookdescription
        bs.book_image=bookimage
        bs.save()
        
        return redirect('/home')
    
    else:
        m.error(request,'Try Again...')
        return render(request,'addbook.html')

def book_details(request,id):
    bid=books.objects.get(id=id)
    bl=books.objects.filter(bookid=bid)
    context={'bookdetails':bl}
    return render(request,"bookdetails.html",context)

def book_search(request):
    #uid=request.session.get("uid")
    srch=request.POST.get("search")
    bsearch=books.objects.filter(bookname__contains=srch)
    
    context={'blist':bsearch}
    return render(request,"home.html",context)
    #return render(request,"booksearchlist.html",context)

def booklist(request):
    blist=books.objects.all()
    context={'blist':blist}
    #context={'form':f,'mlist':mlist} 
    return render(request,'booklist.html',context)

def booksissue(request,id):
    uid=request.session.get("uid")
    
    if request.method=="POST":
        if request.user.is_authenticated:
        
            bid=request.POST.get("bid")
            #bookid=request.POST.get("bookid")
            #bookname=request.POST.get("bookname")
            #bookauthor=request.POST.get("bookauthor")
            #publishdate=request.POST.get("publishdate")
            #s=Movies.objects.filter(movieid=chkid).exists()
            bi=bookissue()
            bi.book=books.objects.get(id=bid)
            #bi.bookname=bookname
            #bi.book_author=bookauthor
            #bi.publish_date=publishdate
            bi.issuedate=datetime.datetime.now()
            
            bi.user=User.objects.get(id=uid)
            #bi.user=UserInfoForm.objects.get(id=uid)

            bi.save()
            bis=bookissue.objects.filter(user=uid).order_by("-id")
            context={"booksissued":bis}
            return redirect("/booksissued")
            #return render(request,'booksissued.html',context)
        
        else:
            m.info(request,'Please login to issue book')
            f=LoginForm
            context={'form':f}
            return render(request,"login.html",context)
    
    else:
        #bt=BooksIssueForm()
        bid=books.objects.get(id=id)
        bl=books.objects.filter(bookid=bid)
        #context={'form':bt,}
        context={'bookdetails':bl}
        return render(request,'bookdetails.html',context)

def books_issued(request):
    uid=request.session.get("uid")
    
    #inclist=bookticket.objects.filter(user=uid)
    #context={'incl':inclist}
    #sb=bookticket.objects.all().order_by("-id")
    bi=bookissue.objects.filter(user=uid).order_by("-id")
    #b=books.objects.all()
    context={"booksissued":bi}
    return render(request,"booksissued.html",context)

def edit_book(request,id):
    bid=books.objects.get(id=id)
    
    if request.method=='POST':
        f=BooksForm(request.POST,request.FILES,instance=bid)
        f.save()
        #return render(request,'movielist.html')
        return redirect("/booklist")
    else:
        #m.error(request,'Try Again...')
        f=BooksForm(instance=bid)
        context={'form':f}
        return render(request,"editbook.html",context)


def return_book(request,id):
    uid=request.session.get("uid")
    
    if request.user.is_authenticated:
        bid=bookissue.objects.get(id=id)
        
        b=bookissue.objects.filter(id=id).update(returndate=datetime.datetime.now())
        #b.returndate=datetime.datetime.now()
        #b.save()
        
        #bi.save()
        
        bis=bookissue.objects.filter(user=uid).order_by("-id")
        context={"booksissued":bis}
        return redirect("/booksissued")
        
    else:
        m.info(request,'Please login to return book')
        f=LoginForm
        context={'form':f}
        return render(request,"login.html",context)
    

def delete_book(request,id):
    bid=books.objects.get(id=id)
    bid.delete()
    return redirect("/booklist")

#### User Section ########

def adduserform(request):
    return render(request,"adduser.html")

def add_user(request):
    
    if request.method=="POST":

        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        if User.objects.filter(email = email).first():
            m.warning(request, "Email already exists")
            return redirect('/adduserform')
        contact=request.POST.get('contact')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 != password2:
            m.error(request, "Passwords do not match")
            return redirect('/adduserform')
        uf=UserInfoForm()
        
        uf.username=username
        uf.first_name=first_name
        uf.last_name=last_name
        uf.email=email
        uf.contact=contact
        uf.age=age
        uf.gender=gender
        uf.address=address
        uf.password1=password1
        uf.password2=password2
        uf.set_password(password1)
        #uf.check_password=password2
        #uf.password1=password1
        #uf.password2=password2

        uf.save()
        return redirect('/')
    
    else:
        uf=UserInfoForm()
        context={'form':uf}
        return render(request,'adduser.html',context)


def login_view(request):
    if request.method=='POST':  
        #uname=request.POST.get("username")
        #passw=request.POST.get("password") 
        email=request.POST.get("username")
        password=request.POST.get("password")
        username = User.objects.get(email=email.lower()).username  #for email login
        user = authenticate(username=username, password=password)
        #user=authenticate(request,username=uname,password=passw) #need to work on
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            return redirect("/home")
        else: 
            m.error(request,'Invalid Username and Password')
            return redirect('/login')
    else:
        #m.error(request,'Invalid Credentials')
        f=LoginForm
        context={'form':f}
        return render(request,"login.html",context)


def logout_view(request):
    logout(request)
    return redirect("/")