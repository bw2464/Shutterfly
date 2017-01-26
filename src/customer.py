from event import Event


class Customer(Event):
    new = 'NEW'
    update = 'UPDATE'

    def __init__(self, data):
        assert data.get('type', None) == 'CUSTOMER'
        super(Customer, self).__init__(data)
        self.site_visits = list()
        self.images = list()
        self.orders = list()

    @property
    def type(self):
        return 'CUSTOMER'

    @property
    def verb(self):
        if self.data.get('verb') == self.new:
            return self.new
        if self.data.gt('verb') == self.update:
            return self.update
        return None

    @property
    def key(self):
        return self.data.get('key', None)

    @property
    def last_name(self):
        return self.data.get('last_name', None)

    @property
    def adr_city(self):
        return self.data.get('adr_city', None)

    @property
    def adr_state(self):
        return self.data.get('adr_state', None)

    def get_total_visits(self):
        return len(self.site_visits)

    def get_total_expenditure(self):
        total = 0.0
        for order in self.orders:
            total += order.total_amount
        return total

    def update(self, data):
        self.data = data

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key
