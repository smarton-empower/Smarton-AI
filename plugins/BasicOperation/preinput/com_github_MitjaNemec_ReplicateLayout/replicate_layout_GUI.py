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
## Class ReplicateLayoutGUI
###########################################################################

class ReplicateLayoutGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Replicate layout", pos = wx.DefaultPosition, size = wx.Size( 362,655 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.Size( 313,409 ), wx.DefaultSize )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Source hierarchy level:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer14.Add( self.m_staticText5, 0, wx.ALL, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        list_levelsChoices = []
        self.list_levels = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), list_levelsChoices, 0 )
        self.list_levels.SetMinSize( wx.Size( -1,60 ) )

        bSizer18.Add( self.list_levels, 3, wx.ALL|wx.EXPAND, 5 )


        bSizer14.Add( bSizer18, 1, wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Destination sheets:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer14.Add( self.m_staticText6, 0, wx.ALL, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        list_sheetsChoices = []
        self.list_sheets = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,-1 ), list_sheetsChoices, wx.LB_MULTIPLE|wx.LB_NEEDED_SB )
        self.list_sheets.SetMinSize( wx.Size( -1,80 ) )

        bSizer16.Add( self.list_sheets, 2, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )


        bSizer14.Add( bSizer16, 2, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Replicate:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer14.Add( self.m_staticText3, 0, wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.chkbox_tracks = wx.CheckBox( self, wx.ID_ANY, u"Tracks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_tracks.SetValue(True)
        bSizer5.Add( self.chkbox_tracks, 0, wx.ALL, 5 )

        self.chkbox_zones = wx.CheckBox( self, wx.ID_ANY, u"Zones", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_zones.SetValue(True)
        bSizer5.Add( self.chkbox_zones, 0, wx.ALL, 5 )

        self.chkbox_text = wx.CheckBox( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_text.SetValue(True)
        bSizer5.Add( self.chkbox_text, 0, wx.ALL, 5 )

        self.chkbox_drawings = wx.CheckBox( self, wx.ID_ANY, u"Drawings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_drawings.SetValue(True)
        bSizer5.Add( self.chkbox_drawings, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer5, 0, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Group:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer14.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.chkbox_group = wx.CheckBox( self, wx.ID_ANY, u"Replicate group only", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_group.SetToolTip( u"Replicate only footprints that are in the same group as anchor (selected) footprint" )

        bSizer14.Add( self.chkbox_group, 0, wx.ALL, 5 )

        self.chkbox_group_layouts = wx.CheckBox( self, wx.ID_ANY, u"Group layouts", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_group_layouts.SetToolTip( u"Group replicated layouts by hierarchical sheets" )

        bSizer14.Add( self.chkbox_group_layouts, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.chkbox_group_footprints = wx.CheckBox( self, wx.ID_ANY, u"Footprints", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_group_footprints.Enable( False )
        self.chkbox_group_footprints.SetToolTip( u"Add replicated footprints into layout's groups" )

        bSizer6.Add( self.chkbox_group_footprints, 0, wx.ALL, 5 )

        self.chkbox_group_tracks = wx.CheckBox( self, wx.ID_ANY, u"Tracks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_group_tracks.Enable( False )
        self.chkbox_group_tracks.SetToolTip( u"Add replicated tracks into layout's groups" )

        bSizer6.Add( self.chkbox_group_tracks, 0, wx.ALL, 5 )

        self.chkbox_group_zones = wx.CheckBox( self, wx.ID_ANY, u"Zones", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_group_zones.Enable( False )
        self.chkbox_group_zones.SetToolTip( u"Add replicated zones into layout's groups" )

        bSizer6.Add( self.chkbox_group_zones, 0, wx.ALL, 5 )

        self.chkbox_group_text = wx.CheckBox( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_group_text.Enable( False )
        self.chkbox_group_text.SetToolTip( u"Add replicated text into layout's groups" )

        bSizer6.Add( self.chkbox_group_text, 0, wx.ALL, 5 )

        self.chkbox_group_drawings = wx.CheckBox( self, wx.ID_ANY, u"Drawings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_group_drawings.Enable( False )
        self.chkbox_group_drawings.SetToolTip( u"Add replicated drawings into layout's groups" )

        bSizer6.Add( self.chkbox_group_drawings, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer6, 0, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Replicate locked:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer14.Add( self.m_staticText4, 0, wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.chkbox_locked = wx.CheckBox( self, wx.ID_ANY, u"Footprints", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_locked.SetToolTip( u"Replicate also locked footprints" )

        bSizer6.Add( self.chkbox_locked, 0, wx.ALL, 5 )

        self.chkbox_locked_tracks = wx.CheckBox( self, wx.ID_ANY, u"Tracks", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.chkbox_locked_tracks, 0, wx.ALL, 5 )

        self.chkbox_locked_zones = wx.CheckBox( self, wx.ID_ANY, u"Zones", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.chkbox_locked_zones, 0, wx.ALL, 5 )

        self.chkbox_locked_text = wx.CheckBox( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.chkbox_locked_text, 0, wx.ALL, 5 )

        self.chkbox_locked_drawings = wx.CheckBox( self, wx.ID_ANY, u"Drawings", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.chkbox_locked_drawings, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer6, 0, wx.EXPAND, 5 )

        self.chkbox_intersecting = wx.CheckBox( self, wx.ID_ANY, u"Replicate intersecting tracks/zones/drawings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_intersecting.SetToolTip( u"Replicate also items that cross source bounding box boundary" )

        bSizer14.Add( self.chkbox_intersecting, 0, wx.ALL, 5 )

        self.chkbox_include_group_items = wx.CheckBox( self, wx.ID_ANY, u"Include group items", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.chkbox_include_group_items.Enable( False )
        self.chkbox_include_group_items.SetToolTip( u"Replicate group items outside of source bounding box if they are members of the source group" )

        bSizer14.Add( self.chkbox_include_group_items, 0, wx.ALL, 5 )

        self.chkbox_remove = wx.CheckBox( self, wx.ID_ANY, u"Remove existing tracks/zones/drawings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_remove.SetToolTip( u"Remove item existing in the destination bounding box before replication" )

        bSizer14.Add( self.chkbox_remove, 0, wx.ALL, 5 )

        self.chkbox_remove_duplicates = wx.CheckBox( self, wx.ID_ANY, u"Remove duplicates (might take some time)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.chkbox_remove_duplicates.SetToolTip( u"Remove duplicate items (track over track, zone over zone). Useful if you run the plugin multiple times" )

        bSizer14.Add( self.chkbox_remove_duplicates, 0, wx.ALL, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.btn_cancel, 0, wx.ALL, 5 )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_ok = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.btn_ok, 0, wx.ALL, 5 )


        bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer14.Add( bSizer15, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_cancel )
        self.list_levels.Bind( wx.EVT_LISTBOX, self.level_changed )
        self.list_sheets.Bind( wx.EVT_LISTBOX, self.destination_selected )
        self.chkbox_tracks.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_zones.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_text.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_drawings.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_group.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_group_layouts.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_group_footprints.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_group_tracks.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_group_zones.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_group_text.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_group_drawings.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_locked_tracks.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_locked_zones.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_locked_text.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_locked_drawings.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_intersecting.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.chkbox_include_group_items.Bind( wx.EVT_CHECKBOX, self.level_changed )
        self.btn_cancel.Bind( wx.EVT_BUTTON, self.on_cancel )
        self.btn_ok.Bind( wx.EVT_BUTTON, self.on_ok )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_cancel( self, event ):
        event.Skip()

    def level_changed( self, event ):
        event.Skip()

    def destination_selected( self, event ):
        event.Skip()



















    def on_ok( self, event ):
        event.Skip()


