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
from django.views.decorators.http import require_GET
from django.http import JsonResponse, HttpResponse
from .models import Post, User




@require_GET
def my_view(request):
    return HttpResponse("<h1>Hi</h1>")

@require_GET
def second_try(request, testy):
    return HttpResponse(f"<h1>Hi, you choose: {testy}</h1>")

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
    print(response)
    return JsonResponse({"respone": "OK","data":response})


@require_GET
def get_post_by_id(request, id):
    response = Post.objects.filter(id=id)
    response = [post.serialize() for post in response]
    print(response)
    return JsonResponse({"respone": "OK","data":response})


urlpatterns = [
    path("test/", my_view),
    path("test2/<int:testy>", second_try),
    path("test2/<testy>", third_test),
    path("json/<testy>", test_json),
    path("get_posts/", get_all_posts),
    path("get_post/<int:id>", get_post_by_id)
]

