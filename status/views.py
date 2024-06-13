from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import computers
from .forms import *

# Create your views here.


@login_required()
def home(request):
    return render(request,'computer/base.html')
@login_required
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
        return redirect("display")
    return render(request,'computer/front.html',cs)
@login_required
def display(request):
    details={
        'details':computers.objects.all()
    }
    return render(request,'computer/display.html',details)

@login_required
def base(request):
    return render(request,'computer/base.html')

@login_required
def complaint(request,pk):
    computer = get_object_or_404(computers, pk=pk)
    
    if request.method == "POST":
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('details')  # or wherever you want to redirect after a successful edit
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'computer/complaint.html', {'form': form})

@login_required
def submit(request):
    if request.method=="POST":
        status_list=request.POST.getlist('status')
        for label_status in status_list:
            c_label,status=label_status.split('_')
        computers.objects.filter(c_label=c_label).update(status=status)
    return render(request,'computer/complaint.html')
@login_required
def edit_computer(request, computer_id):
    computer = get_object_or_404(computers, id=computer_id)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('computer_detail', computer_id=computer.id)
    else:
        form =ComputerForm(instance=computer)
    return render(request, 'computer/edit_computer.html', {'form': form})

    
@login_required
def edit_computer(request, pk):
    computer = get_object_or_404(computers, pk=pk)
    
    if request.method == "POST":
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('display')  # or wherever you want to redirect after a successful edit
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'computer/edit_computer.html', {'form': form})
    

@login_required
def report(request):
    cpu_filter = request.GET.get('cpu')
    status_filter = request.GET.get('status')
    lab_filter = request.GET.get('lab')
    mb_filter = request.GET.get('mb')

    computers_queryset = computers.objects.all()

    if cpu_filter:
        computers_queryset = computers_queryset.filter(cpu__cpu_id=cpu_filter)
    if status_filter:
        computers_queryset = computers_queryset.filter(status=status_filter)
    if lab_filter:
        computers_queryset = computers_queryset.filter(lab__lab_id=lab_filter)
    if mb_filter:
        computers_queryset = computers_queryset.filter(mb__mb_id=mb_filter)

    context = {
        'details': computers_queryset,
        'cpu_types': cpu_types.objects.all(),
        'lab_types': lab.objects.all(),  # Corrected the context key to 'lab_types'
        'mb_types': motherboard_type.objects.all(),  # Corrected the context key to 'mb_types'
        'statuses':  computers.objects.values_list('status', flat=True).distinct(),
    }
    
    return render(request, 'computer/report.html', context)
@login_required
def lab_selection(request):
    return render(request, 'computer/lab_selection.html')
@login_required
def complaint_report(request):
    details={
        'details':computers.objects.all()
    }
    return render(request,'computer/complaint_report.html',details)





