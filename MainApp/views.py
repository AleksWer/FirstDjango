from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from MainApp.models import Item


# Create your views here.

def home(request):
    context = {
        "name": "Архаров Александр Андреевич",
        "email": "S_RedStar@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        "Имя": "Александр",
        "Отчество": "Андреевич",
        "Фамилия": "Архаров",
        "телефон": "8-800-700-60-50",
        "email": "S_RedStar@mail.ru"

    }
    result = f"""
    <header>
        /<a href="/">Home</a> / <a href="/items"> Items</a> / <a href="/about"> About</a>
    </header><br>
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(result)


def get_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        colors = []

        if item.colors.exists():
            colors = item.colors.all()

    except Item.DoesNotExist:
        return HttpResponseNotFound(f'Item with id={item_id} not found')
    else:
        context = {
            "item": item,
            "colors": colors
        }
        return render(request, "item-page.html", context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)
