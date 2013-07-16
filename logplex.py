# -*- coding: utf-8 -*-

from datetime import datetime

from packages import requests

class Logplex(object):
    """A Logplex client."""

    def __init__(self, token=None, url=None, timeout=2):
        super(Logplex, self).__init__()

        self.url = url
        self.token = token
        self.timeout = timeout
        self.hostname = 'myhost'
        self.procid = 'lpxc'
        self.msgid = '-'
        self.structured_data = '-'
        self.session = requests.session()

    def format_data(self, data):

        pkt = "<190>1 "
        pkt += datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00 ")
        pkt += '{} '.format(self.hostname)
        pkt += '{} '.format(self.token)
        pkt += '{} '.format(self.procid)
        pkt += '{} '.format(self.msgid)
        pkt += '{} '.format(self.structured_data)
        pkt += data
        return '{} {}'.format(len(pkt), pkt)


    def puts(self, s):

        print s
        print self.format_data(s)

