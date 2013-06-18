"""Base controller classes for VTR control.

Copyright 2013 Joshua Hutchins.
"""

__author__ = 'jdhutchin@gmail.com (Joshua Hutchins)'

import collections


Timecode = collections.namedtuple('Timecode', ['hour', 'minute', 'second', 'frame'])


class Error(Exception):
  pass


class VTRController(object):
  """Base class for VTR controller."""
  pass

