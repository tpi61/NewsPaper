from django.urls import path

from .views import PostsList, NewsList, PostDetail


urlpatterns = [
   path('', PostsList.as_view(), name='all_posts'),
   # path('/news/', NewsList.as_view(), name='all_news'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   # path('news/create/', NewsEdit.as_view(), name='news_create'),
   # path('article/create/', ArticleEdit.as_view(), name='article_create'),
]