from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import PostForm
from .models import Post
from .get_title import call_groq
from django.views.decorators.csrf import csrf_exempt
import urllib

def create_post(request):
    
    return render(request, 'myapp/create_post.html')

def blog_form(request):
    
    return render(request, 'myapp/blog_form.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

@csrf_exempt
def ajax_call(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
                content = data.get('content')
            
            elif request.content_type == 'application/x-www-form-urlencoded':
                decoded_body = request.body.decode('utf-8')
                parsed_data = urllib.parse.parse_qs(decoded_body)
                content = parsed_data.get('content', [None])[0]
            
            if content is None:
                return JsonResponse({'success': False, 'message': 'Content is missing from the request'}, status=400)

            result = call_groq(content)
            return JsonResponse({'success': True, 'result': result})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)
