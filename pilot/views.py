from django.contrib import messages

from project.utils.djangojinja2 import render_to_response


def home(request):
    class A(object):
        def __init__(self, string, tag):
            self.string = string
            self.tags = tag

        def __unicode__(self):
            return self.string

    msgs = ['quantu solor, lal',
            'dolor medit amse, lla',
            'msg1,',
            ' lorem ipsum']

    msg_types = ['info', 'warning', 'success', 'error']

    for msg, msg_type in zip(msgs, msg_types):
        getattr(messages, msg_type)(request, msg)

    return render_to_response(
        'pilot/index.html', {}, request)
