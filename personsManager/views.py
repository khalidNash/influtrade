from django.shortcuts import render, redirect  
from personsManager.forms import ContactForm  
from personsManager.models import Contact 
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import Http404
# Create your views here.

def emp(request):  
    if request.method == "POST":  
        form = ContactForm(request.POST)
        print(form)  
        if form.is_valid():  
            try: 
                form.save() 
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ContactForm()  
    return render(request,'index.html',{'form':form})  
def show(request):
    print("hello i have reached on get all")
    cache_key = 'onekey' # needs to be unique
    cache_time = 60*3 # time in seconds for cache to be valid
    contacts = cache.get(cache_key)
    print(contacts) # returns None if no key-value pair
    if not contacts:
        try:
            contacts = Contact.objects.all()
            cache.set(cache_key, contacts, cache_time)
            print("set the key")
        except Contact.DoesNotExist:
            raise Http404("Contact does not exist")
    list1 = []
    for elements in contacts:
        print(elements.age)
        list1.append(elements.age)
        print(list1)
    print(contacts)
    return render(request,"show.html",{'employees':contacts,'list':list1})  
def edit(request, id): 
    print("hello i have reached on edit all")  
    contact = Contact.objects.get(id=id)  
    return render(request,'edit.html', {'contact':contact})  
def update(request, id):
    print("hello i have updated here")   
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': contact})  
def destroy(request, id): 
    print("hello i have reached here") 
    contact = Contact.objects.get(id=id) 
    print(contact)  
    contact.delete()  
    return redirect("/show")  