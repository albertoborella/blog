from django.urls import path
from .views import PostListView,PostDetailView,CategoriaListView,AutorListView,PostCreateView,PostUpdateView,PostDeleteView,AboutPageView,dates


urlpatterns = [
    #path('', home, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('crear/', PostCreateView.as_view(), name='crear-post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('categoria/', CategoriaListView.as_view(), name='categoria'),
    path('autor/', AutorListView.as_view(), name='autor'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),
    
]