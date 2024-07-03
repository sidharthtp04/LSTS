from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import computers
from .forms import *
from django.contrib import messages
from django.utils import timezone

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

def complaint(request, pk):
    computer = get_object_or_404(computers, pk=pk)
    
    # Check if computer status is already 'not working'
    if computer.status == 'not working':
        return redirect('complaint_report')

    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.computer = computer
            complaint.save()

            # Update the computer status to 'not working'
            computer.status = 'not working'
            computer.save()
            print(f"Updated computer {computer.c_label} status to {computer.status}")

            return redirect('report_generation')  # Adjust the redirect as needed
        else:
            print("Form is not valid")
    else:
        form = ComplaintForm(initial={'computer': computer})
    
    return render(request, 'computer/complaint.html', {'form': form, 'computer': computer})


@login_required
def submit(request):
    if request.method=="POST":
        status_list=request.POST.getlist('status')
        for label_status in status_list:
            c_label,status=label_status.split('_')
        computers.objects.filter(c_label=c_label).update(status=status)
    return render(request,'computer/complaint.html')

    
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



@login_required
def repair_detail(request, pk):
    computer = get_object_or_404(computers, pk=pk)
    # Filter complaints with pending repair details and get the latest one
    latest_complaint = Complaint.objects.filter(computer=computer, repair__isnull=True).order_by('-complaint_date').first()

    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.complaint = latest_complaint  # Link the repair to the latest pending complaint
            repair.save()

            # Update computer status and any other necessary logic
            computer.status = 'working'
            computer.save()

            return redirect('report_generation')  # Redirect after successful form submission
    else:
        form = RepairForm(initial={'complaint': latest_complaint})

    context = {
        'computer': computer,
        'latest_complaint': latest_complaint,
        'form': form
    }

    return render(request, 'computer/repair_detail.html', context)
@login_required
def report_generation(request):
    complaints = Complaint.objects.select_related('computer').all()
    repairs = Repair.objects.select_related('complaint').all()

    # Create a dictionary mapping complaint IDs to repairs
    repairs_dict = {repair.complaint_id: repair for repair in repairs}

    # Create a list of dictionaries that combine complaints and repairs
    combined_data = []
    for complaint in complaints:
        data = {
            'computer_label': complaint.computer.c_label,
            'complaint_details': complaint.complaint_details,
            'complaint_date': complaint.complaint_date,
            'repair_reason': repairs_dict[complaint.id].reason if complaint.id in repairs_dict else 'Pending',
            'repair_date': repairs_dict[complaint.id].repair_date if complaint.id in repairs_dict else 'Pending'
        }
        combined_data.append(data)

    if request.method == 'POST':
        if 'complaint_submit' in request.POST:
            complaint_form = ComplaintForm(request.POST)
            if complaint_form.is_valid():
                complaint_form.save()
                return redirect('report_generation')
        elif 'repair_submit' in request.POST:
            repair_form = RepairForm(request.POST)
            if repair_form.is_valid():
                repair_form.save()
                return redirect('report_generation')
    else:
        complaint_form = ComplaintForm()
        repair_form = RepairForm()

    context = {
        'combined_data': combined_data,
        'complaint_form': complaint_form,
        'repair_form': repair_form,
    }
    return render(request, 'computer/report_generation.html', context)
@login_required
def delete_repair(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    complaint = get_object_or_404(Complaint, computer=repair.computer)
    computer = repair.computer

    repair.delete()

    remaining_repairs = Repair.objects.filter(computer=computer).exists()
    if not remaining_repairs:
        computer.status = 'not working'
        computer.save()

    return redirect('report_generation')
@login_required
def delete_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    computer = complaint.computer

    complaint.delete()

    remaining_complaints = Complaint.objects.filter(computer=computer).exists()
    if not remaining_complaints:
        computer.status = 'working'
        computer.save()

    return redirect('report_generation')

@login_required
def new_page(request):
    # Process form submission and filter queryset based on form data
    lab_id = request.GET.get('lab')
    status = request.GET.get('status')

    computers_list = computers.objects.all()  # Use the correct model name 'Computer'

    if lab_id:
        computers_list = computers_list.filter(lab_id=lab_id)

    if status:
        computers_list = computers_list.filter(status=status)

    context = {
        'computers_list': computers_list
    }

    return render(request, 'computer/new.html', context)
