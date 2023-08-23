from django.urls import path
from . import views  # view가 있는 현재폴더 posts에서 가져온다는 말 


app_name = 'posts' # 이건 그냥 장고에서 하라는 데로 써야함(index.html에서 posts.detail과 연결되는 부분) 

urlpatterns = [
    path('',views.index, name='index'), # ''에 아무것도 안적으면 경로 posts/만 적어짐.
    # 이제 app_name, name을 변수로 사용해서 url 을 작성할 예정
    path('<int:id>/', views.detail, name='detail'),

    # Create
    path('new/', views.new, name='new'),
]