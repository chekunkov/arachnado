# -*- coding: utf-8 -*-
from __future__ import absolute_import  
import functools
from scrapy.utils.serialize import ScrapyJSONEncoder

from tornado import gen
from twisted.internet.defer import Deferred
from twisted.internet import reactor


def tt_coroutine(func):
    """
    Twisted-Tornado coroutine which uses tornago.gen inside,
    but returns Twisted Deferred to the outside.
    """
    return gen_to_twisted(gen.coroutine(func))


def wrap_future(future):
    """
    Wrap tornado.concurrent.Future in a twisted.internet.defer.Deferred.
    Only basics are supported: callback, errback.
    """
    d = Deferred()

    def callback(future):
        e = future.exception()
        if e:
            reactor.callFromThread(d.errback, e)
            return
        reactor.callFromThread(d.callback, future.result())

    future.add_done_callback(callback)
    return d


def gen_to_twisted(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return wrap_future(func(*args, **kwargs))
    return wrapper


# XXX: this is copy-pasted to make motor_exporter independent
_encoder = ScrapyJSONEncoder(ensure_ascii=False)
def json_encode(obj):
    """
    Encode a Python object to JSON.
    Unlike standard json.dumps, datetime.datetime objects are supported.
    """
    return _encoder.encode(obj)
