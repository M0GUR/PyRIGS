from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.utils import timezone
from django.db.models import Max
import random

from assets import models


class Command(BaseCommand):
    help = 'Creates some sample data for testing'

    def handle(self, *args, **kwargs):
        from django.conf import settings

        if not (settings.DEBUG or settings.STAGING):
            raise CommandError('You cannot run this command in production')

        random.seed('Some object to see the random number generator')

        self.create_categories()
        self.create_statuses()
        self.create_suppliers()
        self.create_assets()
        self.create_connectors()
        self.create_cables()

    def create_categories(self):
        categories = ['Case', 'Video', 'General', 'Sound', 'Lighting', 'Rigging']

        for cat in categories:
            models.AssetCategory.objects.create(name=cat)

    def create_statuses(self):
        statuses = ['In Service', 'Lost', 'Binned', 'Sold', 'Broken']

        for stat in statuses:
            models.AssetStatus.objects.create(name=stat)

    def create_suppliers(self):
        suppliers = ["Acme, inc.", "Widget Corp", "123 Warehousing", "Demo Company", "Smith and Co.", "Foo Bars", "ABC Telecom", "Fake Brothers", "QWERTY Logistics", "Demo, inc.", "Sample Company", "Sample, inc", "Acme Corp", "Allied Biscuit", "Ankh-Sto Associates", "Extensive Enterprise", "Galaxy Corp", "Globo-Chem", "Mr. Sparkle", "Globex Corporation", "LexCorp", "LuthorCorp", "North Central Positronics", "Omni Consimer Products", "Praxis Corporation", "Sombra Corporation", "Sto Plains Holdings", "Tessier-Ashpool", "Wayne Enterprises", "Wentworth Industries", "ZiffCorp", "Bluth Company", "Strickland Propane", "Thatherton Fuels", "Three Waters", "Water and Power", "Western Gas & Electric", "Mammoth Pictures", "Mooby Corp", "Gringotts", "Thrift Bank", "Flowers By Irene", "The Legitimate Businessmens Club", "Osato Chemicals", "Transworld Consortium", "Universal Export", "United Fried Chicken", "Virtucon", "Kumatsu Motors", "Keedsler Motors", "Powell Motors", "Industrial Automation", "Sirius Cybernetics Corporation", "U.S. Robotics and Mechanical Men", "Colonial Movers", "Corellian Engineering Corporation", "Incom Corporation", "General Products", "Leeding Engines Ltd.", "Blammo",
                     "Input, Inc.", "Mainway Toys", "Videlectrix", "Zevo Toys", "Ajax", "Axis Chemical Co.", "Barrytron", "Carrys Candles", "Cogswell Cogs", "Spacely Sprockets", "General Forge and Foundry", "Duff Brewing Company", "Dunder Mifflin", "General Services Corporation", "Monarch Playing Card Co.", "Krustyco", "Initech", "Roboto Industries", "Primatech", "Sonky Rubber Goods", "St. Anky Beer", "Stay Puft Corporation", "Vandelay Industries", "Wernham Hogg", "Gadgetron", "Burleigh and Stronginthearm", "BLAND Corporation", "Nordyne Defense Dynamics", "Petrox Oil Company", "Roxxon", "McMahon and Tate", "Sixty Second Avenue", "Charles Townsend Agency", "Spade and Archer", "Megadodo Publications", "Rouster and Sideways", "C.H. Lavatory and Sons", "Globo Gym American Corp", "The New Firm", "SpringShield", "Compuglobalhypermeganet", "Data Systems", "Gizmonic Institute", "Initrode", "Taggart Transcontinental", "Atlantic Northern", "Niagular", "Plow King", "Big Kahuna Burger", "Big T Burgers and Fries", "Chez Quis", "Chotchkies", "The Frying Dutchman", "Klimpys", "The Krusty Krab", "Monks Diner", "Milliways", "Minuteman Cafe", "Taco Grande", "Tip Top Cafe", "Moes Tavern", "Central Perk", "Chasers"]

        for supplier in suppliers:
            models.Supplier.objects.create(name=supplier)

    def create_assets(self):
        asset_description = ['Large cable', 'Shiny thing', 'New lights', 'Really expensive microphone', 'Box of fuse flaps', 'Expensive tool we didn\'t agree to buy', 'Cable drums', 'Boring amount of tape', 'Video stuff no one knows how to use', 'More amplifiers', 'Heatshrink']

        categories = models.AssetCategory.objects.all()
        statuses = models.AssetStatus.objects.all()
        suppliers = models.Supplier.objects.all()

        for i in range(100):
            asset = models.Asset.objects.create(
                asset_id='{}'.format(models.Asset.get_available_asset_id()),
                description=random.choice(asset_description),
                category=random.choice(categories),
                status=random.choice(statuses),
                date_acquired=timezone.now().date()
            )

            if i % 4 == 0:
                asset.parent = models.Asset.objects.order_by('?').first()

            if i % 3 == 0:
                asset.purchased_from = random.choice(suppliers)

            asset.save()

    def create_cables(self):
        asset_description = ['The worm', 'Harting without a cap', 'Heavy cable', 'Extension lead', 'IEC cable that we should remember to prep']

        csas = [0.75, 1.00, 1.25, 2.5, 4]
        lengths = [1,2,5,10,15,20,25,30,50,100]
        cores = [3,5]
        circuits = [1,2,3,6]
        categories = models.AssetCategory.objects.all()
        statuses = models.AssetStatus.objects.all()
        suppliers = models.Supplier.objects.all()
        connectors = models.Connector.objects.all()

        for i in range(100):
            asset = models.Asset.objects.create(
                asset_id='{}'.format(models.Asset.get_available_asset_id()),
                description=random.choice(asset_description),
                category=random.choice(categories),
                status=random.choice(statuses),
                date_acquired=timezone.now().date(),

                is_cable = True,
                plug = random.choice(connectors),
                socket = random.choice(connectors),
                csa = random.choice(csas),
                length = random.choice(lengths),
                circuits = random.choice(circuits),
                cores = random.choice(circuits)
            )

            if i % 4 == 0:
                asset.parent = models.Asset.objects.order_by('?').first()

            if i % 3 == 0:
                asset.purchased_from = random.choice(suppliers)

            asset.save()

    def create_connectors(self):
        connectors = [
            {"description": "13A UK", "current_rating": 13, "voltage_rating": 230, "num_pins": 3},
            {"description": "16A", "current_rating": 16, "voltage_rating": 230, "num_pins": 3},
            {"description": "32/3", "current_rating": 32, "voltage_rating": 400, "num_pins": 5},
            {"description": "Socapex", "current_rating": 23, "voltage_rating": 600, "num_pins": 19},
        ]
        for connector in connectors:
            conn = models.Connector.objects.create(**connector)
            conn.save()