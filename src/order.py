from event import Event


class Order(Event):

    def __init__(self, data):
        assert data.get('type', None) == 'ORDER'
        super(Order, self).__init__(data)

    @property
    def type(self):
        return 'ORDER'

    @property
    def verb(self):
        if self.data.get('verb') == 'NEW':
            return 'NEW'
        elif self.data.get('verb') == 'UPDATE':
            return 'UPDATE'
        return None

    @property
    def key(self):
        return self.data.get('key', None)

    @property
    def customer_id(self):
        return self.data.get('customer_id', None)

    @property
    def total_amount(self):
        value = self.data.get('total_amount', None)
        if not value:
            return None
        return float(value.strip().split(' ')[0])
