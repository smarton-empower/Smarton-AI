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
## Class RestoreLayoutDialogGUI
###########################################################################

class RestoreLayoutDialogGUI ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Save/Restore Layout", pos = wx.DefaultPosition, size = wx.Size( 253,192 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"If field is not empty, restored elements\n will be put in a group.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Group name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.lbl_group_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_group_name.SetMinSize( wx.Size( 120,-1 ) )

        bSizer5.Add( self.lbl_group_name, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button3 = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button3, 0, wx.ALL, 5 )


        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


