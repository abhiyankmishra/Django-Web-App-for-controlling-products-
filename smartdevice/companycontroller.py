from django.shortcuts import render
from .import pool
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse

@xframe_options_exempt
def companyinterface(request):
    try:
     row=request.session["admin"]
     return render(request,"companyinterface.html",{'msg':''})
    except:
        return render(request, "adminlogin.html", {'msg': ''})


def submitcompanyinterface(request):
    try:
         acompanyname=request.POST['compname']
         acontactperson=request.POST['contactperson']
         acontactpersonmobileno = request.POST['mobile']
         aemail=request.POST['email']
         aaddress = request.POST['compaddress']
         astate = request.POST['compstate']
         acity = request.POST['compcity']
         azipcode = request.POST['compzipcode']
         alogo = request.FILES['complogo']
         apassword = request.POST['password']
         alocation=request.POST['location']
         db,cmd=pool.connection()
         q="insert into companies(companyname,contactperson,contactpersonmobileno,email,location,address,state,city,zipcode,logo,password) " \
           "values('{0}','{1}','{2}','{3}','{4}','{5}',{6},{7},{8},'{9}','{10}')".\
             format(acompanyname,acontactperson,acontactpersonmobileno,aemail,alocation,aaddress,astate,acity,azipcode,alogo.name,apassword)
         cmd.execute(q)
         db.commit()
         db.close()
         f=open("D:/django second proj/smartdevice/assets/"+alogo.name,"wb")
         for chunk in alogo.chunks():
            f.write(chunk)
         f.close()


         return render(request, "companyinterface.html",{'msg':'record submitted successfully'})
    except Exception as e :
        # print("**********",e)
        return render(request, "companyinterface.html",{'msg':'record not submitted'})

@xframe_options_exempt
def displayallcompanies(request):
    try:
        row = request.session["admin"]
        db,cmd=pool.connection()
        q="select c.*,(select s.statename from states s where  s.stateid=c.state) as statename,(select ct.cityname from city ct where ct.cityid=c.city) as cityname from companies c"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()

        return render(request, "displayallcompanies.html", {'data': rows})
    except Exception as e:
        return render(request, "adminlogin.html", {'msg': ''})

@xframe_options_exempt
def compdisplaybyid(request):
    try:
        cid=request.GET["cid"]
        db,cmd=pool.connection()
        q="select c.*,(select s.statename from states s where  s.stateid=c.state) as statename,(select ct.cityname from city ct where ct.cityid=c.city) as cityname from companies c where c.companyid={0}".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()

        return render(request, "compdisplaybyid.html", {'data': row})
    except Exception as e:
        return render(request, "compdisplaybyid.html",{'data':[]})



def subcompdisplaybyid(request):
    btn=request.GET['btn']
    if(btn=="Save Edited"):

     try:
        cid=request.GET["compid"]

        acompanyname = request.GET['compname']
        acontactperson = request.GET['contactperson']
        acontactpersonmobileno = request.GET['mobile']
        aemail = request.GET['email']
        aaddress = request.GET['compaddress']
        astate = request.GET['compstate']
        acity = request.GET['compcity']
        azipcode = request.GET['compzipcode']
        apassword = request.GET['password']
        alocation = request.GET['location']

        db,cmd=pool.connection()
        q = "update  companies set companyname='{0}',contactperson='{1}',contactpersonmobileno='{2}',email='{3}',location='{4}',address='{5}',state={6},city={7},zipcode={8},password='{9}' where companyid={10}".\
            format(acompanyname, acontactperson, acontactpersonmobileno, aemail, alocation, aaddress, astate, acity,
                   azipcode, apassword,cid)
        cmd.execute(q) 
        db.commit()
        db.close()

        return displayallcompanies(request)
     except Exception as e:
        return displayallcompanies(request)
    elif(btn=="DELETE"):
        cid = request.GET["compid"]
        db, cmd = pool.connection()
        q="delete from companies where companyid={0}".format(cid)
        cmd.execute(q)
        db.commit()
        db.close()
        return displayallcompanies(request)

@xframe_options_exempt
def picdisplaybyid(request):
    cid = request.GET["cid"]
    pic = request.GET["pic"]
    return render(request, "picdisplaybyid.html", {'data': [cid,pic]})

def subpicdisplaybyid(request):
    try:
       logo=request.FILES['logo']
       cid=request.POST['cid']
       db, cmd = pool.connection()
       q = "update companies set  logo='{0}' where companyid={1}".format(logo.name,cid)
       cmd.execute(q)
       db.commit()
       db.close()
       print("update companies set  logo='{0}' where companyid={1}".format(logo.name,cid))
       f = open("D:/django second proj/smartdevice/assets/" + logo.name, "wb")
       for chunk in logo.chunks():
         f.write(chunk)
       f.close()
       return displayallcompanies(request)
    except Exception as e:
       return displayallcompanies(request)


# def deletebyid(request):
#     try:
#         cid = request.GET["compid"]
#         db,cmd = pool.connection()
#         q = "delete from companies where companyid={0}".format(cid)
#         cmd.execute(q)
#         db.commit()
#         db.close()
#         return displayallcompanies(request)
#     except Exception as e:
#         return displayallcompanies(request)





def fetchcompanies(request):
    try:
        db,cmd=pool.connection()
        cmd.execute("Select * from companies")
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)

