class sahkoData:
    def __init__(self, kwh, kwh_price):
        self.kwh = kwh
        self.kwh_price = kwh_price / 100 # Price in euros


    def __str__(self):
        return f'Consumed {self.kwh} with total price {self.kwh_price}'

