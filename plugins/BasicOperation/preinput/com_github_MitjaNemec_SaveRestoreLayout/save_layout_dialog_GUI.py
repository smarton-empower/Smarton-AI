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
## Class SaveLayoutDialogGUI
###########################################################################

class SaveLayoutDialogGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Save/Restore Layout", pos = wx.DefaultPosition, size = wx.Size( 258,373 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.Size( 258,200 ), wx.DefaultSize )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Hierarchy level:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer14.Add( self.m_staticText5, 0, wx.ALL, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        list_levelsChoices = []
        self.list_levels = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), list_levelsChoices, 0 )
        bSizer18.Add( self.list_levels, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer14.Add( bSizer18, 1, wx.EXPAND, 5 )

        self.cb_intersecting = wx.CheckBox( self, wx.ID_ANY, u"Save intersecting items", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.cb_intersecting, 0, wx.ALL, 5 )

        self.cb_tracks = wx.CheckBox( self, wx.ID_ANY, u"Tracks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_tracks.SetValue(True)
        bSizer14.Add( self.cb_tracks, 0, wx.ALL, 5 )

        self.cb_zones = wx.CheckBox( self, wx.ID_ANY, u"Zones", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_zones.SetValue(True)
        bSizer14.Add( self.cb_zones, 0, wx.ALL, 5 )

        self.cb_text = wx.CheckBox( self, wx.ID_ANY, u"Text items", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_text.SetValue(True)
        bSizer14.Add( self.cb_text, 0, wx.ALL, 5 )

        self.cb_drawings = wx.CheckBox( self, wx.ID_ANY, u"Drawings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_drawings.SetValue(True)
        bSizer14.Add( self.cb_drawings, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn_cancel, 0, wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_ok = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn_ok, 0, wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer14.Add( bSizer6, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.list_levels.Bind( wx.EVT_LISTBOX, self.level_changed )
        self.cb_intersecting.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.cb_tracks.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.cb_zones.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.cb_text.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.cb_drawings.Bind( wx.EVT_CHECKBOX, self.level_changed )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def level_changed( self, event ):
        event.Skip()







