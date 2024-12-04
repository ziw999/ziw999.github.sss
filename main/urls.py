from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name='main'

urlpatterns = [
    path('index/', cache_page(60*3)(views.IndexView.as_view()), name='index'),
    path('about/', cache_page(60*3)(views.AboutView.as_view()), name='about'),
    path('contacts/', cache_page(60*3)(views.ContactView.as_view()), name='contacts'),
    path('delivery/', cache_page(60*3)(views.DeliveryView.as_view()), name='delivery'),
    path('stocks/', cache_page(60*3)(views.StocksView.as_view()), name='stocks'),
    path('offer/', cache_page(60*3)(views.OfferView.as_view()), name='offer'),
    path('confidentiality/', cache_page(60*3)(views.ConfidentialityView.as_view()), name='confidentiality'),
    path('news/', cache_page(60*3)(views.NewsView.as_view()), name='news'),
    path('interesting/', cache_page(60*3)(views.InterestingView.as_view()), name='interesting'),
]
