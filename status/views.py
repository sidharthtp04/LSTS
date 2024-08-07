from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import computers
from .forms import *
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .decorators import group_required
# Create your views here.


@login_required()
@group_required('li')
def home_report(request):
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


@login_required()
@group_required('li')
def home(request):
    return render(request,'computer/home.html')

@login_required
@group_required('li')
def computer(request):
    cs = {
        'lab': lab.objects.all(),
        'cpu': cpu_types.objects.all(),
        'motherboard': motherboard_type.objects.all(),
        'ram': ram_type.objects.all(),
        'storage': storage_type.objects.all(),
        'smps': smps.objects.all(),
        'keyboard': keyboard.objects.all(),
        'mouse': mouse.objects.all(),
        'monitor': monitor.objects.all()
    }
    
    if request.method == "POST":
        clabel = request.POST.get('clabel')
        dop = request.POST.get('dop')
        status = request.POST.get('status')
        invoice_no = request.POST.get('invoice_no')
        os_type = request.POST.get('os_type')
        
        labe_id = request.POST.get('lab')
        cpue_id = request.POST.get('cpu')
        mbe_id = request.POST.get('mb')
        smpse_id = request.POST.get('smps')
        rame_id = request.POST.get('ram')
        storagee_id = request.POST.get('storage')
        keyboarde_id = request.POST.get('keyboard')
        mousee_id = request.POST.get('mouse')
        monitore_id = request.POST.get('monitor')
        
        labe = lab.objects.get(lab_id=labe_id)
        cpue = cpu_types.objects.get(cpu_id=cpue_id)
        mbe = motherboard_type.objects.get(mb_id=mbe_id)
        smpse = smps.objects.get(smps_id=smpse_id)
        rame = ram_type.objects.get(ram_id=rame_id)
        storagee = storage_type.objects.get(storage_id=storagee_id)
        keyboarde = keyboard.objects.get(keyboard_id=keyboarde_id)
        mousee = mouse.objects.get(mouse_id=mousee_id)
        monitore = monitor.objects.get(monitor_id=monitore_id)
        
        comp = computers(
            c_label=clabel,
            lab=labe,
            cpu=cpue,
            ram=rame,
            storage=storagee,
            dop=dop,
            status=status,
            invoice_no=invoice_no,
            os_type=os_type,
            mb=mbe,
            smps=smpse,
            keyboard=keyboarde,
            mouse=mousee,
            monitor=monitore
        )
        comp.save()
        return redirect("display")
    
    return render(request, 'computer/front.html', cs)

@login_required
@group_required('li')
def display(request):

    filtered_computers = computers.objects.exclude(status='TRASHED')
    details={
        'details':filtered_computers
    }
    return render(request,'computer/display.html',details)


@login_required
@group_required('li')
def trashed_computers(request):
    trashed_computers = computers.objects.filter(status='TRASHED')
    details = {
        'details': trashed_computers
    }
    return render(request, 'computer/trashed_computers.html', details)

@login_required
@group_required('li')
def computer_complaint_report(request, computer_id):
    computer = get_object_or_404(computers, c_id=computer_id)
    complaints = Complaint.objects.filter(computer=computer)
    
    context = {
        'computer': computer,
        'complaints': complaints
    }
    
    if not complaints:
        context['no_complaints'] = True
    
    return render(request, 'computer/computer_complaint.html', context)

@login_required
@group_required('li')
def base(request):
    return render(request,'computer/base.html')

@login_required
@group_required('li')
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
@group_required('li')
def submit(request):
    if request.method=="POST":
        status_list=request.POST.getlist('status')
        for label_status in status_list:
            c_label,status=label_status.split('_')
        computers.objects.filter(c_label=c_label).update(status=status)
    return render(request,'computer/complaint.html')

    
@login_required
@group_required('li')
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
    storage_filter = request.GET.get('storage')
    ram_filter = request.GET.get('ram')

    computers_queryset = computers.objects.all()

    if cpu_filter:
        computers_queryset = computers_queryset.filter(cpu__cpu_id=cpu_filter)
    if status_filter:
        computers_queryset = computers_queryset.filter(status=status_filter)
    if lab_filter:
        computers_queryset = computers_queryset.filter(lab__lab_id=lab_filter)
    if mb_filter:
        computers_queryset = computers_queryset.filter(mb__mb_id=mb_filter)
    if storage_filter:
        computers_queryset = computers_queryset.filter(storage__storage_id=storage_filter)
    if ram_filter:
        computers_queryset = computers_queryset.filter(ram__ram_id=ram_filter)

    context = {
        'details': computers_queryset,
        'cpu_types': cpu_types.objects.all(),
        'lab_types': lab.objects.all(),
        'mb_types': motherboard_type.objects.all(),
        'storage_types': storage_type.objects.all(),
        'ram_types': ram_type.objects.all(),
        'statuses': computers.objects.values_list('status', flat=True).distinct(),
    }

    return render(request, 'computer/report.html', context)

@login_required
@group_required('li')
def lab_selection(request):
    return render(request, 'computer/lab_selection.html')


@login_required
@group_required('li')
def complaint_report(request):
    # Get the filter value from the GET parameters
    status_filter = request.GET.get('status', 'all')
    
    filtered_computers = computers.objects.exclude(status='TRASHED')

    details = {
        'details': filtered_computers,
        'status_filter': status_filter  # Pass the current filter value to the template
    }
    
    return render(request, 'computer/complaint_report.html', details)

@login_required
@group_required('li')
def change_status_to_trashed(request, computer_id):
    computer = get_object_or_404(computers, pk=computer_id)
    computer.status = 'TRASHED'
    computer.save()
    return redirect('display')

@login_required
@group_required('li')
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
@group_required('li')
def report_generation(request):
    complaints = Complaint.objects.select_related('computer').all()
    repairs = Repair.objects.select_related('complaint').all()

    # Create a dictionary mapping complaint IDs to repairs
    repairs_dict = {repair.complaint_id: repair for repair in repairs}
    form = ComplaintFilterForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data['c_label']:
            complaints = complaints.filter(computer__c_label=form.cleaned_data['c_label'])
        if form.cleaned_data['lab_name']:
            complaints = complaints.filter(computer__lab__lab_name=form.cleaned_data['lab_name'])

    # Create a list of dictionaries that combine complaints and repairs
    combined_data = []
    for complaint in complaints:
        data = {
            'computer_label': complaint.computer.c_label,
            'lab_name': complaint.computer.lab.lab_name,
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
        'form': form,
        'complaints': complaints,
        'repairs': repairs,
    }
    return render(request, 'computer/report_generation.html', context)



def first_page(request):
    cpu_filter = request.GET.get('cpu')
    status_filter = request.GET.get('status')
    lab_filter = request.GET.get('lab')
    mb_filter = request.GET.get('mb')

    computers_queryset = computers.objects.all()

    if cpu_filter:
        computers_queryset = computers_queryset.filter(cpu__make=cpu_filter)
    if status_filter:
        computers_queryset = computers_queryset.filter(status=status_filter)
    if lab_filter:
        computers_queryset = computers_queryset.filter(lab__lab_id=lab_filter)
    if mb_filter:
        computers_queryset = computers_queryset.filter(mb__mb_socket_type=mb_filter)

    context = {
        'details': computers_queryset,
        'cpu_types': cpu_types.objects.all(),
        'lab_types': lab.objects.all(),
        'mb_types': motherboard_type.objects.all(),
        'statuses':  computers.objects.values_list('status', flat=True).distinct(),
    }

    return render(request, 'computer/firstpage.html', context)
