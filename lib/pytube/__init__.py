# -*- coding: utf-8 -*-
# flake8: noqa: F401
# noreorder
"""
Pytube: a very serious Python library for downloading YouTube Videos.
"""
__title__ = "pytube3"
__author__ = "Nick Ficano, Harold Martin"
__license__ = "MIT License"
__copyright__ = "Copyright 2019 Nick Ficano"

from .version import __version__
from .streams import Stream
from .captions import Caption
from .query import CaptionQuery
from .query import StreamQuery
from .__main__ import YouTube
from .contrib.playlist import Playlist
