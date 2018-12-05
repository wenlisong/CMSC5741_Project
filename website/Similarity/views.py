# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import os
import pdb

def index(request):
    return render(request, 'index.html')

def upload(request):
    print('123')
    if request.method=="GET":
        return  render(request,'index.html')
    elif request.method == "POST":
        res = {"status":"success","code":999}
        img_obj = request.FILES.get('img')
        # with open(os.path.join('static/images', img_obj.name), 'wb') as f:
            # for chunk in img_obj.chunks(chunk_size=1024):
            #     f.write(chunk)
        res['file_path'] = os.path.join('/static/images', img_obj.name)
        return JsonResponse(res)