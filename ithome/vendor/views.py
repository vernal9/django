from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm
from .forms import RawVendorForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView

# Create your views here.
#def vendor_index(request):
#    vendor_list = Vendor.objects.all()  # 把所有 Vendor 的資料取出來
#    context = {'vendor_list': vendor_list}  # 建立 Dict對應到Vendor的資料，
#    return render(request, 'vendors/vendor_detail.html', context)

def singleVendor(request, id):
    #vendor_list = Vendor.objects.get(id=id)
    vendor_list = get_object_or_404(Vendor, id=id)
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendors/vendor_one.html', context)

#def vendor_create_view(request):
#    form = VendorForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = VerdorForm()  # 清空 form
#    context = {
#        'form' : form
#    }
#    return render(request, "vendors/vendor_create.html", context)

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'

class VendorDetail(DetailView):
    model = Vendor
    # queryset = Vendor.objects.all()
    template_name = 'vendors/vendor_detail.html'

class VendorCreateView(CreateView):
    #model = Vendor
    form_class = VendorForm
    #fields = '__all__'
    #fields = ['vendor_name', 'store_name'] #指定欄位寫法
    template_name = 'vendors/vendor_create.html'

class VendorUpdateView(UpdateView):
    form_class = VendorForm
    template_name = 'vendors/vendor_create.html'
    queryset = Vendor.objects.all()

