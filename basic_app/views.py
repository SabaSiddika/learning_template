from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic = {'text':'hello world','number':100}
    return render(request,'basic_app/index.html',context_dic)

def other(request):
    return render(request,'basic_app/other.html')

def base(request):
    return render(request,'basic_app/base.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')