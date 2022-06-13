from django.shortcuts import render
from .models import UserProfile
import json
import random
from django.http import JsonResponse

def login(request):
    if(request.method!="POST"):
        return JsonResponse({'code':403,'msg':"Please use Post"})
    json_str=request.body
    json_obj=json.loads(json_str)['data']

    username=json_obj['username']
    sid=json_obj['sid']
    cet4=json_obj['cet4']
    cet6=json_obj['cet6']
    created_data=UserProfile.objects.create(username=username,sid=sid,
                               cet4=cet4,cet6=cet6,result=0)
    data={'id':created_data.id}
    #print(created_data.id)
    #print({'code':200,'msg':"sucess",'data':data})
    return JsonResponse({'code':200,'msg':"sucess",'data':data})
    