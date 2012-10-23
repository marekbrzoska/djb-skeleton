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

    tags = ['info', 'warning', 'success', 'error']

    messages = [A(x, y)
                for x, y
                in zip(msgs, tags)
                ]

    return render_to_response(
        'pilot/index.html',
        {
            'messages': messages
        }
    )
