from django.shortcuts import render
from .import pool
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def index(request):
     return render(request,"ClientView/index.html")






@xframe_options_exempt
def customerinterface(request):
    try:
       row = request.session["comp"]
       return render(request,"ClientView/registration.html",{'compid':row[0]})
    except:
       return render(request, "complogin.html", {'msg': 'needs to login'})


def subcustomerinterface(request):
    try:
        prodid = request.POST['prodid']

        compid = request.POST['compid']
        custmob = request.POST['custmob']
        custemail = request.POST['custemail']

        custname = request.POST['custname']
        custinvoice = request.POST['custinvoice']

        custpass = request.POST['custpass']

        db, cmd = pool.connection()
        q = "insert into customer(customermobileno,customeremailid,name,companyid,invoiceno,password,prodid) " \
            "values('{0}','{1}','{2}',{3},'{4}','{5}',{6})". \
            format(custmob, custemail, custname, compid,custinvoice, custpass,prodid)
        cmd.execute(q)
        db.commit()
        db.close()

        return render(request, "ClientView/login.html", {'msg': 'registration done ,try logging in'})
    except Exception as e:
        # print("**********",e)
        return render(request, "ClientView/registration.html", {'msg': 'registration  not done'})

@xframe_options_exempt
def customerlogin(request):
    return render(request,"ClientView/login.html",{'msg':''})

def customerlogincheck(request):
    try:
        email=request.POST['email']
        password=request.POST['password']
        db, cmd = pool.connection()
        q="select * from customer where (customeremailid='{0}' or customermobileno='{1}') and password='{2}'".format(email, email, password)
        cmd.execute(q)
        row=cmd.fetchone()
        print(row)
        db.close()
        if(row):
          request.session["cust"]=row
          return categories(request)
        else:
          return render(request, "ClientView/login.html",{'msg':'Invalid Login'})
    except:
        return render(request, "ClientView/login.html", {'msg': 'Invalid Login'})



def categories(request):
    try:
        db, cmd = pool.connection()
        row=request.session["cust"]
        cmd.execute("Select * from categories where companyid={0}".format(row[3]))
        rows = cmd.fetchall()
        return render(request, "ClientView/categories.html", {'rows':rows})
    except Exception as e:
        return render(request, "ClientView/categories.html", {'rows': []})


@xframe_options_exempt
def subcatdisplaybycatid(request):
    try:
        cid=request.GET["cid"]
        db,cmd=pool.connection()
        q="select * from subcategory where categoryid={0}".format(cid)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()

        return render(request, "ClientView/companysubcategories.html", {'data': rows})
    except Exception as e:
        return render(request, "ClientView/companysubcategories.html",{'data':[]})



@xframe_options_exempt
def  productdisplaybysubcatid(request):
    try:
        scid=request.GET["scid"]
        row = request.session["cust"]

        db,cmd=pool.connection()
        q="select * from product where subcategoryid={0} and productid={1}".format(scid,row[6])
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()

        return render(request, "ClientView/companyproducts.html", {'data': rows})
    except Exception as e:
        return render(request, "ClientView/companyproducts.html",{'data':[]})
