from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Nurin Farzana Nafiah',
        'class': 'PBP C',
        'barang1' : 'Beras Sumo Premium',
        'barang2' : 'Minyak Goreng Tropical',
        'barang3' : 'Indomie Goreng',
        'barang4' : 'Indomie Kuah Rasa Soto',
        'barang5' : 'Ultra Milk Plain',
        'barang6' : 'Aqua Mineral',
        'barang7' : 'Pantene Shampoo',
        'berat1' :'5 Kg',
        'berat2' :'2 L',
        'berat3' :'80 Gram',
        'berat4' :'70 Gram',
        'berat5' :'250 Ml',
        'berat6' :'750 Ml',
        'berat7' :'900 Ml',
        'harga1' :'Rp72.600',
        'harga2' :'Rp36.200',
        'harga3' :'Rp3.100',
        'harga4' :'Rp2.850',
        'harga5' :'Rp4.450',
        'harga6' :'Rp6.600',
        'harga7' :'Rp108.700',
        'stok1' :'48',
        'stok2' :'69',
        'stok3' :'120',
        'stok4' :'108',
        'stok5' :'55',
        'stok6' :'78',
        'stok7' :'85'
    }

    return render(request, "main.html", context)
