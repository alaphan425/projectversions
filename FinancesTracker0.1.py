import datetime

class Spending:
    def __init__(self, name, business, QTY, category, YYYY, MM, DD):
        # Initialization
        self.name = name
        self.business = business
        self.QTY = QTY
        self.category = category
        self.YYYY = YYYY
        self.MM = MM
        self.DD = DD
        # Create list to append purchase name, for what business it was 
        # puchased, and for what it was purchased.
        self.spendingInfo = []
        self.spendingQTYDate = {}
        date = datetime.date(YYYY, MM, DD)
        self.spendingInfo.append(date, QTY, name, business, category)
        self.spendingQTYDate[date] = QTY
        
class Revenue:
    def __init__(self, name, business, QTY, category, YYYY, MM, DD):
        # Initialization
        self.name = name
        self.business = business
        self.QTY = QTY
        self.category = category
        self.YYYY = YYYY
        self.MM = MM
        self.DD = DD
        # Create list to append purchase name, for what business it was 
        # puchased, and for what it was purchased.
        self.revenueInfo = []
        self.revenueQTYDate = {}
        date = datetime.date(YYYY, MM, DD)
        self.revenueInfo.append((date, QTY, name, business, category))
        self.revenueQTYDate[date] = QTY

class Profits(Spending, Revenue):
    def __init__(self):
        self.datedProfits = {}
        profit = 0
        for date in set(Revenue.revenueQTYDate.keys()) & set(Spending.spendingQTYDate.keys()):
             profit = float(Revenue.revenueQTYDate[date]) - float(Spending.spendingQTYDate[date])
             self.datedProfits[date] = profit
        