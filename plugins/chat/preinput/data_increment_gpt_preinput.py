# Smarton AI for Kicad - Analying help documentation paragraphs and invoke plugins intelligently
# Copyright (C) 2023 Beijing Smarton Empower
# Contact: yidong.tian@smartonep.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

def data_increment_gpt_preinput():
    Data_Increment_GPTModel_messages = [
        [
            {"role": "system", "content": "Task 1: 1-Introduction to the KiCad Schematic Editor"},
            {"role": "system", "content": "The following 7 Subtasks are the Subtasks of Task 1"},
            {"role": "system", "content": "Subtask 1: 1-Description"},
            {"role": "system", "content": "Subtask 2: 2-Initial Configuration"},
            {"role": "system", "content": "Subtask 3: 3-The Schematic Editor User Interface"},
            {"role": "system", "content": "Subtask 4: 4-Navigating the editing canvas"},
            {"role": "system", "content": "Subtask 5: 5-Hotkeys"},
            {"role": "system", "content": "Subtask 6: 6-Mouse operations and selection"},
            {"role": "system", "content": "Subtask 7: 7-Left toolbar display controls"},
        ],
        [
            {"role": "system", "content": "Task 2: 2-Schematic Creation and Editing"},
            {"role": "system", "content": "The following 12 Subtasks are the Subtasks of Task 2"},
            {"role": "system", "content": "Subtask 1: 1-Introduction"},
            {"role": "system", "content": "Subtask 2: 2-Schematic editing operations"},
            {"role": "system", "content": "Subtask 3: 3-Grids"},
            {"role": "system", "content": "Subtask 4: 4-Snapping"},
            {"role": "system", "content": "Subtask 5: 5-Editing object properties"},
            {"role": "system", "content": "Subtask 6: 6-Working with symbols"},
            {"role": "system", "content": "Subtask 7: 7-Reference Designators and Symbol Annotation"},
            {"role": "system", "content": "Subtask 8: 8-Electrical Connections"},
            {"role": "system", "content": "Subtask 9: 9-Netclasses"},
            {"role": "system", "content": "Subtask 10: 10-Graphical items"},
            {"role": "system", "content": "Subtask 11: 11-Schematic Setup"},
            {"role": "system", "content": "Subtask 12: 12-Rescuing cached symbols"},
        ],
        [
            {"role": "system", "content": "Task 3: 3-Hierarchical schematics"},
            {"role": "system", "content": "The following 5 Subtasks are the Subtasks of Task 3"},
            {"role": "system", "content": "Subtask 1: 1-Introduction"},
            {"role": "system", "content": "Subtask 2: 2-Adding sheets to a design"},
            {"role": "system", "content": "Subtask 3: 3-Navigating between sheets"},
            {"role": "system", "content": "Subtask 4: 4-Electrical connections between sheets"},
            {"role": "system", "content": "Subtask 5: 5-Hierarchical design examples"},
        ],
        [
            {"role": "system", "content": "Task 4: 4-Inspecting a schematic"},
            {"role": "system", "content": "The following 4 Subtasks are the Subtasks of Task 4"},
            {"role": "system", "content": "Subtask 1: 1-Find tool"},
            {"role": "system", "content": "Subtask 2: 2-Net highlighting"},
            {"role": "system", "content": "Subtask 3: 3-Cross-probing from the PCB"},
            {"role": "system", "content": "Subtask 4: 4-Electrical Rules Check"},
        ],
        [
            {"role": "system", "content": "Task 5: 5-Assigning Footprints"},
            {"role": "system", "content": "The following 3 Subtasks are the Subtasks of Task 5"},
            {"role": "system", "content": "Subtask 1: 1-Assigning Footprints in Symbol Properties"},
            {"role": "system", "content": "Subtask 2: 2-Assigning Footprints While Placing Symbols"},
            {"role": "system", "content": "Subtask 3: 3-Assigning Footprints with the Footprint Assignment Tool"},
        ],
        [
            {"role": "system", "content": "Task 6: 6-Forward and back annotation"},
            {"role": "system", "content": "The following 2 Subtasks are the Subtasks of Task 6"},
            {"role": "system", "content": "Subtask 1: 1-Update PCB from Schematic (forward annotation)"},
            {"role": "system", "content": "Subtask 2: 2-Update Schematic from PCB (back annotation)"},
        ],
        [
            {"role": "system", "content": "Task 7: 7-Schematic Editor Generating Outputs"},
            {"role": "system", "content": "The following 4 Subtasks are the Subtasks of Task 7"},
            {"role": "system", "content": "Subtask 1: 1-Printing"},
            {"role": "system", "content": "Subtask 2: 2-Plotting"},
            {"role": "system", "content": "Subtask 3: 3-Generating a Bill of Materials"},
            {"role": "system", "content": "Subtask 4: 4-Generating a Netlist"},
        ],
        [
            {"role": "system", "content": "Task 8: 8-Symbols and Symbol Libraries"},
            {"role": "system", "content": "The following 3 Subtasks are the Subtasks of Task 8"},
            {"role": "system", "content": "Subtask 1: 1-Managing symbol libraries"},
            {"role": "system", "content": "Subtask 2: 2-Creating and editing symbols"},
            {"role": "system", "content": "Subtask 3: 3-Browsing symbol libraries"},
        ],
        [
            {"role": "system", "content": "Task 9: 9-Simulator"},
            {"role": "system", "content": "The following 4 Subtasks are the Subtasks of Task 9"},
            {"role": "system", "content": "Subtask 1: 1-Value notation"},
            {"role": "system", "content": "Subtask 2: 2-Assigning models"},
            {"role": "system", "content": "Subtask 3: 3-SPICE directives"},
            {"role": "system", "content": "Subtask 4: 4-Running simulations"},
        ],
        [
            {"role": "system", "content": "Task 10: 10-Schematic Editor Advanced Topics"},
            {"role": "system", "content": "The following 4 Subtasks are the Subtasks of Task 10"},
            {"role": "system", "content": "Subtask 1: 1-Configuration and Customization"},
            {"role": "system", "content": "Subtask 2: 2-Text variables"},
            {"role": "system", "content": "Subtask 3: 3-Database Libraries"},
            {"role": "system", "content": "Subtask 4: 4-Custom Netlist and BOM Formats"},
        ],
        [
            {"role": "system", "content": "Task 11: 11-Schematic Editor Actions reference"},
            {"role": "system", "content": "The following 2 Subtasks are the Subtasks of Task 11"},
            {"role": "system", "content": "Subtask 1: 1-Schematic Editor"},
            {"role": "system", "content": "Subtask 2: 2-Common"},
        ],
        [
            {"role": "system", "content": "Task 12: 12-Introduction to the KiCad Schematic Editor"},
            {"role": "system", "content": "The following 4 Subtasks are the Subtasks of Task 12"},
            {"role": "system", "content": "Subtask 1: 1-Initial configuration"},
            {"role": "system", "content": "Subtask 2: 2-The PCB Editor user interface"},
            {"role": "system", "content": "Subtask 3: 3-Navigating the editing canvas"},
            {"role": "system", "content": "Subtask 4: 4-Hotkeys"},
        ],
        [
            {"role": "system", "content": "Task 13: 13-Display and selection controls"},
            {"role": "system", "content": "The following 6 Subtasks are the Subtasks of Task 13"},
            {"role": "system", "content": "Subtask 1: 1-Board layers"},
            {"role": "system", "content": "Subtask 2: 2-The appearance panel"},
            {"role": "system", "content": "Subtask 3: 3-Selection and the selection filter"},
            {"role": "system", "content": "Subtask 4: 4-Net highlighting"},
            {"role": "system", "content": "Subtask 5: 5-Cross-probing from the schematic"},
            {"role": "system", "content": "Subtask 6: 6-Left toolbar display controls"},
        ],
        [
            {"role": "system", "content": "Task 14: 14-Creating a PCB"},
            {"role": "system", "content": "The following 5 Subtasks are the Subtasks of Task 14"},
            {"role": "system", "content": "Subtask 1: 1-Basic PCB concepts"},
            {"role": "system", "content": "Subtask 2: 2-Capabilities"},
            {"role": "system", "content": "Subtask 3: 3-Starting from a schematic"},
            {"role": "system", "content": "Subtask 4: 4-Starting from scratch"},
            {"role": "system", "content": "Subtask 5: 5-Board setup"},
        ],
        [
            {"role": "system", "content": "Task 15: 15-Editing a board"},
            {"role": "system", "content": "The following 11 Subtasks are the Subtasks of Task 15"},
            {"role": "system", "content": "Subtask 1: 1-Placement and drawing operations"},
            {"role": "system", "content": "Subtask 2: 2-Snapping"},
            {"role": "system", "content": "Subtask 3: 3-Editing object properties"},
            {"role": "system", "content": "Subtask 4: 4-Working with footprints"},
            {"role": "system", "content": "Subtask 5: 5-Working with pads"},
            {"role": "system", "content": "Subtask 6: 6-Working with zones"},
            {"role": "system", "content": "Subtask 7: 7-Graphical objects"},
            {"role": "system", "content": "Subtask 8: 8-Dimensions"},
            {"role": "system", "content": "Subtask 9: 9-Routing tracks"},
            {"role": "system", "content": "Subtask 10: 10-Forward and back annotation"},
            {"role": "system", "content": "Subtask 11: 11-Locking"},
        ],
        [
            {"role": "system", "content": "Task 16: 16-Inspecting a board"},
            {"role": "system", "content": "The following 6 Subtasks are the Subtasks of Task 16"},
            {"role": "system", "content": "Subtask 1: 1-Measurement tool"},
            {"role": "system", "content": "Subtask 2: 2-Design rule checking"},
            {"role": "system", "content": "Subtask 3: 3-Find tool"},
            {"role": "system", "content": "Subtask 4: 4-Search panel"},
            {"role": "system", "content": "Subtask 5: 5-3D Viewer"},
            {"role": "system", "content": "Subtask 6: 6-Net inspector"},
        ],
        [
            {"role": "system", "content": "Task 17: 17-PCB Editor Generating outputs"},
            {"role": "system", "content": "The following 6 Subtasks are the Subtasks of Task 17"},
            {"role": "system", "content": "Subtask 1: 1-Fabrication outputs and plotting"},
            {"role": "system", "content": "Subtask 2: 2-Drill files"},
            {"role": "system", "content": "Subtask 3: 3-Component placement files"},
            {"role": "system", "content": "Subtask 4: 4-Additional fabrication outputs"},
            {"role": "system", "content": "Subtask 5: 5-Printing"},
            {"role": "system", "content": "Subtask 6: 6-Exporting files"},
        ],
        [
            {"role": "system", "content": "Task 18: 18-Footprints and footprint libraries"},
            {"role": "system", "content": "The following 2 Subtasks are the Subtasks of Task 18"},
            {"role": "system", "content": "Subtask 1: 1-Managing symbol libraries"},
            {"role": "system", "content": "Subtask 2: 2-Creating and editing footprints"},
        ],
        [
            {"role": "system", "content": "Task 19: 19-PCB Editor Advanced topics"},
            {"role": "system", "content": "The following 5 Subtasks are the Subtasks of Task 19"},
            {"role": "system", "content": "Subtask 1: 1-Configuration and Customization"},
            {"role": "system", "content": "Subtask 2: 2-Text variables"},
            {"role": "system", "content": "Subtask 3: 3-Custom design rules"},
            {"role": "system", "content": "Subtask 4: 4-Scripting"},
            {"role": "system", "content": "Subtask 5: 5-Working With IDF Component Outlines"},
        ],
        [
            {"role": "system", "content": "Task 20: 20-PCB Editor Actions reference"},
            {"role": "system", "content": "The following 3 Subtasks are the Subtasks of Task 20"},
            {"role": "system", "content": "Subtask 1: 1-PCB Editor"},
            {"role": "system", "content": "Subtask 2: 2-3D Viewer"},
            {"role": "system", "content": "Subtask 3: 3-Common"},
        ],
    ]
    return Data_Increment_GPTModel_messages