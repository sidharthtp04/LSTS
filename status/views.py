from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return HttpResponse('hello')

def computer(request):
    cs={
        'lab':lab.objects.all(),
        'cpu':cpu_types.objects.all(),
        'motherboard':motherboard_type.objects.all(),
        'ram':ram_type.objects.all(),
        'storage':storage_type.objects.all(),
        'smps':smps.objects.all(),
        'keyboard':keyboard.objects.all(),
        'mouse':mouse.objects.all(),
        'monitor':monitor.objects.all()

    }
    if request.method=="POST":
        clabel=request.POST.get('clabel')
        dop=request.POST.get('dop')
        status=request.POST.get('status')
        invoice_no=request.POST.get('invoice_no')
        os_type=request.POST.get('os_type')
        labe=request.POST.get('lab')
        cpue=request.POST.get('cpu')
        mbe=request.POST.get('mb')
        smpse=request.POST.get('smps')
        rame=request.POST.get('ram')
        storagee=request.POST.get('storage')
        keyboarde=request.POST.get('keyboard')
        mousee=request.POST.get('mouse')
        monitore=request.POST.get('monitor')
        labe=lab.objects.get(lab_id=labe)
        cpue=cpu_types.objects.get(cpu_id=cpue)
        rame=ram_type.objects.get(ram_id=rame)
        storagee=storage_type.objects.get(storage_id=storagee)
        mbe=motherboard_type.objects.get(mb_id=mbe)
        smpse=smps.objects.get(smps_id=smpse)
        keyboarde=keyboard.objects.get(keyboard_id=keyboarde)
        mousee=mouse.objects.get(mouse_id=mousee)
        monitore=monitor.objects.get(monitor_id=monitore)

        comp=computers(c_label=clabel,lab=labe,cpu=cpue,ram=rame,storage=storagee,dop=dop,status=status,invoice_no=invoice_no,os_type=os_type,mb=mbe,smps=smpse,keyboard=keyboarde,mouse=mousee,monitor=monitore)
        comp.save()
    return render(request,'computer/front.html',cs)

def display(request):
    details={
        'details':computers.objects.all()
    }
    return render(request,'computer/display.html',details)
def base(request):
    return render(request,'computer/base.html')
