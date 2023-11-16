from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This data is used to print our assumption'
    d={'sorna':data}
    return render(request,'data_render.html',context=d)