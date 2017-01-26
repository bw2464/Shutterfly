from datetime import date


class Event(object):

    def __init__(self, data):
        self.data = data

    @property
    def type(self):
        raise NotImplementedError('subclasses must override!')

    @property
    def verb(self):
        raise NotImplementedError('subclasses must override!')

    @property
    def event_time(self):
        time_str = self.data.get('event_time')
        if not time_str:
            return None
        time_tokens = time_str.split(':')
        day_tokens = time_tokens[0].split('-')
        return date(int(day_tokens[0]), int(day_tokens[1]), int(day_tokens[2]))
