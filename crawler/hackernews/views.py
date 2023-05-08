from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, RedirectView, View
from django.http.response import StreamingHttpResponse
import requests
# Create your views here.

JS = False


class Echo(TemplateView):
    template_name = ''

    def response_class(self, *args, **kwargs):
        return StreamingHttpResponse('<!DOCTYPE html><html><head><meta charset="utf-8"><title></title></head><body>Hi</body></html>')


class HackerNewsProxyOther(RedirectView):
    url = 'https://news.ycombinator.com/'

    def get_redirect_url(self, *args, **kwargs):
        return f'{super().get_redirect_url(*args, **kwargs)}{self.request.path.strip("/")}'


class HackerNewsProxyHnJs(View):

    def dispatch(self, request, *args, **kwargs):
        if JS:
            with open(f'{settings.MEDIA_DIR}/item_files/hn.js', 'r', encoding="utf-8") as file:
                return StreamingHttpResponse(file.readlines(), headers={'Content-Type': 'application/javascript; charset=UTF-8"'})
        return HackerNewsProxyOther.as_view()(request, *args, **kwargs)

class HackerNewsProxy(TemplateView):
    template_name = ''
    url = 'https://news.ycombinator.com/item'
    source = ()

    def response_class(self, request, *args, **kwargs):
        if JS:
            return StreamingHttpResponse(self.get_request(request))
        return StreamingHttpResponse(self.word_generator(request))

    def get_request(self, request):
        return requests.get(f'{self.url}?{request.GET.urlencode()}', timeout=5000, stream=True)

    def set_source(self, request):
        # with open(item.raw, 'r', encoding='utf-8') as source:
        self.source = (line for line in self.get_request(request).iter_lines(decode_unicode=True))
        return self.source

    def get_line(self):
        # line = source.readline()
        line = next(self.source, '')
        return line

    def word_generator(self, request):
        self.set_source(request)
        line = self.get_line()

        while line:
            first, splitter, line = line.partition('<div class="comment">')
            if not splitter:
                first, splitter, line = first.partition("<div class='comment'>")

            yield first
            yield splitter

            if splitter:
                line = (yield from self.started(line or self.get_line()))

            line = line or self.get_line()


    def started(self, line):
        while line:
            # print('_____________________________________________________________')
            # print(line)
            # print('_____________________________________________________________')
            first, splitter, line = line.partition('<div class="reply">')
            if not splitter:
                first, splitter, line = first.partition("<div class='reply'>")


            if first:
                # first.replace('', '') # some regexp

                skip = False
                count = 0
                for letter in first:

                    if not skip and letter in (' ', ',', '.', '<', '>', '\n'):
                        if count == 6:
                            yield '™'
                        count = 0

                    if letter == '<':
                        skip = True
                        count = 0

                    elif skip and letter == '>':
                        skip = False
                        count = 0

                    elif not skip:
                        if letter.isalpha():
                            count = count + 1
                        else:
                            count = 0

                    yield letter

            if splitter:
                yield splitter
                return line

            line = line or self.get_line()
