from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    context = {'recipe': DATA.get('omlet')}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'index.html', context=context)

def pasta(request):
    context = {'recipe': DATA.get('pasta')}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'index.html', context=context)

def buter(request):
    context = {'recipe': DATA['buter']}
    servings = int(request.GET.get('servings', 1))
    for key in context['recipe'].keys():
        context['recipe'][key] = context['recipe'][key] * servings
    return render(request, 'index.html', context=context)


def home(request):
    return render(request, 'main.html')


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
