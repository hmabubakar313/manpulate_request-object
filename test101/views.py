from django.shortcuts import render 
  
# Create your views here. 
def home_view(request):
    # print(request.POST) 
    # name=request.POST.get('name')

    return render(request, "home.html") 

def show(request):
    x=request.POST['your_name']
    print(x)
    data = {
        'name': x,
            }
    return render(request,"show.html",{'data':data})