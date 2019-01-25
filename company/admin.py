from django.contrib import admin
from .models import Stock, StockDetailToday, StockQuestion


# Register your models here.
admin.site.register(Stock)
admin.site.register(StockDetailToday)
admin.site.register(StockQuestion)