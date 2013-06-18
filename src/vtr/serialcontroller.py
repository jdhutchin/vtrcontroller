"""Controller for VTR's using the Sony 9-pin protocol or a variant.

Copyright 2013 Joshua Hutchins."""

import threading
import serial

import controller


Timecode = controller.Timecode


class ChecksumError(controller.Error):
  pass


class CommandFactory(object):
  """Factory for generating various VTR commands."""

  def PlayCommand(self):
    return 


class Command(object):
  """Command for VTR."""

  def CommandBytes(self):
    """Return an array of the two command bytes."""
    raise NotImplementedError()

  def DataBytes(self):
    """Return an array of the data bytes, or an empty array."""
    return []


  def ProcessResult(self, bytes):
    """Process the bytes that the VTR sent back."""
    pass


class BaseSimpleCommand(Command):

  def ProcessResult(self, bytes):
    if bytes[0] == 0x11:
      raise controller.Error('Error code %x' % bytes[2])


class SerialVTRController(controller.VTRController):
  """Class to work with VTR controllers that use a 9-pin protocol."""

  def __init__(self, port, command_factory):
    self.port_name = port
    self.opened = False
    self._port = None
    self._command_factory = command_factory
    self._lock = threading.Lock()

  def Open(self):
    with self._lock:
      self._port = serial.Serial(port=self.port_name,
                                 baudrate=38400)
      self._port.open()

  def Close(self):
    with self._lock:
      if self._port:
        self._port.close()
        self._port = None

  def _SendCommand(self, command):
    """Send a command and return the response."""
    bytes = command.CommandBytes() + command.DataBytes()

    assert len(command.DataBytes()) == command.CommandBytes()[0] & 0xF

    checksum = sum(bytes) & 0xFF
    with self._lock:
      self._port.write(bytes + [checksum])
      self._port.flush()
      response = [self._port.read(size=1)]
      resp_data = response[0] & 0xF
      response += [self._port.read(size=resp_data+1)]
      checksum = self._port.read(size=1)
    if checksum != sum(response) & 0xFF:
      raise ChecksumError('Error receiving response')
    command.ProcessResult(response)



