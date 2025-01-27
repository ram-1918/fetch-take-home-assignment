import math

class ReceiptProcessorService:
    """
    Sample Data:
    ------------
    {
        "retailer": "Walgreens",
        "purchaseDate": "2022-01-02",
        "purchaseTime": "08:13",
        "total": "2.65",
        "items": [
            {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
            {"shortDescription": "Dasani", "price": "1.40"}
        ]
    }
    Business Rules:
    ---------------
        Rule 1: len(retailer_name) * 1
        Rule 2: is_rounded(total) && 50
        Rule 3: total % 0.25 == 0 && 25
        Rule 4: total_items // 2 * 5
        Rule 5: round_to_nearest(len(item_description.strip()) % 3 == 0 && item_price * 0.2)
        Rule 6: total > 10 && 5
        Rule 7: day_in_purchase_date % 2 == 1 && 6
        Rule 8: 2PM < time_of_purchase < 4PM && 10
    """
        
    def __init__(self):
        self.total_points = 0
    
    def initialize_data(self, data):
        self.retailer_name = data.get('retailer')
        self.purchase_date = data.get('purchaseDate')
        self.purchase_time = data.get('purchaseTime')
        self.total_price = data.get('total')
        self.items = data.get('items')
    
    def handle_item_description(self):
        # Rule 5: Round to the nearest
        for item in self.items:
            item_description = item.get('shortDescription').strip()
            item_price = float(item.get('price'))

            if len(item_description) % 3 == 0:
                # Use math.ceil for rounding up
                self.total_points += math.ceil(item_price * 0.2)

    def handle_purchase_time_check(self):
        # Rule 8: Puchase time is between 2:00 pm - 4:00 pm, given: 24-hr format, 13:08
        # Expected Times: 2:00, 2:01...3:59
        # 14 <= h < 16 and s > 0
        h, s = list(map(int, self.purchase_time.split(':')))
        if 14 <= h < 16 and s > 0:
            self.total_points += 10
    
    def calculate_points(self):
        total_price_in_float = float(self.total_price)
        items_count = len(self.items)

        # Rule 1: add points based on the length of retailer
        self.total_points += sum((1 for c in self.retailer_name if c.isalnum()))
        print(f'At RULE 1: {self.total_points}')

        # Rule 2: check if the total_price is rounded: 50
        if int(total_price_in_float) == total_price_in_float:
            self.total_points += 50
        print(f'At RULE 2: {self.total_points}')
        
        # Rule 3: check if the total_price is multiple of 0.25
        if total_price_in_float % 0.25 == 0.0:
            self.total_points += 25
        print(f'At RULE 3: {self.total_points}')

        # Rule 4: Add 5 points for every 2 items
        self.total_points += ((items_count) // 2) * 5
        print(f'At RULE 4: {self.total_points}')

        # Rule 5: Round to the nearest
        self.handle_item_description()
        print(f'At RULE 5: {self.total_points}')

        # Rule 7: Day in the purchase date is Odd, date format: YYYY-MM-DD
        if self.purchase_date[-1] not in {'0', '2', '4', '6', '8'}:
            self.total_points += 6
        print(f'At RULE 7: {self.total_points}')
        
        # Rule 8: Puchase time is between 2:00 pm - 4:00 pm
        self.handle_purchase_time_check()
        print(f'At RULE 8: {self.total_points}')

        
    def get_points(self, data):
        # retailer, total, items_count, each_item, day in purchaseDate, purchaseTime
        self.initialize_data(data)
        self.calculate_points()
        return self.total_points