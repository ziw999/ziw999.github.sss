from django.contrib import admin

from .models import (
    About,
    Contact,
    Delivery,
    Stocks,
    Offer,
    Confidentiality,
    News,
    Interesting,
    Index,

)


admin.site.register(Index)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Delivery)
admin.site.register(Stocks)
admin.site.register(Offer)
admin.site.register(Confidentiality)
admin.site.register(News)
admin.site.register(Interesting)

