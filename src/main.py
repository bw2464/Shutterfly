"""
Use the following command
python main.py --file filename --num number
filename is the location of the data file
number is the number of customers who have
the largest LTV

In the data, I assume that the event time of the customer
is the beginning time for a customer to calculate the visits
and expenditure. If we do not have the customer type for one
customer, we will get the beginning time as the earliest
site visit time for all customers
Also, the order of the events in the file will not effect
the result
"""
from customer import Customer
from site_visit import SiteVisit
from image import Image
from order import Order
import json
import argparse


class Analysis(object):

    def __init__(self, filename=None):
        self.customers = dict()
        self.images = list()
        self.site_visits = list()
        self.orders = list()
        if filename:
            with open(filename, 'r') as read_file:
                data_list = json.load(read_file)
            for data in data_list:
                self.ingest(data)

    def ingest(self, data):
        if data.get('type') == 'CUSTOMER':
            if data.get('key') in self.customers:
                self.customers.get(data.get('key')).update(data)
            else:
                customer = Customer(data)
                self.customers[customer.key] = customer
        else:
            if data.get('type') == 'IMAGE':
                img = Image(data)
                self.images.append(img)
                customer_id = img.customer_id
                if customer_id not in self.customers:
                    self.customers[customer_id] = Customer({
                        'type': 'CUSTOMER',
                        'key': customer_id
                    })
                self.customers.get(customer_id).images.append(img)
            if data.get('type') == 'SITE_VISIT':
                site_visit = SiteVisit(data)
                self.site_visits.append(site_visit)
                customer_id = site_visit.customer_id
                if customer_id not in self.customers:
                    self.customers[customer_id] = Customer({
                        'type': 'CUSTOMER',
                        'key': customer_id
                    })
                self.customers.get(customer_id).site_visits.append(site_visit)
            if data.get('type') == 'ORDER':
                order = Order(data)
                self.orders.append(order)
                customer_id = order.customer_id
                if customer_id not in self.customers:
                    self.customers[customer_id] = Customer({
                        'type': 'CUSTOMER',
                        'key': customer_id
                    })
                self.customers.get(customer_id).orders.append(order)

    def get_max_min_date(self):
        if len(self.site_visits) == 0:
            return None, None
        maxV = self.site_visits[0].event_time
        minV = self.site_visits[0].event_time
        for site_visit in self.site_visits:
            time = site_visit.event_time
            if time > maxV:
                maxV = time
            if time < minV:
                minV = time
        self.maxV = maxV
        self.minV = minV

    def top_X_Simple_LTV_Customers(self, x):
        def sort(x):
            start_time = x.event_time if x.event_time else self.minV
            weeks = (self.maxV - start_time).days / 7.0
            return x.get_total_expenditure() / weeks
        return sorted(self.customers.values(), key=sort, reverse=True)[:x]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num',
                        type=int,
                        help='Num of Customers')
    parser.add_argument('-f', '--file',
                        required=True,
                        help='file of data')
    args = parser.parse_args()
    analysis = Analysis(args.file)
    analysis.get_max_min_date()
    print analysis.top_X_Simple_LTV_Customers(args.num)


if __name__ == '__main__':
    main()
