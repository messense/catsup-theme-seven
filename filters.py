# -*- coding: utf-8 -*-


def excerpt(text, count=200, suffix=u'...', wrapper=u'p'):
    import re
    summary = re.sub(r'<.*?>', u'', text)
    summary = u' '.join(summary.split())[0:count]
    return u'<{0}>{1}{2}</{0}>'.format(wrapper, summary, suffix)


def sinaimg_large(url):
    if url.find('sinaimg.cn') != -1:
        if url.find('thumbnail') != -1:
            url = url.replace('thumbnail', 'large')
        if url.find('bmiddle') != -1:
            url = url.replace('bmiddle', 'large')
    return url


def sinaimg_middle(url):
    if url.find('sinaimg.cn') != -1:
        if url.find('thumbnail') != -1:
            url = url.replace('thumbnail', 'bmiddle')
        if url.find('large') != -1:
            url = url.replace('large', 'bmiddle')
    return url


def sinaimg_small(url):
    if url.find('sinaimg.cn') != -1:
        if url.find('bmiddle') != -1:
            url = url.replace('bmiddle', 'thumbnail')
        if url.find('large') != -1:
            url = url.replace('large', 'thumbnail')
    return url
