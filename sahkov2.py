class sahkoData:
    def __init__(self, kwh, kwh_price):
        self.kwh = kwh
        self.kwh_price = kwh_price / 100 # Price in euros

    def __str__(self):
        return f'Consumed {self.kwh} with total price {self.kwh_price}'

    def monthly_cost(self):
        self.cost = self.kwh * self.kwh_price

    def show_monthly_cost(self):
        return f'Monthly cost {self.cost:.2f}e'

eka = sahkoData(600.78, 3.75)
print(eka)
eka.monthly_cost()
print(eka.show_monthly_cost())