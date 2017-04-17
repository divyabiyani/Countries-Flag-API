#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class CountriesResource(object):
    def getJson(self):
        content = ''
        with open('Countries.json','r') as f:
            content = content + (f.readline())
        return content
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.body = (self.getJson())
# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
countries = CountriesResource()

# things will handle all requests to the '/things' URL path
app.add_route('/countries', countries)
