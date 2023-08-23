"""
URL configuration for board project.

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
from django.contrib import admin
from django.urls import path, include

# 처음 기본으로 설정되어있는 admin 설정때문에 runserver 처음 시행시에
# 18개가 migrate DB로 번역되어야 합니다. 이런식으로 뜨는 것. 
# 만약 model 안의 이름이 무언가가 바뀌면 다시 번역 코드를 입력해야함.

urlpatterns = [
    path('admin/', admin.site.urls),
    # posts/로 시작하는 url들을 묶어서 표현
    path('posts/', include('posts.urls')),   # path(), -> posts/, include() -> 괄호 안 : 이런식으로 내가 어떤 함수를 작성하는지 의식하면서 적어나가기

]
