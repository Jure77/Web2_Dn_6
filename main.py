#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAddHandler, DetailHandler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert-page"),
    webapp2.Route('/topic/add', TopicAddHandler),
    webapp2.Route('/topic_detail/<details_id:\d+>', DetailHandler),
], debug=True)
