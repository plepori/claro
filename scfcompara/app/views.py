from django.shortcuts import render
from bs4 import BeautifulSoup
from django.views import View
from django.core.files.storage import FileSystemStorage
from app.funcion import *


class home(View):
    def get(self,request):
        return render(request, 'home.html') 
    
    def post(sefl,request):
        try:
            myfile = request.FILES['myfile']
            myfile2 = request.FILES['myfile2']
        except:
            return render(request,"home.html")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile) 
        filename2 = fs.save(myfile2.name, myfile2)

        
        with open(filename,"r") as page:
            plan = BeautifulSoup(page,'xml',from_encoding='utf-8')
        with open(filename2,"r") as page:
            plan2 = BeautifulSoup(page,'xml',from_encoding='utf-8')        
        
        fs.delete(filename) 
        fs.delete(filename2)

        scf = datos(plan)
        info = scf.ipif()
        port = scf.puertos()

        scf2 = datos(plan2)
        info2 = scf2.ipif()
        port2 = scf2.puertos()

        
        return render(request, "home.html", {"info":info, "info2":info2, "port":port, "port2":port2})
