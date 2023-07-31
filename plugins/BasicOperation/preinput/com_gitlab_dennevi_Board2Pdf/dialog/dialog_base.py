# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SettingsDialogBase
###########################################################################

class SettingsDialogBase ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Board2Pdf", pos = wx.DefaultPosition, size = wx.Size( 900,670 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.BORDER_DEFAULT )

        self.SetSizeHints( wx.Size( 900,670 ), wx.DefaultSize )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class SettingsDialogPanel
###########################################################################

class SettingsDialogPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,760 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer30 = wx.BoxSizer( wx.VERTICAL )

        sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"General Settings" ), wx.VERTICAL )

        bSizer32 = wx.BoxSizer( wx.VERTICAL )

        sortingSizer = wx.StaticBoxSizer( wx.StaticBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Enabled Templates" ), wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        templatesSortOrderBoxChoices = []
        self.templatesSortOrderBox = wx.ListBox( sortingSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, templatesSortOrderBoxChoices, wx.LB_SINGLE|wx.BORDER_SIMPLE )
        self.templatesSortOrderBox.SetToolTip( u"Double-click to disable template" )

        bSizer6.Add( self.templatesSortOrderBox, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_button_template_up = wx.Button( sortingSizer.GetStaticBox(), wx.ID_ANY, u"Up", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_template_up.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_BUTTON ) )
        self.m_button_template_up.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer5.Add( self.m_button_template_up, 0, wx.ALL, 5 )

        self.m_button_template_down = wx.Button( sortingSizer.GetStaticBox(), wx.ID_ANY, u"Down", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_template_down.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ) )
        self.m_button_template_down.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer5.Add( self.m_button_template_down, 0, wx.ALL, 5 )

        self.m_button_template_new = wx.Button( sortingSizer.GetStaticBox(), wx.ID_ANY, u"New", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_template_new.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_BUTTON ) )
        self.m_button_template_new.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer5.Add( self.m_button_template_new, 0, wx.ALL, 5 )

        self.m_button_template_copy = wx.Button( sortingSizer.GetStaticBox(), wx.ID_ANY, u"Clone", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_template_copy.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_COPY, wx.ART_BUTTON ) )
        self.m_button_template_copy.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer5.Add( self.m_button_template_copy, 0, wx.ALL, 5 )

        self.m_button_template_disable = wx.Button( sortingSizer.GetStaticBox(), wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_template_disable.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
        self.m_button_template_disable.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer5.Add( self.m_button_template_disable, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer5, 0, wx.ALIGN_RIGHT, 5 )


        sortingSizer.Add( bSizer4, 1, wx.EXPAND, 5 )

        self.m_staticText81 = wx.StaticText( sortingSizer.GetStaticBox(), wx.ID_ANY, u"Note! Template at the top of the list will become page one in pdf, and so on.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        sortingSizer.Add( self.m_staticText81, 0, wx.ALL, 5 )


        bSizer32.Add( sortingSizer, 1, wx.ALL|wx.EXPAND, 5 )

        layersSizer = wx.StaticBoxSizer( wx.StaticBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Disabled Templates" ), wx.VERTICAL )

        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer61 = wx.BoxSizer( wx.VERTICAL )

        disabledTemplatesSortOrderBoxChoices = []
        self.disabledTemplatesSortOrderBox = wx.ListBox( layersSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, disabledTemplatesSortOrderBoxChoices, wx.LB_SINGLE|wx.LB_SORT|wx.BORDER_SIMPLE )
        self.disabledTemplatesSortOrderBox.SetToolTip( u"Double-click to enable template" )

        bSizer61.Add( self.disabledTemplatesSortOrderBox, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer41.Add( bSizer61, 1, wx.EXPAND, 5 )

        bSizer51 = wx.BoxSizer( wx.VERTICAL )

        self.m_button_template_enable = wx.Button( layersSizer.GetStaticBox(), wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_template_enable.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
        self.m_button_template_enable.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer51.Add( self.m_button_template_enable, 0, wx.ALL, 5 )

        self.m_button4 = wx.Button( layersSizer.GetStaticBox(), wx.ID_ANY, u"Del", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button4.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_BUTTON ) )
        self.m_button4.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer51.Add( self.m_button4, 0, wx.ALL, 5 )


        bSizer41.Add( bSizer51, 0, wx.ALIGN_RIGHT, 5 )


        layersSizer.Add( bSizer41, 1, wx.EXPAND, 5 )


        bSizer32.Add( layersSizer, 1, wx.ALL|wx.EXPAND, 5 )

        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Settings" ), wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText8 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Output Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        fgSizer1.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.outputDirPicker = wx.DirPickerCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select bom folder", wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRP_USE_TEXTCTRL|wx.BORDER_SIMPLE )
        fgSizer1.Add( self.outputDirPicker, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


        sbSizer6.Add( fgSizer1, 1, wx.EXPAND, 5 )

        bSizer201 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox_create_svg = wx.CheckBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Create SVGs", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer201.Add( self.m_checkBox_create_svg, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_checkBox_delete_single_page_files = wx.CheckBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Delete single page files", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer201.Add( self.m_checkBox_delete_single_page_files, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_checkBox_delete_temp_files = wx.CheckBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Delete temporary files", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer201.Add( self.m_checkBox_delete_temp_files, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        sbSizer6.Add( bSizer201, 1, wx.ALIGN_RIGHT, 5 )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText82 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Library for coloring:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText82.Wrap( -1 )

        bSizer21.Add( self.m_staticText82, 0, wx.ALL, 5 )

        self.m_radio_fitz = wx.RadioButton( sbSizer6.GetStaticBox(), wx.ID_ANY, u"PyMuPdf/fitz (fast)", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        bSizer21.Add( self.m_radio_fitz, 0, wx.ALL, 5 )

        self.m_radio_pypdf = wx.RadioButton( sbSizer6.GetStaticBox(), wx.ID_ANY, u"pypdf (slow)", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.m_radio_pypdf, 0, wx.ALL, 5 )


        sbSizer6.Add( bSizer21, 1, wx.EXPAND, 5 )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Library for merging:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer22.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_radio_merge_fitz = wx.RadioButton( sbSizer6.GetStaticBox(), wx.ID_ANY, u"PyMuPdf/fitz (fast)", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        bSizer22.Add( self.m_radio_merge_fitz, 0, wx.ALL, 5 )

        self.m_radio_merge_pypdf = wx.RadioButton( sbSizer6.GetStaticBox(), wx.ID_ANY, u"pypdf (slow)", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.m_radio_merge_pypdf, 0, wx.ALL, 5 )


        sbSizer6.Add( bSizer22, 1, wx.EXPAND, 5 )

        bSizer39 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button41 = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Save current settings", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_DEFAULT )

        self.m_button41.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
        self.m_button41.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer39.Add( self.m_button41, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer39.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button42 = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Perform", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_DEFAULT|wx.BORDER_RAISED )

        self.m_button42.SetDefault()

        self.m_button42.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PRINT, wx.ART_CMN_DIALOG ) )
        self.m_button42.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer39.Add( self.m_button42, 0, wx.ALL, 5 )

        self.m_button43 = wx.Button( sbSizer6.GetStaticBox(), wx.ID_CANCEL, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_DEFAULT )

        self.m_button43.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_CMN_DIALOG ) )
        self.m_button43.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer39.Add( self.m_button43, 0, wx.ALL, 5 )


        sbSizer6.Add( bSizer39, 0, wx.EXPAND, 5 )

        self.m_progress = wx.Gauge( sbSizer6.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 400,-1 ), wx.GA_HORIZONTAL )
        self.m_progress.SetValue( 0 )
        sbSizer6.Add( self.m_progress, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText_status = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_status.Wrap( -1 )

        sbSizer6.Add( self.m_staticText_status, 0, wx.ALL, 5 )


        bSizer32.Add( sbSizer6, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer22.Add( bSizer32, 1, wx.EXPAND, 5 )


        bSizer30.Add( sbSizer22, 1, wx.EXPAND, 5 )


        bSizer20.Add( bSizer30, 1, wx.EXPAND, 5 )

        bSizer301 = wx.BoxSizer( wx.VERTICAL )

        sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Template Settings" ), wx.VERTICAL )

        m_sizer_template = wx.BoxSizer( wx.VERTICAL )

        sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Template Properties" ), wx.VERTICAL )

        gSizer1 = wx.GridSizer( 3, 2, 0, 0 )

        self.m_staticText_template_name = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Template name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_template_name.Wrap( -1 )

        gSizer1.Add( self.m_staticText_template_name, 0, wx.ALL, 5 )

        self.m_textCtrl_template_name = wx.TextCtrl( sbSizer61.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 190,-1 ), 0 )
        gSizer1.Add( self.m_textCtrl_template_name, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText_frame_layer = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Draw frame on layer", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_frame_layer.Wrap( -1 )

        gSizer1.Add( self.m_staticText_frame_layer, 0, wx.ALL, 5 )

        m_comboBox_frameChoices = []
        self.m_comboBox_frame = wx.ComboBox( sbSizer61.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 190,-1 ), m_comboBox_frameChoices, 0 )
        gSizer1.Add( self.m_comboBox_frame, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_checkBox_mirror = wx.CheckBox( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Mirror all layers (bottom view)", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_checkBox_mirror, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_checkBox_tent = wx.CheckBox( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Do not tent vias on solder mask", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_checkBox_tent, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        sbSizer61.Add( gSizer1, 1, wx.EXPAND, 5 )


        m_sizer_template.Add( sbSizer61, 0, wx.ALL|wx.EXPAND, 5 )

        sbSizer611 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Layer Properties" ), wx.VERTICAL )

        gSizer2 = wx.GridSizer( 0, 4, 0, 0 )

        self.m_staticText_layer_color = wx.StaticText( sbSizer611.GetStaticBox(), wx.ID_ANY, u"Layer color", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_layer_color.Wrap( -1 )

        gSizer2.Add( self.m_staticText_layer_color, 0, wx.ALL, 5 )

        self.m_textCtrl_color = wx.TextCtrl( sbSizer611.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_textCtrl_color, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_color_shower = wx.StaticText( sbSizer611.GetStaticBox(), wx.ID_ANY, u"test", wx.DefaultPosition, wx.Size( 80,20 ), 0 )
        self.m_color_shower.Wrap( -1 )

        self.m_color_shower.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        gSizer2.Add( self.m_color_shower, 0, wx.ALL, 5 )

        self.m_button_pick_color = wx.Button( sbSizer611.GetStaticBox(), wx.ID_ANY, u"Pick Color", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )

        self.m_button_pick_color.SetBitmapMargins( wx.Size( 2,-1 ) )
        gSizer2.Add( self.m_button_pick_color, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        sbSizer611.Add( gSizer2, 1, wx.EXPAND, 5 )

        gSizer3 = wx.GridSizer( 0, 3, 0, 0 )

        self.m_checkBox_negative = wx.CheckBox( sbSizer611.GetStaticBox(), wx.ID_ANY, u"Negative plot", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_checkBox_negative, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_checkBox_reference_designators = wx.CheckBox( sbSizer611.GetStaticBox(), wx.ID_ANY, u"Plot ref. designators", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_checkBox_reference_designators, 0, wx.ALL, 5 )

        self.m_checkBox_footprint_values = wx.CheckBox( sbSizer611.GetStaticBox(), wx.ID_ANY, u"Plot footprint values", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_checkBox_footprint_values, 0, wx.ALL, 5 )


        sbSizer611.Add( gSizer3, 1, wx.EXPAND, 5 )


        m_sizer_template.Add( sbSizer611, 0, wx.ALL|wx.EXPAND, 5 )

        sortingSizer1 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Enabled Layers" ), wx.VERTICAL )

        bSizer512 = wx.BoxSizer( wx.VERTICAL )

        bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer62 = wx.BoxSizer( wx.VERTICAL )

        layersSortOrderBoxChoices = []
        self.layersSortOrderBox = wx.ListBox( sortingSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, layersSortOrderBoxChoices, wx.LB_SINGLE|wx.BORDER_SIMPLE )
        self.layersSortOrderBox.SetToolTip( u"Double-click to disable layer" )

        bSizer62.Add( self.layersSortOrderBox, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer42.Add( bSizer62, 1, wx.EXPAND, 5 )

        bSizer52 = wx.BoxSizer( wx.VERTICAL )

        self.m_button_layer_up = wx.Button( sortingSizer1.GetStaticBox(), wx.ID_ANY, u"Up", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_layer_up.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_BUTTON ) )
        self.m_button_layer_up.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer52.Add( self.m_button_layer_up, 0, wx.ALL, 5 )

        self.m_button_layer_down = wx.Button( sortingSizer1.GetStaticBox(), wx.ID_ANY, u"Down", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_layer_down.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ) )
        self.m_button_layer_down.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer52.Add( self.m_button_layer_down, 0, wx.ALL, 5 )

        self.m_button_layer_disable = wx.Button( sortingSizer1.GetStaticBox(), wx.ID_ANY, u"Disable", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_layer_disable.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
        self.m_button_layer_disable.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer52.Add( self.m_button_layer_disable, 0, wx.ALL, 5 )


        bSizer42.Add( bSizer52, 0, wx.ALIGN_RIGHT, 5 )


        bSizer512.Add( bSizer42, 1, wx.EXPAND, 5 )

        self.m_staticText_layer_info = wx.StaticText( sortingSizer1.GetStaticBox(), wx.ID_ANY, u"Note! Layers at the top of the list will be drawn on top of layers further down.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_layer_info.Wrap( -1 )

        bSizer512.Add( self.m_staticText_layer_info, 0, wx.ALL, 5 )


        sortingSizer1.Add( bSizer512, 1, wx.EXPAND, 5 )


        m_sizer_template.Add( sortingSizer1, 1, wx.ALL|wx.EXPAND, 5 )

        layersSizer1 = wx.StaticBoxSizer( wx.StaticBox( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Disabled Layers" ), wx.VERTICAL )

        bSizer411 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer611 = wx.BoxSizer( wx.VERTICAL )

        disabledLayersSortOrderBoxChoices = []
        self.disabledLayersSortOrderBox = wx.ListBox( layersSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, disabledLayersSortOrderBoxChoices, wx.LB_SINGLE|wx.LB_SORT|wx.BORDER_SIMPLE )
        self.disabledLayersSortOrderBox.SetToolTip( u"Double-click to enable layer" )

        bSizer611.Add( self.disabledLayersSortOrderBox, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer411.Add( bSizer611, 1, wx.EXPAND, 5 )

        bSizer511 = wx.BoxSizer( wx.VERTICAL )

        self.m_button_layer_enable = wx.Button( layersSizer1.GetStaticBox(), wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.Size( 70,30 ), 0|wx.BORDER_DEFAULT )

        self.m_button_layer_enable.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
        self.m_button_layer_enable.SetBitmapMargins( wx.Size( 2,-1 ) )
        bSizer511.Add( self.m_button_layer_enable, 0, wx.ALL, 5 )


        bSizer411.Add( bSizer511, 0, wx.ALIGN_RIGHT, 5 )


        layersSizer1.Add( bSizer411, 1, wx.EXPAND, 5 )


        m_sizer_template.Add( layersSizer1, 1, wx.ALL|wx.EXPAND, 5 )


        sbSizer23.Add( m_sizer_template, 1, wx.EXPAND, 5 )


        bSizer301.Add( sbSizer23, 1, wx.EXPAND, 5 )


        bSizer20.Add( bSizer301, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer20 )
        self.Layout()

        # Connect Events
        self.templatesSortOrderBox.Bind( wx.EVT_LISTBOX, self.OnTemplateEdit )
        self.templatesSortOrderBox.Bind( wx.EVT_LISTBOX_DCLICK, self.OnTemplateDisable )
        self.m_button_template_up.Bind( wx.EVT_BUTTON, self.OnTemplateSortOrderUp )
        self.m_button_template_down.Bind( wx.EVT_BUTTON, self.OnTemplateSortOrderDown )
        self.m_button_template_new.Bind( wx.EVT_BUTTON, self.OnTemplateNew )
        self.m_button_template_copy.Bind( wx.EVT_BUTTON, self.OnTemplateClone )
        self.m_button_template_disable.Bind( wx.EVT_BUTTON, self.OnTemplateDisable )
        self.disabledTemplatesSortOrderBox.Bind( wx.EVT_LISTBOX_DCLICK, self.OnTemplateEnable )
        self.m_button_template_enable.Bind( wx.EVT_BUTTON, self.OnTemplateEnable )
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnTemplateDelete )
        self.m_button41.Bind( wx.EVT_BUTTON, self.OnSaveSettings )
        self.m_button42.Bind( wx.EVT_BUTTON, self.OnPerform )
        self.m_button43.Bind( wx.EVT_BUTTON, self.OnExit )
        self.m_textCtrl_template_name.Bind( wx.EVT_TEXT, self.OnTemplateNameChange )
        self.m_textCtrl_color.Bind( wx.EVT_TEXT, self.OnSaveLayer )
        self.m_button_pick_color.Bind( wx.EVT_BUTTON, self.OnPickColor )
        self.m_checkBox_negative.Bind( wx.EVT_CHECKBOX, self.OnSaveLayer )
        self.m_checkBox_reference_designators.Bind( wx.EVT_CHECKBOX, self.OnSaveLayer )
        self.m_checkBox_footprint_values.Bind( wx.EVT_CHECKBOX, self.OnSaveLayer )
        self.layersSortOrderBox.Bind( wx.EVT_LISTBOX, self.OnLayerEdit )
        self.layersSortOrderBox.Bind( wx.EVT_LISTBOX_DCLICK, self.OnLayerDisable )
        self.m_button_layer_up.Bind( wx.EVT_BUTTON, self.OnLayerSortOrderUp )
        self.m_button_layer_down.Bind( wx.EVT_BUTTON, self.OnLayerSortOrderDown )
        self.m_button_layer_disable.Bind( wx.EVT_BUTTON, self.OnLayerDisable )
        self.disabledLayersSortOrderBox.Bind( wx.EVT_LISTBOX_DCLICK, self.OnLayerEnable )
        self.m_button_layer_enable.Bind( wx.EVT_BUTTON, self.OnLayerEnable )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnTemplateEdit( self, event ):
        event.Skip()

    def OnTemplateDisable( self, event ):
        event.Skip()

    def OnTemplateSortOrderUp( self, event ):
        event.Skip()

    def OnTemplateSortOrderDown( self, event ):
        event.Skip()

    def OnTemplateNew( self, event ):
        event.Skip()

    def OnTemplateClone( self, event ):
        event.Skip()


    def OnTemplateEnable( self, event ):
        event.Skip()


    def OnTemplateDelete( self, event ):
        event.Skip()

    def OnSaveSettings( self, event ):
        event.Skip()

    def OnPerform( self, event ):
        event.Skip()

    def OnExit( self, event ):
        event.Skip()

    def OnTemplateNameChange( self, event ):
        event.Skip()

    def OnSaveLayer( self, event ):
        event.Skip()

    def OnPickColor( self, event ):
        event.Skip()




    def OnLayerEdit( self, event ):
        event.Skip()

    def OnLayerDisable( self, event ):
        event.Skip()

    def OnLayerSortOrderUp( self, event ):
        event.Skip()

    def OnLayerSortOrderDown( self, event ):
        event.Skip()


    def OnLayerEnable( self, event ):
        event.Skip()



