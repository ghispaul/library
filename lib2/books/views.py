from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from books.models import Book



# Create your views here.
def home(request):
    context={'name':'Adhi','place':'Alapy'}
    return render(request,'home.html',context)

@login_required
def add_book(request):
    if(request.method=='POST'):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa= request.POST['pa']
        l= request.POST['l']

        i=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,pages=pa,price=p,language=l,cover=i,pdf=f)
        b.save()
        return redirect('books:view')
    return render(request, 'add.html')
@login_required
def view_book(request):
    k=Book.objects.all()
    return render(request,'view.html',{'book':k})
@login_required
def detail(request,i):
    k=Book.objects.get(id=i)
    return render(request,'detail.html',{'book':k})
@login_required
def edit(request,p):
    k = Book.objects.get(id=p)
    if(request.method=='POST'):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.page=request.POST['pa']
        k.language=request.POST['l']

        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')

        if (request.FILES.get('f') == None):
            k.save()
        else:
            k.pdf= request.FILES.get('f')
        k.save()
        k = Book.objects.get(id=p)

        return view_book(request)

    return render(request,'edit.html',{'book':k})

@login_required
def delete(request,p):
    k = Book.objects.get(id=p)
    k.delete()
    return redirect('books:view')

from django.db.models import Q
def search(request):
    k=None
    if(request.method=="POST"):
        query=request.POST['q']
        print(query)
        if query:
            k=Book.objects.filter(Q(title__icontains=query) |Q(author__icontains=query))
            print(k)
    return render(request,'search.html',{'book':k})
