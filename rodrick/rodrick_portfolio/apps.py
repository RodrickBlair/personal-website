from django.apps import AppConfig


class RodrickPortfolioConfig(AppConfig):
    name = 'rodrick_portfolio'

def ready(self):
    	import rodrick_portfolio.signals