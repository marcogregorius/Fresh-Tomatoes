#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:11:12 2017

@author: gregoriusmarco
"""
# Defining class of Movie
class Movie(object):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title=title
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube_url

