from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from tool.Quiz import quiz
import json
import csv
from django.core.cache import cache
from Student.models import UserProfile
# Create your views here.

#异常码 10100 - 10199

import os


class VocabViews(View):
    def get(self,request):
        pro=quiz.quiz()
        print(request.GET)
        get_id=request.GET.get('id')
        get_id = str(get_id)
        if get_id=="":
            return JsonResponse({'code': 411,'msg':'Please login first'})
        wordList1,wordList2,wordList3 = pro.GetWordcsv()
        
        print(get_id)
        cache.set(get_id+"wordList1",wordList1,15*60)
        cache.set(get_id+"wordList2",wordList2,15*60)
        cache.set(get_id+"wordList3",wordList3,15*60)
        problemList = pro.Problem(wordList1,wordList2,wordList3)

        return JsonResponse({'code':200,'msg':'get test','data':problemList})

    def post(self,request):
        json_str=request.body
        json_obj=json.loads(json_str)
        test=json_obj['data']
        cookie_id=request.COOKIES.get('id')
        get_id=json_obj['id']
        print(get_id)
        wordList1=cache.get(get_id+'wordList1')
        wordList2=cache.get(get_id+'wordList2')
        wordList3=cache.get(get_id+'wordList3')
        res = quiz.quiz()
        result=res.evaluateResult(res.getResult(test,wordList1,wordList2,wordList3),wordList1,wordList2,wordList3)  
        print("result: ",result)
        
        user=UserProfile.objects.get(id=get_id)
        user.result=result
        user.save()

#         print(type(test))
#         print(test)
        
        data={'result':result}
        
        result = {'code': 200,'msg':'post test',"data":data}
        return JsonResponse(result)
