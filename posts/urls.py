from django.urls import path
from . import views  # view가 있는 현재폴더 posts에서 가져온다는 말 


app_name = 'posts' # 이건 그냥 장고에서 하라는 데로 해야함.

urlpatterns = [
    path('',views.index, name='index'), # ''에 아무것도 안적으면 경로 posts/만 적어짐.
    # 이제 app_name, name을 변수로 사용해서 url 을 작성할 예정
    # ex. 항상 /posts/index 이런식으로 작성했던 것 대신 저 변수 사용 (변경할 때 돌아다니면서 하나하나 바꿀 필요 사라짐)
    
]