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

def main_gpt_preinput(
        number_of_task=20,
        pre_description=2
):
    tasks = {
        'Task 1': '1-Introduction to the KiCad Schematic Editor',
        'Task 2': '2-Schematic Creation and Editing',
        'Task 3': '3-Hierarchical schematics',
        'Task 4': '4-Inspecting a schematic',
        'Task 5': '5-Assigning Footprints',
        'Task 6': '6-Forward and back annotation',
        'Task 7': '7-Schematic Editor Generating Outputs',
        'Task 8': '8-Symbols and Symbol Libraries',
        'Task 9': '9-Simulator',
        'Task 10': '10-Schematic Editor Advanced Topics',
        'Task 11': '11-Schematic Editor Actions reference',
        'Task 12': '12-Introduction to the KiCad PCB Editor',
        'Task 13': '13-Display and selection controls',
        'Task 14': '14-Creating a PCB',
        'Task 15': '15-Editing a board',
        'Task 16': '16-Inspecting a board',
        'Task 17': '17-PCB Editor Generating outputs',
        'Task 18': '18-Footprints and footprint libraries',
        'Task 19': '19-PCB Editor Advanced topics',
        'Task 20': '20-PCB Editor Actions reference',
    }

    main_topics = ['1-Introduction to the KiCad Schematic Editor',
                   '2-Schematic Creation and Editing',
                   '3-Hierarchical schematics',
                   '4-Inspecting a schematic',
                   '5-Assigning Footprints',
                   '6-Forward and back annotation',
                   '7-Schematic Editor Generating Outputs',
                   '8-Symbols and Symbol Libraries',
                   '9-Simulator',
                   '10-Schematic Editor Advanced Topics',
                   '11-Schematic Editor Actions reference',
                   '12-Introduction to the KiCad PCB Editor',
                   '13-Display and selection controls',
                   '14-Creating a PCB',
                   '15-Editing a board',
                   '16-Inspecting a board',
                   '17-PCB Editor Generating outputs',
                   '18-Footprints and footprint libraries',
                   '19-PCB Editor Advanced topics',
                   '20-PCB Editor Actions reference']

    # 10 11 12 16 17 20 dosenot shortened
    main_gpt_messages = [
        # pre_description
        {"role": "system",
         "content": "You are a helpful assistant from Smarton Company, which is designed to help pcb engineers to learn Schematic Editor and PCB Editor for Kicad."},
        {"role": "system",
         "content": "There are {} Tasks from help manual of Schematic Editor and PCB Editor. The Tasks from 1 to 11 is about Schematic Editor and Tasks from 12-20 is about PCB Editor".format(
             number_of_task)},
        # Tasks
        {"role": "system",
         "content": "'Task 1': 'Introduction to the KiCad Schematic Editor'. Task 1 is ideal for users who are new to KiCad or schematic capture software in general. Typical queries might include questions about the functionalities and features of the Schematic Editor, its compatibility across different operating systems, or its integration with other KiCad components. Users looking to understand the layout of the Schematic Editor's interface, how to navigate and control the editing canvas, and use hotkeys would also be best served by this task. Moreover, questions about initial configuration, particularly concerning the setup of the global symbol library table, can be answered by 'Task 1'."},
        {"role": "system",
         "content": "'Task 2': 'Schematic Creation and Editing'. Task 2 is relevant for users wanting to understand the purpose and process of designing schematics with KiCad, such as creating symbols, wires, labels, junctions, and buses. It would also be helpful for those curious about the benefits of a KiCad-designed schematic, like validation, bill of materials generation, netlist creation for simulation, and circuit definition for PCB layout. This task will be suitable for users asking about managing schematics across multiple sheets or wanting to learn about the hierarchical organization of multi-sheet schematics in KiCad. In addition, 'Task 2' could help users who need information on editing object properties, understanding grids and snapping, working with symbols, understanding reference designators and symbol annotation, making electrical connections, defining netclasses, dealing with graphical items, and configuring the schematic setup. It would also be helpful for those inquiring about rescuing cached symbols."},
        {"role": "system",
         "content": "'Task 3': 'Hierarchical schematics'. Task 3 is particularly beneficial for those who are working with multi-sheet schematics and want to know how these are organized in a hierarchical manner with a root sheet and multiple sub-sheets. This task is important if users need to understand how to improve the legibility and efficiency of their schematics by adopting a hierarchical design approach. It provides detailed instructions on how to start a hierarchical schematic from the root sheet, create sub-sheets, draw circuits, and establish electrical connections between sheets. Queries about using hierarchical pins and labels for inter-sheet connections or global labels for connections in the entire hierarchy would also fall under this task. Furthermore, if users are interested in learning how to navigate between sheets, add new sheets to their design, or want to see examples of hierarchical designs, 'Task 3' would be the best choice."},
        {"role": "system",
         "content": "'Task 4': 'Inspecting a schematic'. Task 4 focuses on features related to searching, highlighting, cross-probing, and checking electrical rules in the schematic editor. It includes tools like Find and Find and Replace for text search, net highlighting for visualizing net connections, cross-probing between the schematic and PCB, ERC for detecting errors or warnings, and customization options for ERC settings. The task also covers specific topics like power pins, ERC configuration, and the generation of ERC report files."},
        {"role": "system",
         "content": "'Task 5': 'Assigning Footprints'. Task 5 is focused on the utilization of various methods provided by KiCad for footprint assignment in PCB design. Users will learn how to assign footprints using Symbol Properties, Symbol Fields Table, and while placing symbols. The task also covers the use of the Footprint Assignment Tool, which offers features like filtering and viewing footprints, 3D component model visualization, and automatic footprint association using equivalence files. Users will understand the process of manual and automatic footprint assignment, viewing the current footprint, and opening footprints in the 3D model viewer. It is important to note that prior configuration of the Footprint Library Table is necessary for assigning footprints. If queries involve footprint selection and assignment, the usage of specific tools like the Footprint Assignment Tool, managing the Footprint Library Browser, using equivalence files, or viewing footprints and 3D models, they should be categorized under Task 5."},
        {"role": "system",
         "content": "'Task 6': 'Forward and back annotation'. Task 6 should be selected if a user is discussing a project in KiCad and they mention needing to synchronize design changes between the schematic and the PCB. Specifically, if the user mentions updating the PCB from the schematic (also known as forward annotation), or updating the schematic from the PCB (known as back annotation), this indicates Task 6 is appropriate. This might include user statements such as 'I've made changes in the schematic and need to reflect them in the PCB', or 'I've made updates in the PCB and want them back-annotated into the schematic'."},
        {"role": "system",
         "content": "'Task 7': 'Schematic Editor Generating Outputs'. Task 7 should be selected if a user is talking about wanting to generate different types of outputs in KiCad, like wanting to print or plot their schematic, generate a Bill of Materials (BOM), or create a netlist. User inputs might include phrases like 'How can I print my schematic in KiCad?', 'How to plot a schematic to a file?', 'I want to generate a BOM in KiCad', or 'I need to create a netlist in KiCad."},
        {"role": "system",
         "content": "'Task 8': 'Symbols and Symbol Libraries'. Possible actions to perform with task 8:'Create a new symbol''Edit an existing symbol''Save a symbol to a library''Create a new symbol library''Browse through the symbols in a specific library''Add a new pin to a symbol''Create a new power symbol''Change the body style of a symbol'"},
        {"role": "system",
         "content": "'Task 9': 'Simulator'.Task 9 focuses on the simulation capabilities of KiCad using the integrated ngspice electrical circuit simulator and guides you through setting up and running simulations, interpreting results, and troubleshooting simulation issues. "},
        {"role": "system",
         "content": "'Task 10': 'Schematic Editor Advanced Topics'. Configuration and Customization,Text variables,Database Libraries,Custom Netlist and BOM Formats"},
        {"role": "system",
         "content": "'Task 11': 'Schematic Editor Actions reference'. Actions reference is a list of every available action in the KiCad Schematic Editor: a command that can be assigned to a hotkey. It includes actions are available in the Schematic Editor. Hotkeys can be assigned to any of these actions in the Hotkeys section of the preferences."},
        {"role": "system",
         "content": "'Task 12': 'Introduction to the KiCad PCB Editor'. Task 12 is suitable for new users. It covers initial configuration, including setting up the global footprint library table. The user interface, including toolbars, message panel, and selection filter panel, is explained. Navigating the canvas, hotkeys for actions, and accessing the hotkey list are discussed. Context menu options are highlighted."},
        {"role": "system",
         "content": "'Task 13': 'Display and selection controls'. Task 13 covers display and selection controls in the KiCad PCB Editor. It explains managing board layers, customizing object appearance, controlling selection filters, highlighting nets, and enabling cross-probing. Users learn to navigate the PCB design, select and manipulate objects, visualize specific nets, and establish a seamless connection between schematic and PCB for efficient design review."},
        {"role": "system",
         "content": "'Task 14': 'Creating a PCB'.  Task 14 covers the process of creating a PCB in KiCad. It explains the basic concepts of PCB design, such as footprints, nets, tracks, vias, and zones. KiCad's capabilities, including the number of layers and measurement resolution, are also discussed. The task provides guidance on starting a PCB design from a schematic and the recommended workflow. It explains how to import schematic design information into the PCB editor and emphasizes the use of the 'Update PCB from Schematic' tool. Additionally, it explains how to start a PCB design from scratch and the importance of configuring board settings using the Board Setup dialog."},
        {"role": "system",
         "content": "'Task 15': 'Editing a board'. Task 15 contains following sub tasks, Placement and drawing operations, Snapping, Editing object properties, 4-Working with footprints, 5-Working with pads, 6-Working with zones, 7-Graphical objects, 8-Dimensions, 9-Routing tracks, 10-Forward and back annotation, 11-Locking"},
        {"role": "system",
         "content": "'Task 16': 'Inspecting a board'. Task 16 covers tools for inspecting a board in KiCad. The measurement tool (5.1) enables distance and angle measurements on the PCB. The design rule checker (5.2) verifies compliance with board setup requirements and netlist connectivity. The Find tool (5.3) searches for text in the PCB, including reference designators and footprint fields. The 3D Viewer (5.5) displays a 3D view of the board and components, offering different perspectives, component visibility, cross-probing, and raytraced renders. The Net Inspector (5.6) provides statistics on nets, including pad count, via count, track length, and die length."},
        {"role": "system",
         "content": "'Task 17': 'PCB Editor Generating outputs'. Task 17 focuses on generating manufacturing outputs and interfacing with external software in KiCad. It covers the creation of Gerber files for PCB manufacturing using the Plot dialog, including layer configurations and output options. KiCad can also generate CNC drilling files in Excellon or Gerber X2 format, along with options for output folder, mirroring, and file merging. Component placement files for pick-and-place machines, additional fabrication outputs such as footprint reports and BOMs, printing options, and exporting to third-party formats like Specctra .DSN, IDF, and Hyperlynx are also discussed."},
        {"role": "system",
         "content": "'Task 18': 'Footprints and footprint libraries'. Task 18 contains following sub tasks, Managing symbol libraries, Creating and editing footprints"},
        {"role": "system",
         "content": "'Task 19': 'PCB Editor Advanced topics'. Task 19 covers advanced topics including Configuration and Customization, Text variables, Custom design rules, Scripting, Working With IDF Component Outlines"},
        {"role": "system",
         "content": "'Task 20': 'PCB Editor Actions reference'.Task 20 provides a comprehensive list of actions in the PCB Editor and 3D Viewer, as well as common actions across KiCad. These actions cover various functionalities such as alignment, distribution, layer management, net manipulation, shape creation, diagnostics, footprint management, routing, 3D model control, and basic editing functions. Hotkeys can be assigned for quick access."},
    ]

    items = list(tasks.items())
    tasks = dict(items[:number_of_task+pre_description])
    # main_gpt_messages = main_gpt_messages[:pre_description+number_of_task+1]
    # print(tasks)
    # print(main_gpt_messages)

    return tasks, main_topics, main_gpt_messages