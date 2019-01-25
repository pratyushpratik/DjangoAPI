from django.db import models
import datetime

class Stock(models.Model):
    ticker = models.CharField(max_length=10, primary_key=True)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker


class StockDetailToday(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    today = models.CharField(max_length=100, default=datetime.datetime.now())
    today_up = models.FloatField()
    today_down = models.FloatField()

    def __str__(self):
        return self.today
  #  today_avg = (today_up + today_down)/2


class StockQuestion(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None)
    stock_detail = models.ForeignKey(StockDetailToday, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=10000)

    def __str__(self):
        return self.question