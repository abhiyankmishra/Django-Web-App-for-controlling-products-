from django.shortcuts import render
from .import pool
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse


@xframe_options_exempt
def subcategoryinterface(request):
    try:
     row = request.session["comp"]
     return render(request,"subcategoryinterface.html",{'companyid':row[0]})
    except:
        return render(request, "complogin.html", {'msg': ''})

@xframe_options_exempt
def submitsubcategoryinterface(request):
    try:
         compid = request.POST['compid']
         catid = request.POST['catid']
         subcatname= request.POST['subcatname']
         description= request.POST['desc']
         subcatlogo= request.FILES['subcatlogo']
         db,cmd=pool.connection()
         q="insert into subcategory(companyid,categoryid,subcategoryname,description ,subcategoryicon) values({0},{1},'{2}','{3}','{4}')".\
             format(compid,catid,subcatname,description,subcatlogo.name)
         cmd.execute(q)
         db.commit()
         db.close()
         f=open("D:/django second proj/smartdevice/assets/"+subcatlogo.name,"wb")
         for chunk in subcatlogo.chunks():
            f.write(chunk)
         f.close()
         return render(request, "subcategoryinterface.html",{'msg':'record submitted successfully'})
    except Exception as e :
        # print("**********",e)
        return render(request, "subcategoryinterface.html",{'msg':'record not submitted'})

@xframe_options_exempt
def displayallsubcategory(request):
        try:
            row = request.session["comp"]

            db, cmd = pool.connection()
            # q="select * from subcategory"
            q = "select sc.*,(select s.companyname from companies s where  s.companyid=sc.companyid) as companyname,(select c.categoryname from categories c  where  c.categoryid=sc.categoryid) as categoryname from subcategory sc"

            cmd.execute(q)
            rows = cmd.fetchall()
            db.close()

            return render(request, "displayallsubcategory.html", {'data': rows})
        except Exception as e:
            return render(request, "complogin.html", {'msg': ''})


@xframe_options_exempt
def subcatpicdisplaybyid(request):
    scid = request.GET["scid"]
    pic = request.GET["pic"]
    return render(request, "subcatpicdisplaybyid.html", {'data': [scid,pic]})

@xframe_options_exempt
def subsubcatpicdisplaybyid(request):
    try:
       logo=request.FILES['logo']
       scid=request.POST['scid']
       db, cmd = pool.connection()
       q = "update subcategory set  subcategoryicon='{0}' where subcategoryid={1}".format(logo.name,scid)
       cmd.execute(q)
       db.commit()
       db.close()
       # print("update companies set  logo='{0}' where companyid={1}".format(logo.name,cid))
       f = open("D:/django second proj/smartdevice/assets/" + logo.name, "wb")
       for chunk in logo.chunks():
         f.write(chunk)
       f.close()
       return displayallsubcategory(request)
    except Exception as e:
       return displayallsubcategory(request)


@xframe_options_exempt
def subcatdisplaybyid(request):
    try:
        scid=request.GET["scid"]
        db,cmd=pool.connection()
        q="select * from subcategory where subcategoryid={0}".format(scid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()

        return render(request, "subcatdisplaybyid.html", {'data': row})
    except Exception as e:
        return render(request, "subcatpdisplaybyid.html",{'data':[]})


@xframe_options_exempt
def subsubcatdisplaybyid(request):
    btn=request.GET['btn']
    if(btn=="Save Edited"):

     try:
        scid=request.GET["scid"]
        compid = request.GET['compid']
        catid = request.GET['catid']
        subcatname = request.GET['subcatname']
        desc = request.GET['desc']

        db,cmd=pool.connection()
        q = "update  subcategory set companyid={0},categoryid={1},subcategoryname='{2}',description='{3}' where subcategoryid={4}".\
            format(compid, catid, subcatname,desc,scid)
        cmd.execute(q)
        db.commit()
        db.close()

        return displayallsubcategory(request)
     except Exception as e:
         return displayallsubcategory(request)
    elif(btn=="DELETE"):
        scid = request.GET["scid"]
        db, cmd = pool.connection()
        q="delete from subcategory where subcategoryid={0}".format(scid)
        cmd.execute(q)
        db.commit()
        db.close()
        return displayallsubcategory(request)

def fetchsubcategories(request):
    try:
        categoryid=request.GET['categoryid']

        db,cmd=pool.connection()
        cmd.execute("Select * from subcategory where categoryid={}".format(categoryid))
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)


