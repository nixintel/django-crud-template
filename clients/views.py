from django.shortcuts import render, redirect
from django.http import request, Http404
from . models import Vendor
from . forms import VendorForm

# Create your views here.

# CREATE

def add(request):
    form = VendorForm()

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor-list')

    context = {
        'form': form,
    }  

    return render(request, 'clients/add.html', context)

# READ


def list(request):
    try:
        vendors = Vendor.objects.all()
        context = {
            'vendors': vendors
        }
    except Vendor.DoesNotExist:
        raise Http404("Vendor does not exist")
    return render(request,'clients/list.html', context )

# UPDATE

def update(request, pk):
    vendor = Vendor.objects.get(id=pk)
    form = VendorForm(instance=vendor)

    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('list-vendors')

    context = {
        'vendor': vendor,
        'form': form,
    }
    return render(request, 'clients/update.html', context)


# DELETE

def delete(request, pk):
    vendor = Vendor.objects.get(id=pk)

    if request.method == 'POST':
        vendor.delete()
        return redirect('list-vendors')

    context = {
        'vendor': vendor,
    }
    return render(request, 'clients/delete.html', context)