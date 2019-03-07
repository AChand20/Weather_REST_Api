from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Weather
from .serializers import WeatherSerializer


class WeatherView(ListAPIView):

    serializer_class = WeatherSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        qset = queryset.values_list('year','month','value')
        ls =[]
        for w in qset:
            if int(w[1])<=9:
                ls.append({str(w[0])+"-0"+str(w[1]):int(w[2])})
            else:
                ls.append({str(w[0])+"-"+str(w[1]):int(w[2])})

        return Response(ls)

    def get_queryset(self):
        queryset = Weather.objects.all()

        location = self.kwargs['location']

        metric = self.kwargs['metric']

        start_date = self.kwargs['start_date']
        start_date = start_date.split('-')

        end_date = self.kwargs['end_date']
        end_date = end_date.split('-')
        end_date[0]=str(int(end_date[0])-1)

        if(location is not None and metric is not None and start_date is not None and end_date is not None):
            queryset1 = queryset.filter(location = location,
                                       metric = metric,
                                       year__gte = start_date[0],
                                       month__gte = start_date[1],
                                       year__lte = end_date[0])
            queryset2 = queryset.filter(location = location,
                                       metric = metric,
                                       year__exact = str(int(end_date[0])+1),
                                       month__lte = end_date[1])

            return queryset1.union(queryset2)
