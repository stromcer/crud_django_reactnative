"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse, HttpResponse, HttpRequest
from .models import Post, User
from django.views.decorators.csrf import csrf_exempt
import json


@require_GET
def my_view(request):
    return HttpResponse("<h1>Hi</h1>")

@require_GET
def second_try(request, testy):
    return HttpResponse(f"<h1>Hi, you choose number: {testy}</h1>")

@require_GET
def third_test(request, testy):
    return HttpResponse(f"<h1>Hi, you write: {testy}</h1>")

@require_GET
def test_json(request, testy):
    return JsonResponse(
        {
            "Hello": testy,
            "this_should_be": "a json"
        }
    )
    
@require_GET
def get_all_posts(request):
    response = Post.objects.all()
    response = [post.serialize() for post in response]
    return JsonResponse({"respone": "OK","data":response})

@require_GET
def get_post_by_id(request, id):
    response = Post.objects.filter(id=id)
    response = [post.serialize() for post in response]
    return JsonResponse({"respone": "OK","data":response})

@csrf_exempt
@require_POST
def create_user(request):
    body = json.loads(request.body)
    new_user = User(
        nickname = body["name"]
    )
    new_user.save()
    return JsonResponse({"respone": "OK","data":new_user.serialize()})

@csrf_exempt
@require_POST
def create_post(request):
    body = json.loads(request.body)
    target_author = User.objects.get(nickname=body["author"])
    new_post = Post(
        tittle = body["tittle"],
        content = body["content"],
        author = target_author
    )
    new_post.save()
    return JsonResponse({"respone": "OK","data":new_post.serialize()})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request, id):
    target_user = User.objects.get(pk=id)
    target_user.delete()
    return JsonResponse({"response":"OK","data":f"User with id {id} deleted"})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_post(request, id):
    target_post = Post.objects.get(pk=id)
    target_post.delete()
    return JsonResponse({"response":"OK","data":f"Post with id {id} deleted"})


@csrf_exempt
@require_http_methods(["PUT"])
def modify_user(request, id):
    body = json.loads(request.body)
    target_user = User.objects.get(pk=id)
    target_user.nickname = body["name"]
    target_user.save()
    return JsonResponse({"response":"OK","data":f"User with id {id} changed name to {target_user.nickname}"})


@csrf_exempt
@require_http_methods(["PUT"])
def modify_post(request, id):
    body = json.loads(request.body)
    target_post = Post.objects.get(pk=id)
    target_post.tittle = body["tittle"]
    target_post.content = body["content"]
    target_post.save()
    return JsonResponse({"response":"OK","data":target_post.serialize()})
    
    

urlpatterns = [
    path("get_posts/", get_all_posts),
    path("get_post/<int:id>", get_post_by_id),
    path("new_user/", create_user),
    path("new_post/", create_post),
    path("delete_user/<int:id>", delete_user),
    path("delete_post/<int:id>", delete_post),
    path("modify_user/<int:id>", modify_user),
    path("modify_post/<int:id>", modify_post)
]

