from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponse
import os
import django.contrib.auth
from django.views.generic import DetailView, ListView

from users.models import User
from goods.models import Categories
from main.models import (
    Index,
    About,
    Contact,
    Delivery,
    Stocks,
    Offer,
    Confidentiality,
    News,
    Interesting,
    
)
    

class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        form = Index.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Главная"
        context["form"] = form
        return context
    
class DeliveryView(TemplateView):
    template_name = "main/delivery.html"

    def get_context_data(self, **kwargs):
        form = Delivery.objects.order_by("-id")
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Оплата и услуги"
        context["form"] = form
        return context


class ContactView(TemplateView):
    template_name = "main/contacts.html"

    def get_context_data(self, **kwargs):
        form = Contact.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Наши контакты"
        context["form"] = form
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        form = About.objects.order_by("-id")
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-О нас"
        context["form"] = form
        return context


class StocksView(TemplateView):
    template_name = "main/stocks.html"

    def get_context_data(self, **kwargs):
        form = Stocks.objects.order_by("-id")
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Акции"
        context["form"] = form
        return context


class OfferView(TemplateView):
    template_name = "main/offer.html"

    def get_context_data(self, **kwargs):
        form = Offer.objects.order_by("-id")
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Публичные фферты"
        context["form"] = form
        return context


class ConfidentialityView(TemplateView):
    template_name = "main/confidentiality.html"

    def get_context_data(self, **kwargs):
        form = Confidentiality.objects.order_by("-id")
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Политика конфеденциальности"
        context["form"] = form
        return context


class NewsView(TemplateView):
    template_name = "main/news.html"

    def get_context_data(self, **kwargs):
        form = News.objects.order_by("-id")
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Новости"
        context["form"] = form
        return context


class InterestingView(TemplateView):
    template_name = "main/interesting.html"

    def get_context_data(self, **kwargs):
        form = Interesting.objects.order_by("-id")
        context = super().get_context_data(**kwargs)
        context["title"] = "Магазин инженерной сантехники-Это интересно"
        context["form"] = form
        return context


# def index(request):

#     context={
#         'title': 'КАЛИНКА-Главная',
#         'content': 'Интернет магазин мебели КАЛИНКА',
#     }
#     return render(request, 'main/index.html', context)


# def about(request):
#     form=About.objects.order_by('-id')
#     context={
#         'title': 'КАЛИНКА-Про нас',
#         'form': form
#     }
#     return render(request, 'main/about.html', context)


# def contacts(request):
#     form=Contact.objects.all()
#     context={
#         'title': 'КАЛИНКА-Наши контакты',
#         'form': form
#     }
#     return render(request, 'main/contacts.html', context)

# def delivery(request):
#     form=Delivery.objects.order_by('-id')
#     context={
#         'title': 'КАЛИНКА-Доставка и оплата',
#         'form': form
#     }
#     return render(request, 'main/delivery.html', context)
