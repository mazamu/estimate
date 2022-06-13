from django.http import JsonResponse
from tool.data import test
import json

json_data='''
[
{
"word": "卢俊义",
  "flag": false
},
{
"word": "吴用",
  "id": 2,
"age": 40,
"sex": "男",
  "flag": false
},
  {
    "word": "吴大用",
    "id": 3,
    "age": 40,
    "sex": "男",
    "flag": false
  },
  {
    "word": "吴小用",
    "id": 4,
    "age": 40,
    "sex": "男",
    "flag": false
  },
  {
    "word": "吴无用",
    "id": 5,
    "age": 40,
    "sex": "男",
    "flag": false
  },
  {
    "word": "吴有用",
    "id": 6,
    "age": 40,
    "sex": "男",
    "flag": false
  },
  {
    "word": "吴啊啊",
    "id": 7,
    "age": 40,
    "sex": "男",
    "flag": false
  },
  {
    "word": "吴呵呵",
    "id": 8,
    "age": 40,
    "sex": "男",
    "flag": false

  }
]
'''
def test_cors(request):
    return JsonResponse({'msg':'CORS is OK'})


def test_json(request):
    mydata=json.loads(json_data)
    return JsonResponse(mydata,safe=False)
    
    