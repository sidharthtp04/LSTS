from django.db import models

# Create your models here.


class cpu_types(models.Model):
    cpu_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=15)
    generation = models.CharField(max_length=15)
    speed = models.CharField(max_length=15)
    series = models.CharField(max_length=20)
    core_count = models.IntegerField()
    def __str__(self):
        return f"{self.make} {self.series}-{self.generation} CPU @ {self.speed} x {self.core_count}"

class motherboard_type(models.Model):
    mb_id = models.AutoField(primary_key=True)
    mb_socket_type= models.CharField(max_length=15)
    max_ram_capacity = models.CharField(max_length=15)
    make = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.mb_socket_type},{self.max_ram_capacity}GB,{self.make}"
    
class ram_type(models.Model):
    ram_id = models.AutoField(primary_key=True)
    ram_size = models.CharField(max_length=15)
    make = models.CharField(max_length=15)
    speed = models.IntegerField()
    series = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.ram_size} {self.make} {self.speed} {self.series}"
class storage_type(models.Model):
    storage_id = models.AutoField(primary_key=True)
    storage_size= models.CharField(max_length=15)
    make = models.CharField(max_length=15)
    technology = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.storage_size} {self.make} {self.technology}"
class smps(models.Model):
    smps_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=15)
    power = models.IntegerField()
    def __str__(self):
        return f"{self.make} {self.power}"
class keyboard(models.Model):
    keyboard_id =  models.AutoField(primary_key=True)
    make =  models.CharField(max_length=15)
    def __str__(self):
        return f"{self.make}"
class mouse(models.Model):
    mouse_id =  models.AutoField(primary_key=True)
    make =  models.CharField(max_length=15)
    def __str__(self):
        return f"{self.make}"
class monitor(models.Model):
    monitor_id =  models.AutoField(primary_key=True)
    make =  models.CharField(max_length=15)
    size =  models.CharField(max_length=15)
    resolution =  models.CharField(max_length=15)
    def __str__(self):
        return f"{self.make} {self.size} {self.resolution}"
class lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length = 15)
    capacity = models.IntegerField()
    def __str__(self):
        return f"{self.lab_name}"
class programme(models.Model):
    programme_id = models.AutoField(primary_key=True)
    programme_name = models.CharField(max_length=20)

class lab_timetable(models.Model):
    lab = models.ForeignKey(lab,on_delete=models.CASCADE)
    day=models.CharField(max_length=20)
    hour=models.TimeField()
    programme=models.ForeignKey(programme,on_delete=models.CASCADE)
    year = models.IntegerField()
    
class computers(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_label=models.CharField(max_length=20)
    lab = models.ForeignKey(lab,on_delete=models.CASCADE)
    cpu=models.ForeignKey(cpu_types,on_delete=models.CASCADE)
    ram=models.ForeignKey(ram_type,on_delete=models.CASCADE)
    storage=models.ForeignKey(storage_type,on_delete=models.CASCADE)
    dop=models.DateField()
    status=models.CharField(max_length=20)
    invoice_no=models.IntegerField()
    os_type=models.CharField(max_length=20)
    mb=models.ForeignKey(motherboard_type,on_delete=models.CASCADE)
    smps=models.ForeignKey(smps,on_delete=models.CASCADE)
    keyboard=models.ForeignKey(keyboard,on_delete=models.CASCADE)
    mouse=models.ForeignKey(mouse,on_delete=models.CASCADE)
    monitor=models.ForeignKey(monitor,on_delete=models.CASCADE)
    
class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    computer = models.ForeignKey(computers, on_delete=models.CASCADE)
    complaint_details = models.TextField()
    complaint_date = models.DateField()  # No auto_now_add=True
    def __str__(self):
        return f"{self.complaint_details}"
class Repair(models.Model):
    repair_id = models.AutoField(primary_key=True)
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE)
    reason = models.TextField()
    repair_date = models.DateField()  # No auto_now=True
    