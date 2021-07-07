from django.shortcuts import render
from .import pool
from django.contrib import auth

def complogin(request):
    return render(request,"complogin.html",{'msg':''})

def complogincheck(request):
    email=request.POST['email']
    password=request.POST['password']
    db, cmd = pool.connection()
    q="select * from companies where (email='{0}' or companyid='{1}') and password='{2}'".format(email,email,password)
    cmd.execute(q)
    row=cmd.fetchone()
    db.close()

    if(row):
        request.session["comp"]=row

        return render(request, "compdashboard.html",{'row':row})
    else:
        return render(request, "complogin.html",{'msg':'Invalid Login'})

def complogout(request):
        auth.logout(request)
        return render(request, "complogin.html",{'msg':''})



