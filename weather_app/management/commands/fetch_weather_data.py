from django.core.management.base import BaseCommand
from weather_app.models import Weather
import requests
import json
import sys


IMPORT_URL = 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{}-{}.json'

class Command(BaseCommand):
    help = 'Displays the weather Report'

    def import_data(self,data,metric,location):
        year = data.get('year', None)
        value = data.get('value', None)
        month = data.get('month', None)

        try:
            weather, created = Weather.objects.get_or_create(
                metric=metric,
                location=location,
                month = month,
                year = year
            )
            if created:
                weather.save()
                display_format = "\nReport, {}, has been saved."
                print(display_format.format(weather))
            else:
                print("Data already present in database")
                sys.exit()
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this report: {}\n{}".format(metric, str(ex))
            print(msg)

    def handle(self, *args, **krawgs):
        url_data = [['Tmax','Tmin','Rainfall'],['UK','England','Scotland','Wales']]
        for i in url_data[0]:
            for j in url_data[1]:
                headers = {'Content-Type': 'application/json'}
                response = requests.get(url=IMPORT_URL.format(i,j),headers=headers,)
                response.raise_for_status()
                data = response.json()

                for object in data:
                    self.import_data(object,i,j)
