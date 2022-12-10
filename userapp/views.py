from django.shortcuts import render,redirect
from . models import reg_tbl,choco_tbl

# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=='POST':
        fna = request.POST.get('nm')
        mbl = request.POST.get('mb')
        eml = request.POST.get('em')
        psw = request.POST.get('ps')
        obj=reg_tbl.objects.create(fn=fna,mb=mbl,em=eml,ps=psw)
        obj.save()
        if obj:
            return render(request,"login.html")
        else:
            return render(request,"reg.html")
    else:
        return render(request,"reg.html")
def login(request):
    if request.method=='POST':
        eml=request.POST.get('em')
        psw=request.POST.get('ps') 
        obj=reg_tbl.objects.filter(em=eml,ps=psw)
        if obj:
            request.session['ema']=eml
            request.session['psa']=psw
            return render(request,"home.html")
        else:
            msg="Invalid Email id and password!.."
            request.session['ema']=''
            request.session['psa']=''
            return render(request,"login.html",{"error":msg})
    else:
        return render(request,"login.html")
def details(request):
    obj=reg_tbl.objects.all()
    return render(request,"details.html",{"data":obj})
def edit(request):
    idno=request.GET.get('idn')
    obj=reg_tbl.objects.filter(id=idno)
    return render(request,"details2.html",{"data":obj})
def update(request):
    if request.method=='POST':
        nma=request.POST.get('nm')
        mbl=request.POST.get('mb')
        ema=request.POST.get('em')
        psw=request.POST.get('ps')
        idl=request.POST.get('idno')
        obj=reg_tbl.objects.get(id=idl)
        obj.fn=nma
        obj.mb=mbl
        obj.em=ema
        obj.ps=psw
        obj.save()
        return redirect("/details")
    return render(request,"details2.html")
def delete(request):
    idno=request.GET.get('idn')
    obj=reg_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect("/details")
def chocoupload(request):
    if request.method=='POST':
        chnm=request.POST.get('cn')
        chpic=request.FILES.get('ch')
        chpr=request.POST.get('cp')
        obj=choco_tbl.objects.create(cnm=chnm,cpic=chpic,cprc=chpr)
        obj.save()
        if obj:
            msg="File Uploaded Successfully"
            return render(request,"chocoupload.html",{"success":msg})
        else:
            return render(request,"chocoupload.html")
    else:
        return render(request,"chocoupload.html")
def chocoview(request):
    obj=choco_tbl.objects.all()
    return render(request,"chocoview.html",{"view":obj})
        
            
        
            
            
        
            
                               
        

    