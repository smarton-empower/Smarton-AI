import pcbnew
import os
import wx
import logging
import sys
import math

print("Hello World")
print(pcbnew.PLUGIN_DIRECTORIES_SEARCH)
pcb_file_name="E:\workspace_kicad\complex_hierarchy_5\complex_hierarchy_5.kicad_pcb"
brd=pcbnew.LoadBoard(pcb_file_name)
fps=brd.GetFootprints()
tracks=brd.GetTracks()


