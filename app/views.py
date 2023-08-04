from django.shortcuts import render

# Create your views here.

def ifelse(request):
    d = {'name' : 'Ajay', 'age' : 4}
    return render(request, 'ifelse.html', context=d)

def ifelif(request):
    d = {'name' : 'Ajay', 'age' : 18}
    return render(request, 'ifelif.html', context = d)

def nestedif(request):
    d = {'a' : 78, 'b' : 85, 'c' : 95}
    return render(request, 'nestedif.html', context = d)

def forloop(request):
    d = {'name' : 'AJAY', 'Hobbies' : ['cricket', 'Football', 'Volleyball', 'chess', 'Badamantion']}
    return render(request, 'forloop.html', context = d)
