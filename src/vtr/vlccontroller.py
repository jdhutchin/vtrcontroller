"""Classes for controlling VLC with VTR controller.

Copyright 2013 Joshua Hutchins.
"""

__author__ = 'jdhutchin@gmail.com (Joshua Hutchins)'


import threading
import socket

import controller


class VLCController(controller.VTRController):

  def __init__(self, host, port):
    self.host = host
    self.port = port
    self._socket = None
    self._lock = threading.Lock()

  def Open(self):
    with self._lock:
      if self._socket:
        return
      self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self._socket.connect((self.host, self.port))


  def Close(self):
    with self._lock:
      if not self._socket:
        return
      try:
        self._socket.Close()
      finally:
        self._socket = None

  def _SendCommand(self, cmd):
    with self._lock:
      self._socket.send('%s\n' % cmd)
      self._socket.recv()

  def Play(self):
    self._SendCommand('normal')
    self._SendCommand('play')

  def Pause(self):
    self._SendCommand('pause')

