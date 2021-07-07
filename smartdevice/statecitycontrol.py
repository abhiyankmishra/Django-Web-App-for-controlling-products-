from django.shortcuts import render
from . import pool
from django.http import JsonResponse
def fetchstates(request):
    try:
        db,cmd=pool.connection()
        cmd.execute("Select * from states")
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)

def fetchcity(request):
    try:
        stateid=request.GET['stateid']
        db,cmd=pool.connection()
        cmd.execute("Select * from city where stateid={}".format(stateid))
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)

