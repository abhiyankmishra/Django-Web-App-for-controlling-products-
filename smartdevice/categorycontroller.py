from django.shortcuts import render
from .import pool
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse

@xframe_options_exempt
def categoryinterface(request):
    try:
        row = request.session["comp"]
        return render(request,"categoryinterface.html",{'companyid':row[0]})
    except:
        return render(request, "complogin.html", {'msg': ''})


@xframe_options_exempt
def submitcategoryinterface(request):
    try:
         compid = request.POST['compid']
         catname = request.POST['catname']
         catlogo= request.FILES['catlogo']
         db,cmd=pool.connection()
         q="insert into categories(companyid,categoryname,categoryicon) values({0},'{1}','{2}')".\
             format(compid,catname,catlogo.name)
         cmd.execute(q)
         db.commit()
         db.close()
         f=open("D:/django second proj/smartdevice/assets/"+catlogo.name,"wb")
         for chunk in catlogo.chunks():
            f.write(chunk)
         f.close()
         return render(request, "categoryinterface.html",{'msg':'record submitted successfully'})
    except Exception as e :
        # print("**********",e)
        return render(request, "categoryinterface.html",{'msg':'record not submitted'})


@xframe_options_exempt
def displayallcategories(request):
        try:
            row = request.session["comp"]
            db, cmd = pool.connection()
            # q="select * from categories"
            q = "select c.*,(select s.companyname from companies s where  s.companyid=c.companyid) as companyname from categories c"

            cmd.execute(q)
            rows = cmd.fetchall()
            db.close()

            return render(request, "displayallcategories.html", {'data': rows})
        except Exception as e:
            return render(request, "complogin.html", {'msg': ''})


@xframe_options_exempt
def catpicdisplaybyid(request):
    cid = request.GET["cid"]
    pic = request.GET["pic"]
    return render(request, "catpicdisplaybyid.html", {'data': [cid,pic]})

@xframe_options_exempt
def subcatpicdisplaybyid(request):
    try:
       logo=request.FILES['logo']
       cid=request.POST['cid']
       db, cmd = pool.connection()
       q = "update categories set  categoryicon='{0}' where categoryid={1}".format(logo.name,cid)
       cmd.execute(q)
       db.commit()
       db.close()
       # print("update companies set  logo='{0}' where companyid={1}".format(logo.name,cid))
       f = open("D:/django second proj/smartdevice/assets/" + logo.name, "wb")
       for chunk in logo.chunks():
         f.write(chunk)
       f.close()
       return displayallcategories(request)
    except Exception as e:
       return displayallcategories(request)



@xframe_options_exempt
def catdisplaybyid(request):
    try:
        cid=request.GET["cid"]
        db,cmd=pool.connection()
        q="select * from categories where categoryid={0}".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()

        return render(request, "catdisplaybyid.html", {'data': row})
    except Exception as e:
        return render(request, "catpdisplaybyid.html",{'data':[]})


@xframe_options_exempt
def subcatdisplaybyid(request):
    btn=request.GET['btn']
    if(btn=="Save Edited"):

     try:
        cid=request.GET["cid"]

        compid = request.GET['compid']
        catname = request.GET['catname']

        db,cmd=pool.connection()
        q = "update  categories set companyid={0},categoryname='{1}' where categoryid={2}".\
            format(compid, catname, cid)
        cmd.execute(q)
        db.commit()
        db.close()

        return displayallcategories(request)
     except Exception as e:
         return displayallcategories(request)
    elif(btn=="DELETE"):
        cid = request.GET["cid"]
        db, cmd = pool.connection()
        q="delete from categories where categoryid={0}".format(cid)
        cmd.execute(q)
        db.commit()
        db.close()
        return displayallcategories(request)


def fetchcategories(request):
    try:
        db,cmd=pool.connection()
        cmd.execute("Select * from categories")
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)
