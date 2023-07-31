# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ConnIssueGUI
###########################################################################

class ConnIssueGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Replicate Layout", pos = wx.DefaultPosition, size = wx.Size( 346,443 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Looks like the design has an exotic connectivity \nthat is not supported by the plugin", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Make sure that you check the connectivity around:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer1.Add( self.list, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


