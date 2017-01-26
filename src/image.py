from event import Event


class Image(Event):

    def __init__(self, data):
        assert data.get('type', None) == 'IMAGE'
        super(Image, self).__init__(data)

    @property
    def type(self):
        return 'IMAGE'

    @property
    def verb(self):
        return self.data.get('verb', None)

    @property
    def key(self):
        return self.data.get('key', None)

    @property
    def customer_id(self):
        return self.data.get('customer_id', None)

    @property
    def camera_make(self):
        return self.data.get('camera_make', None)

    @property
    def camera_model(self):
        return self.data.get('camera_model', None)
