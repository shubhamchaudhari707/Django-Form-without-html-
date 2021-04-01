from django.shortcuts import render
from testapp.forms import StudentRegistation

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistation(request.POST)
        # print(fm)
        # if fm.is_valid():
        #
        #     print('form validated = ',fm.cleaned_data)
        #     print(fm.cleaned_data['name'])
        #     print(fm.cleaned_data['email'])
        #     print(fm.cleaned_data['mobile'])
        #     print('ye POST request sai aaya hai')
        return render(request, 'testapp/sucess.html', {'form':fm})
    else:
        fm = StudentRegistation()
        print('ye get request sai aaya hai')
    return render(request,'testapp/index.html' , {'form':fm})











