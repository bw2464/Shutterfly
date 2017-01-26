from event import Event


class SiteVisit(Event):

    def __init__(self, data):
        assert data.get('type', None) == 'SITE_VISIT'
        super(SiteVisit, self).__init__(data)

    @property
    def type(self):
        return 'SITE_VISIT'

    @property
    def verb(self):
        return 'NEW'

    @property
    def key(self):
        return self.data.get('key', None)

    @property
    def customer_id(self):
        return self.data.get('customer_id', None)

    @property
    def tags(self):
        return self.data.get('tags', None)
