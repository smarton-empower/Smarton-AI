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
## Class PlaceByReferenceGUI
###########################################################################

class PlaceByReferenceGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Place footprints", pos = wx.DefaultPosition, size = wx.Size( 326,496 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.Size( 257,-1 ), wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"List of footprints:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

        list_footprintsChoices = []
        self.list_footprints = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_footprintsChoices, wx.LB_EXTENDED|wx.LB_NEEDED_SB )
        bSizer3.Add( self.list_footprints, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Arrangement:", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

        com_arrChoices = [ u"Linear", u"Matrix", u"Circular" ]
        self.com_arr = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 110,-1 ), com_arrChoices, wx.CB_READONLY )
        self.com_arr.SetSelection( 0 )
        bSizer5.Add( self.com_arr, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Copy text positions:", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.cb_positions = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_positions.SetValue(True)
        bSizer4.Add( self.cb_positions, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_x_mag = wx.StaticText( self, wx.ID_ANY, u"step x (mm):", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.lbl_x_mag.Wrap( -1 )

        bSizer51.Add( self.lbl_x_mag, 0, wx.ALL, 5 )

        self.val_x_mag = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.val_x_mag, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer51, 0, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_y_angle = wx.StaticText( self, wx.ID_ANY, u"step y (mm):", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.lbl_y_angle.Wrap( -1 )

        bSizer7.Add( self.lbl_y_angle, 0, wx.ALL, 5 )

        self.val_y_angle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.val_y_angle, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer7, 0, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_columns_rad_step = wx.StaticText( self, wx.ID_ANY, u"Nr. columns:", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.lbl_columns_rad_step.Wrap( -1 )

        self.lbl_columns_rad_step.Enable( False )

        bSizer8.Add( self.lbl_columns_rad_step, 0, wx.ALL, 5 )

        self.val_columns_rad_step = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.val_columns_rad_step.Enable( False )

        bSizer8.Add( self.val_columns_rad_step, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer8, 0, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_rotate_n_th = wx.StaticText( self, wx.ID_ANY, u"Rotate every n-th footprint", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.lbl_rotate_n_th.Wrap( -1 )

        bSizer10.Add( self.lbl_rotate_n_th, 0, wx.ALL, 5 )

        self.val_nth = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.val_nth, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer10, 0, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Rotate by", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer11.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.val_rotate = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.val_rotate, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer11, 0, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_cancel = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        bSizer9.Add( self.btn_cancel, 0, wx.ALL, 5 )


        bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_ok = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.btn_ok, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer9, 0, wx.EXPAND, 0 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.list_footprints.Bind( wx.EVT_LISTBOX, self.on_selected )
        self.com_arr.Bind( wx.EVT_COMBOBOX, self.arr_changed )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_selected( self, event ):
        event.Skip()

    def arr_changed( self, event ):
        event.Skip()


