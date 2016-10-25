from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def home(request):
    params = {
        'phrase': 'Hello BMSTU!'
    }
    return render(request, 'home.html', context=params)


def feed(request):
    # Получение ленты пользователя
    # ...

    feed_data = [
        {
            'image': 'https://s-media-cache-ak0.pinimg.com/originals/58/50/77/585077f705e1e1e6385940fee0e6a4d7.jpg',
            'likes_count': 3,
            'username': 'r_dmv',
            'text': 'Природа',
            'published': date(2016, 1, 1)
        },
        {
            'image': 'http://2.bp.blogspot.com/-3LeTuET-4wc/T-_ViLNQXWI/AAAAAAAAAmY/peI5QDSfrP0/s1600/nature134.jpg',
            'likes_count': 10,
            'username': 'grigory51',
            'text': 'Классная природа',
            'published': date(2016, 1, 2)
        },
        {
            'image': 'https://s-media-cache-ak0.pinimg.com/originals/58/50/77/585077f705e1e1e6385940fee0e6a4d7.jpg',
            'likes_count': 2,
            'username': 'r_dmv',
            'text': 'Очень классная природа',
            'published': date(2016, 1, 3)
        },
    ]
    return render(request, 'feed.html', context={'feed': feed_data})

