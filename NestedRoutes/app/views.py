from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

posts_list = [
    {"name": "Post 1", "pop": 2, "date": "01.12.23", "likes": 3, "com": "Good"},
    {"name": "Post 2", "pop": 6, "date": "03.12.23", "likes": 14, "com": "Nice"},
    {"name": "Post 3", "pop": 4, "date": "04.12.23", "likes": 5, "com": "Beautifull"},
    {"name": "Post 4", "pop": 8, "date": "05.12.23", "likes": 27, "com": "Very Good"},
]

def popular(request):
    pop_post = 0
    for i in posts_list:
        if i.get("pop") > pop_post:
            pop_post = i.get("pop")
            output_post = i

    return HttpResponse(f"""<h2>Название поста: {output_post.get('name')}</h2> <br> <h2>Значение популярности: {pop_post}</h2> <br> <h2>Количество лайков: {output_post.get('likes')}</h2> <br> <h2>Комментарий: {output_post.get('com')}</h2> <br> <h2>Дата: {output_post.get('date')}</h2> <br>""")

def new(request):
    new_post = posts_list[-1]
    return HttpResponse(f"""<h2>Название поста: {new_post.get('name')}</h2> <br> <h2>Значение популярности: {new_post.get('pop')}</h2> <br> <h2>Количество лайков: {new_post.get('likes')}</h2> <br> <h2>Комментарий: {new_post.get('com')}</h2> <br> <h2>Дата: {new_post.get('date')}</h2>""")

def all_posts(request):
    return HttpResponse(f"<h2>{posts_list}</h2>")

def get_likes_com(request, post=0):

        if post < len(posts_list):
            return HttpResponse(f'<h2>Likes: {posts_list[post].get("likes")}</h2> <br> <h2>Commentaries: {posts_list[post].get("com")}</h2>')
        else:
            return HttpResponseNotFound("<h2>Not Found</h2>")

def index(request):
    login = request.GET.get("login", "Undefineed")
    password = request.GET.get("password", "Undefineed")
    return HttpResponse(f'<h2>Login: {login}</h2> <br> <h2>Password: {password}</h2>')

# временная переадресация
def about(request):
    return HttpResponseRedirect("/posts/allposts")

def contacts(request):
    return HttpResponsePermanentRedirect("/")

def error(request):
    return HttpResponse('<h2>Загрузка страницы была завершена ошибкой 404</h2>', status=404)

def access(request, login="Undifined", password="Undifined"):
    if login == "admin" and password == "admin":
        return HttpResponse("<h2>Доступ разрешён</h2><br><h2>Добро пожаловать</h2>")
    else:
        return HttpResponse("<h2>У вас нет прав администратора</h2>")


def js_file(request, name='Undifined', age=0):
    return JsonResponse({"name": name, "age": age})

def set(request):
    name = request.GET.get("name", "Undefined")
    response = HttpResponse(f"Hello {name}")
    response.set_cookie("name", name)
    return response

def get(request):
    name = request.COOKIES["name"]
    return HttpResponse(f"Hello {name}")
