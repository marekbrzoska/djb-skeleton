from django.contrib import messages
from django.forms.util import ErrorList

from project.utils.djangojinja2 import render_to_response

from . import forms


def home(request):
    msgs = ['quantu solor, lal',
            'dolor medit amse, lla',
            'msg1,',
            'lorem ipsum']

    msg_types = ['info', 'warning', 'success', 'error']

    for msg, msg_type in zip(msgs, msg_types):
        getattr(messages, msg_type)(request, msg)

    return render_to_response(
        'pilot/index.html', {}, request)


def form(request):
    form = forms.Form({'email': 'lsla', 'name': 'Marek'})
    form.errors['__all__'] = ErrorList([u'Great error', u'small error'])
    return render_to_response('pilot/form.html', {'form': form}, request)
