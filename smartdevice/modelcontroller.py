from django.shortcuts import render
from .import pool
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse


@xframe_options_exempt
def modelinterface(request):
    try:
        row = request.session["comp"]
        return render(request,"modelinterface.html",{'companyid':row[0]})
    except:
        return render(request,"complogin.html",{'msg':''})
@xframe_options_exempt
def submitmodelinterface(request):
    try:
         compid = request.POST['compid']
         catid = request.POST['catid']
         subcatid= request.POST['subcatid']
         modelname= request.POST['modelname']
         modeldesc= request.POST['modeldesc']
         db,cmd=pool.connection()
         q="insert into model(companyid,categoryid,subcategoryid,modelname  ,modeldescription  ) values({0},{1},{2},'{3}','{4}')".\
             format(compid,catid,subcatid,modelname,modeldesc)
         cmd.execute(q)
         db.commit()
         db.close()

         return render(request, "modelinterface.html",{'msg':'record submitted successfully'})
    except Exception as e :
        # print("**********",e)
        return render(request, "modelinterface.html",{'msg':'record not submitted'})


@xframe_options_exempt
def displayallmodel(request):
        try:
            row = request.session["comp"]

            db, cmd = pool.connection()
            # q="select * from model"
            q = "select m.*,(select s.companyname from companies s where  s.companyid=m.companyid) as companyname,(select c.categoryname from categories c  where  c.categoryid=m.categoryid) as categoryname,(select sc.subcategoryname from subcategory sc  where  sc.subcategoryid=m.subcategoryid) as subcategoryname from model m"

            cmd.execute(q)
            rows = cmd.fetchall()
            db.close()

            return render(request, "displayallmodel.html", {'data': rows})
        except Exception as e:
            return render(request, "complogin.html", {'msg': ''})

#
# @xframe_options_exempt
# def catpicdisplaybyid(request):
#     cid = request.GET["cid"]
#     pic = request.GET["pic"]
#     return render(request, "catpicdisplaybyid.html", {'data': [cid,pic]})
#
# def subcatpicdisplaybyid(request):
#     try:
#        logo=request.FILES['logo']
#        cid=request.POST['cid']
#        db, cmd = pool.connection()
#        q = "update categories set  categoryicon='{0}' where categoryid={1}".format(logo.name,cid)
#        cmd.execute(q)
#        db.commit()
#        db.close()
#        # print("update companies set  logo='{0}' where companyid={1}".format(logo.name,cid))
#        f = open("D:/django second proj/smartdevice/assets/" + logo.name, "wb")
#        for chunk in logo.chunks():
#          f.write(chunk)
#        f.close()
#        return displayallcategories(request)
#     except Exception as e:
#        return displayallcategories(request)
#


@xframe_options_exempt
def modeldisplaybyid(request):
    try:
        cid=request.GET["cid"]
        db,cmd=pool.connection()
        q="select * from model where modelid={0}".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()

        return render(request, "modeldisplaybyid.html", {'data': row})
    except Exception as e:
        return render(request, "modeldisplaybyid.html",{'data':[]})



def submodeldisplaybyid(request):
    btn=request.GET['btn']
    if(btn=="Save Edited"):

     try:
        mid=request.GET['mid']

        compid = request.GET['compid']
        catid = request.GET['catid']
        subcatid = request.GET['subcatid']

        modname = request.GET['modname']
        desc = request.GET['desc']


        db,cmd=pool.connection()
        q = "update  model set companyid={0},categoryid={1},subcategoryid={2},modelname='{3}',modeldescription='{4}' where modelid={5}".\
            format(compid,catid,subcatid, modname,desc, mid)
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()

        return displayallmodel(request)
     except Exception as e:
         return displayallmodel(request)
    elif(btn=="DELETE"):
        mid = request.GET["mid"]
        db, cmd = pool.connection()
        q="delete from model where modelid={0}".format(mid)
        cmd.execute(q)
        db.commit()
        db.close()
        return displayallmodel(request)


def fetchmodels(request):
    try:
        subcategoryid=request.GET['subcategoryid']

        db,cmd=pool.connection()
        cmd.execute("Select * from model where subcategoryid={0}".format(subcategoryid))
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)


