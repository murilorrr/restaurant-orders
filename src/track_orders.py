class TrackOrders:
    def __init__(self):
        self.log = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.log)

    def add_new_order(self, customer, order, day):
        self.log.append({"customer": customer, "order": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        count = {}
        customer_orders = [row
                           for row in self.log if row['customer'] == customer]
        max_value = customer_orders[0]['order']
        for row in customer_orders:
            if row['order'] not in count:
                count[row['order']] = 1
            if row['order'] in count:
                count[row['order']] += 1
            if count[row['order']] > count[max_value]:
                max_value = row['order']
        return max_value

    def get_never_ordered_per_customer(self, customer):
        all_orders = set()
        customer_orders = set()
        array = self.log
        for row in array:
            all_orders.add(row['order'])
            if row['customer'] == customer:
                customer_orders.add(row['order'])
        return all_orders.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        all_days = set()
        customer_days = set()
        array = self.log
        for row in array:
            all_days.add(row['day'])
            if row['customer'] == customer:
                customer_days.add(row['day'])
        return all_days.difference(customer_days)

    def get_busiest_day(self):
        count = {}
        array = self.log
        max_value = array[0]['day']
        for row in array:
            if row['day'] not in count:
                count[row['day']] = 1
            if row['day'] in count:
                count[row['day']] += 1
            if count[row['day']] > count[max_value]:
                max_value = row['day']
        return max_value

    def get_least_busy_day(self):
        count = {}
        array = self.log
        min_value = array[0]['day']
        for row in array:
            if row['day'] not in count:
                count[row['day']] = 1
            if row['day'] in count:
                count[row['day']] += 1
            if count[row['day']] < count[min_value]:
                min_value = row['day']
        return min_value
