#!/usr/bin/python

"""Main application class for VTR controller."""

import os
import sys
import wx



base_path = os.getcwdu()
if base_path.endswith('app'):
  base_path = base_path[:-4]
sys.path.append(os.getcwdu())


from vtr import vlccontroller


class ControllerFrame(wx.Frame):

  def __init__(self):
    wx.Frame.__init__(self, None, title='VTRController')
    self._BuildMenu()
    self.Show(True)

  def _BuildMenu(self):
    menuBar = wx.MenuBar()
    filemenu = wx.Menu()
    menuExit = filemenu.Append(wx.ID_EXIT, 'E&xit')
    self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

    menuBar.Append(filemenu, '&File')
    self.SetMenuBar(menuBar)

  def OnExit(self, e):
    self.Close(True)
    sys.exit(0)


def main():
  app = wx.App()
  frame = ControllerFrame()

  app.MainLoop()

if __name__ == '__main__':
  main()
