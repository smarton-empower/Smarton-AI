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
## Class InitialDialogGUI
###########################################################################

class InitialDialogGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Place footprints", pos = wx.DefaultPosition, size = wx.Size( 242,107 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Place by?", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_reference = wx.Button( self, wx.ID_ANY, u"Reference nr.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn_reference.SetToolTip( u"This will place footprints which are consecutively numbered with respect to currently selected one. When the footprint selection is ready to place, the plugin sorts this list by reference number." )

        bSizer2.Add( self.btn_reference, 0, wx.ALL, 5 )

        self.btn_sheet = wx.Button( self, wx.ID_ANY, u"Sheet nr.", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.btn_sheet.SetDefault()
        self.btn_sheet.SetToolTip( u"This will place only (and only) footprints from copies of the same sheet as is the currently selected one in. Once the sheet selection is ready, plugin figures out which Footprints it needs to place and sort these footprint by the reference number." )

        bSizer2.Add( self.btn_sheet, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btn_reference.Bind( wx.EVT_BUTTON, self.on_by_reference )
        self.btn_sheet.Bind( wx.EVT_BUTTON, self.on_by_sheet )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_by_reference( self, event ):
        event.Skip()

    def on_by_sheet( self, event ):
        event.Skip()


