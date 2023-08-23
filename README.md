- 프로젝트 생성/ 앱 생성
```bash
django-admin startproject <pjt-name>
django-admin startapp <app-name>
```
- 그 나머지
```bash
python manage.py <command>
```
## HTTP status code
- 200: OK
- 30X: redirect 
- (django는 항상 url 뒤에 / 붙여야 함. 두 url path를 연결할 때 뒤에 슬래쉬가 없으면 그 두개의 url이 슬래쉬 없이 연결되기 때문에 뒤에 항상 붙여놓으라고 django에서 권장하는 것임)
- 4XX: client error(사용자가 잘못한 것)
    - 401: unauthorized error
    - 403: Forbidden
    - 404: Not Found
- 500: server error 