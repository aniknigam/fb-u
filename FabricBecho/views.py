from django.shortcuts import render
from dashboard.models import Product
from advertisement.models import Advertisement
from math import ceil

def index(request):
    allProds = []
    prod = Product.objects.all()
    ads = Advertisement.objects.all()
    # print(ads)
    
    featured = Product.objects.filter(featured_product='Yes')
    
    # prod = Product.objects.filter(category=cat)
    n = len(prod)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(0, nSlides), nSlides])
    
    params = {'allProds':allProds, 'featured':featured, 'ads':ads}
    return render(request, 'index.html', params)

def searchMatch(query, item):
    if query.lower() in item.product_name.lower() or query.lower() in item.seller_name.lower() or query.lower() in item.desc.lower():
        return True
    else:
        return False
 
def search(request):
    if request.method == 'POST':
        searched = request.POST['search']
        print(searched)
        
        productsTemp = Product.objects.all()
        allProds = []
        prod=[item for item in productsTemp if searchMatch(searched, item)]
        
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        
        allProds.append([prod, range(0, nSlides), nSlides])
    
        params = {'allProds':allProds}
        
        return render(request, 'search.html', params)

        
        
        # query = request.POST.get('query')
        # # print(query)
        # products = Product.objects.filter(product_name__icontains=query)
        # # print(products)
        # params = {'product': products}
        # return render(request, 'shop/search.html', params)
    else:
        return render(request, 'search.html')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
