from rest_framework import serializers
from .models import Stock, StockDetailToday, StockQuestion


class StockQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockQuestion
        fields = '__all__'


class StockDetailTodaySerializer(serializers.ModelSerializer):

    stock_question = StockQuestionSerializer(source='stockquestion_set', many=True)

    class Meta:
        model = StockDetailToday
        fields = ('id', 'today', 'today_up', 'today_down', 'stock', 'stock_question')
        #fields = StockDetailToday.objects.filter()
        # read_only_fields =


class StockSerializer(serializers.ModelSerializer):

    stock_daily_today = StockDetailTodaySerializer(source='stockdetailtoday_set', many=True)

    class Meta:
        model = Stock
        #fields = ('ticker', 'volume')
        fields = ('ticker', 'volume', 'stock_daily_today')
        #fields = '__all__'


