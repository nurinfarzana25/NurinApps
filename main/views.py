from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)


# Create your views here.
def show_main(request):
    items = Item.objects.all()
    # total_stok = items.aaggregate(total_stok=Sum('amount'))['total_stok'] or 0
    total_stok = items.aggregate(total_stok=Sum('amount'))['total_stok'] or 0


    context = {
        'name': 'Nurin Farzana Nafiah',
        'class': 'PBP C',
        'items': items,
        'total_stok': total_stok,
    }

    return render(request, "main.html", context)


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

