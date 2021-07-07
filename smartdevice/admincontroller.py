from django.shortcuts import render
from .import pool
from django.contrib import auth
def adminlogin(request):
    return render(request,"adminlogin.html",{'msg':''})

def adminlogincheck(request):
    email=request.POST['email']
    password=request.POST['password']
    db, cmd = pool.connection()
    q="select * from adminlogin where adminemailid='{0}' and password='{1}'".format(email,password)
    cmd.execute(q)
    row=cmd.fetchone()
    db.close()

    if(row):
        request.session["admin"]=row
        return render(request, "dashboard.html",{'row':row})
    else:
        return render(request, "adminlogin.html",{'msg':'Invalid Login'})


def logout(request):
    auth.logout(request)
    return render(request, "adminlogin.html", {'msg': ''})
