from django.shortcuts import render

def showIndex(request):
    return render(request, "index.html")

def logincheck(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "ankit" and password == "tomar":
        return render(request,"Welcome.html")
    else:
        return render(request,"error.html")

