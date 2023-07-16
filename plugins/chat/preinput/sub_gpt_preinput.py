def subtask_preiput():
    # subtask name
    subtasks_name1 = ["1-Description", "2-Initial Configuration", "3-The Schematic Editor User Interface",
                      "4-Navigating the editing canvas", "5-Hotkeys", "6-Mouse operations and selection",
                      "7-Left toolbar display controls"]
    subtasks_name2 = ["1-Introduction", "2-Schematic editing operations", "3-Grids", "4-Snapping",
                      "5-Editing object properties", "6-Working with symbols",
                      "7-Reference Designators and Symbol Annotation", "8-Electrical Connections", "9-Netclasses",
                      "10-Graphical items", "11-Schematic Setup", "12-Rescuing cached symbols"]
    subtasks_name3 = ["1-Introduction", "2-Adding sheets to a design", "3-Navigating between sheets",
                      "4-Electrical connections between sheets", "5-Hierarchical design examples"]
    subtasks_name4 = ["1-Find tool", "2-Net highlighting", "3-Cross-probing from the PCB", "4-Electrical Rules Check"]
    subtasks_name5 = ["1-Assigning Footprints in Symbol Properties", "2-Assigning Footprints While Placing Symbols",
                      "3-Assigning Footprints with the Footprint Assignment Tool"]
    subtasks_name6 = ["1-Update PCB from Schematic (forward annotation)",
                      "2-Update Schematic from PCB (back annotation)"]
    subtasks_name7 = ["1-Printing", "2-Plotting", "3-Generating a Bill of Materials", "4-Generating a Netlist"]
    subtasks_name8 = ["1-Managing symbol libraries", "2-Creating and editing symbols", "3-Browsing symbol libraries"]
    subtasks_name9 = ["1-Value notation", "2-Assigning models", "3-SPICE directives", "4-Running simulations"]
    subtasks_name10 = ["1-Configuration and Customization", "2-Text variables", "Database Libraries",
                       "3-Custom Netlist and BOM Formats"]
    subtasks_name11 = ["1-Schematic Editor", "2-Common"]
    subtasks_name12 = ["1-Initial configuration", "2-The PCB Editor user interface", "3-Navigating the editing canvas",
                       "4-Hotkeys"]
    subtasks_name13 = ["1-Board layers", "2-The appearance panel", "3-Selection and the selection filter",
                       "4-Net highlighting", "5-Cross-probing from the schematic", "6-Left toolbar display controls"]
    subtasks_name14 = ["1-Basic PCB concepts", "2-Capabilities", "3-Starting from a schematic",
                       "4-Starting from scratch", "5-Board setup"]
    subtasks_name15 = ["1-Placement and drawing operations", "2-Snapping", "3-Editing object properties",
                       "4-Working with footprints", "5-Working with pads", "6-Working with zones",
                       "7-Graphical objects", "8-Dimensions", "9-Routing tracks", "10-Forward and back annotation",
                       "11-Locking"]
    subtasks_name16 = ["1-Measurement tool", "2-Design rule checking", "3-Find tool", "4-Search panel", "5-3D Viewer",
                       "6-Net inspector"]
    subtasks_name17 = ["1-Fabrication outputs and plotting", "2-Drill files", "3-Component placement files",
                       "4-Additional fabrication outputs", "5-Printing", "6-Exporting files"]
    subtasks_name18 = ["1-Managing symbol libraries", "2-Creating and editing footprints"]
    subtasks_name19 = ["1-Configuration and Customization", "2-Text variables", "3-Custom design rules", "4-Scripting",
                       "5-Working With IDF Component Outlines"]
    subtasks_name20 = ["1-PCB Editor", "2-3D Viewer", "3-Common"]

    subtasks_name_all = [subtasks_name1, subtasks_name2, subtasks_name3, subtasks_name4, subtasks_name5, subtasks_name6,
                         subtasks_name7, subtasks_name8, subtasks_name9, subtasks_name10, subtasks_name11,
                         subtasks_name12, subtasks_name13, subtasks_name14, subtasks_name15, subtasks_name16,
                         subtasks_name17, subtasks_name18, subtasks_name19, subtasks_name20]

    # subtask preinput
    task_1_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 1 Introduction to the KiCad Schematic Editor, you contain 7 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Description"},
        {"role": "system", "content": "Subtask 2: 2-Initial Configuration"},
        {"role": "system", "content": "Subtask 3: 3-The Schematic Editor User Interface"},
        {"role": "system", "content": "Subtask 4: 4-Navigating the editing canvas"},
        {"role": "system", "content": "Subtask 5: 5-Hotkeys"},
        {"role": "system", "content": "Subtask 6: 6-Mouse operations and selection"},
        {"role": "system", "content": "Subtask 7: 7-Left toolbar display controls"}
    ]

    task_2_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 2 Schematic Creation and Editing, you contain 12 Subtasks."},
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
        {"role": "system", "content": "Subtask 12: 12-Rescuing cached symbols"}

    ]

    task_3_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 3 Hierarchical schematics, you contain 5 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Introduction"},
        {"role": "system", "content": "Subtask 2: 2-Adding sheets to a design"},
        {"role": "system", "content": "Subtask 3: 3-Navigating between sheets"},
        {"role": "system", "content": "Subtask 4: 4-Electrical connections between sheets"},
        {"role": "system", "content": "Subtask 5: 5-Hierarchical design examples"}
    ]

    task_4_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 4 Inspecting a schematic, you contain 4 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Find tool"},
        {"role": "system", "content": "Subtask 2: 2-Net highlighting"},
        {"role": "system", "content": "Subtask 3: 3-Cross-probing from the PCB"},
        {"role": "system", "content": "Subtask 4: 4-Electrical Rules Check"}
    ]

    task_5_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 5 Assigning Footprints, you contain 3 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Assigning Footprints in Symbol Properties"},
        {"role": "system", "content": "Subtask 2: 2-Assigning Footprints While Placing Symbols"},
        {"role": "system", "content": "Subtask 3: 3-Assigning Footprints with the Footprint Assignment Tool"}
    ]
    task_6_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 6 Forward and back annotation, you contain 2 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Update PCB from Schematic (forward annotation)"},
        {"role": "system", "content": "Subtask 2: 2-Update Schematic from PCB (back annotation)"}
    ]

    task_7_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 7 Schematic Editor Generating Outputs, you contain 4 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Printing"},
        {"role": "system", "content": "Subtask 2: 2-Plotting"},
        {"role": "system", "content": "Subtask 3: 3-Generating a Bill of Materials"},
        {"role": "system", "content": "Subtask 4: 4-Generating a Netlist"},
    ]

    task_8_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 8 Symbols and Symbol Libraries, you contain 3 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Managing symbol libraries"},
        {"role": "system", "content": "Subtask 2: 2-Creating and editing symbols"},
        {"role": "system", "content": "Subtask 3: 3-Browsing symbol libraries"}
    ]

    task_9_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 9 Simulator, you contain 4 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Value notation"},
        {"role": "system", "content": "Subtask 2: 2-Assigning models"},
        {"role": "system", "content": "Subtask 3: 3-SPICE directives"},
        {"role": "system", "content": "Subtask 4: 4-Running simulations"}
    ]

    task_10_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 10 Schematic Editor Advanced Topics, you contain 4 Subtasks."},
        {"role": "system", "content": "Subtask 1: 1-Configuration and Customization"},
        {"role": "system", "content": "Subtask 2: 2-Text variables"},
        {"role": "system", "content": "Subtask 3: 3-Database Libraries"},
        {"role": "system", "content": "Subtask 4: 4-Custom Netlist and BOM Formats"}
    ]

    task_11_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 11 Schematic Editor Actions reference, you contain 2 Subtask."},
        {"role": "system", "content": "Subtask 1: 1-Schematic Editor"},
        {"role": "system", "content": "Subtask 2: 2-Common"}
    ]

    task_12_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 12 Introduction to the KiCad PCB Editor, you contain 4 Subtasks."},
        {"role": "system", "content": "Subtask 1: Initial configuration"},
        {"role": "system", "content": "Subtask 2: The PCB Editor user interface"},
        {"role": "system", "content": "Subtask 3: Navigating the editing canvas"},
        {"role": "system", "content": "Subtask 4: Hotkeys"}
    ]

    task_13_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 13 Display and selection controls, you contain 6 Subtasks."},
        {"role": "system", "content": "Subtask 1: Board layers"},
        {"role": "system", "content": "Subtask 2: The appearance panel"},
        {"role": "system", "content": "Subtask 3: Selection and the selection filter"},
        {"role": "system", "content": "Subtask 4: Net highlighting"},
        {"role": "system", "content": "Subtask 5: Cross-probing from the schematic"},
        {"role": "system", "content": "Subtask 6: Left toolbar display controls"}

    ]

    task_14_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 14 Creating a PCB, you contain 5 Subtasks."},
        {"role": "system", "content": "Subtask 1: Basic PCB concepts"},
        {"role": "system", "content": "Subtask 2: Capabilities"},
        {"role": "system", "content": "Subtask 3: Starting from a schematic"},
        {"role": "system", "content": "Subtask 4: Starting from scratch"},
        {"role": "system", "content": "Subtask 5: Board setup"}
    ]

    task_15_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 15 Editing a board, you contain 4 Subtasks."},
        {"role": "system", "content": "Subtask 1: Placement and drawing operations"},
        {"role": "system", "content": "Subtask 2: Snapping"},
        {"role": "system", "content": "Subtask 3: Editing object properties"},
        {"role": "system", "content": "Subtask 4: Working with footprints"},
        {"role": "system", "content": "Subtask 5: Working with pads"},
        {"role": "system", "content": "Subtask 6: Working with zones"},
        {"role": "system", "content": "Subtask 7: Graphical objects"},
        {"role": "system", "content": "Subtask 8: Dimensions"},
        {"role": "system", "content": "Subtask 9: Routing tracks"},
        {"role": "system", "content": "Subtask 10: Forward and back annotation"},
        {"role": "system", "content": "Subtask 11: Locking"}
    ]

    task_16_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 16 Inspecting a board, you contain 6 Subtasks."},
        {"role": "system", "content": "Subtask 1: Measurement tool"},
        {"role": "system", "content": "Subtask 2: Design rule checking"},
        {"role": "system", "content": "Subtask 3: Find tool"},
        {"role": "system", "content": "Subtask 4: Search panel"},
        {"role": "system", "content": "Subtask 5: 3D Viewer"},
        {"role": "system", "content": "Subtask 6: Net inspector"}
    ]

    task_17_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 17 PCB Editor Generating outputs, you contain 6 Subtasks."},
        {"role": "system", "content": "Subtask 1: Fabrication outputs and plotting"},
        {"role": "system", "content": "Subtask 2: Drill files"},
        {"role": "system", "content": "Subtask 3: Component placement files"},
        {"role": "system", "content": "Subtask 4: Additional fabrication outputs"},
        {"role": "system", "content": "Subtask 5: Printing"},
        {"role": "system", "content": "Subtask 6: Exporting files"}
    ]

    task_18_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 18 Footprints and footprint libraries, you contain 2 Subtasks."},
        {"role": "system", "content": "Subtask 1: Managing symbol libraries"},
        {"role": "system", "content": "Subtask 2: Creating and editing footprints"}
    ]

    task_19_subgpt_messages = [
        {"role": "system", "content": "You are subgpt for task 19 PCB Editor Advanced topics, you contain 5 Subtasks."},
        {"role": "system", "content": "Subtask 1: Configuration and Customization"},
        {"role": "system", "content": "Subtask 2: Text variables"},
        {"role": "system", "content": "Subtask 3: Custom design rules"},
        {"role": "system", "content": "Subtask 4: Scripting"},
        {"role": "system", "content": "Subtask 5: Working With IDF Component Outlines"}

    ]

    task_20_subgpt_messages = [
        {"role": "system",
         "content": "You are subgpt for task 20 PCB Editor Actions reference, you contain 3 Subtasks."},
        {"role": "system", "content": "Subtask 1: PCB Editor"},
        {"role": "system", "content": "Subtask 2: 3D Viewer"},
        {"role": "system", "content": "Subtask 3: Common"}
    ]

    task_subgpt_messages_list = [task_1_subgpt_messages, task_2_subgpt_messages, task_3_subgpt_messages,
                                 task_4_subgpt_messages, task_5_subgpt_messages,
                                 task_6_subgpt_messages, task_7_subgpt_messages, task_8_subgpt_messages,
                                 task_9_subgpt_messages, task_10_subgpt_messages,
                                 task_11_subgpt_messages, task_12_subgpt_messages, task_13_subgpt_messages,
                                 task_14_subgpt_messages, task_15_subgpt_messages, task_16_subgpt_messages,
                                 task_17_subgpt_messages, task_18_subgpt_messages, task_19_subgpt_messages,
                                 task_20_subgpt_messages]
    subgpt_message_number_list = [len(task_subgpt_messages_list[i]) for i in range(len(task_subgpt_messages_list))]
    # print(subgpt_message_number_list)

    return subtasks_name_all, task_subgpt_messages_list


# 'Task 1': 'Introduction to the KiCad Schematic Editor'

def task1(path):
    path = path + "01_all.html"
    # print(path)
    return path


def task1_1(path):
    path = path + "01_1.html"
    # print(path)
    return path


def task1_2(path):
    path = path + "01_2.html"
    # print(path)
    return path


def task1_3(path):
    path = path + "01_3.html"
    # print(path)
    return path


def task1_4(path):
    path = path + "01_4.html"
    # print(path)
    return path


def task1_5(path):
    path = path + "01_5.html"
    # print(path)
    return path


def task1_6(path):
    path = path + "01_6.html"
    # print(path)
    return path


def task1_7(path):
    path = path + "01_7.html"
    # print(path)
    return path


# 'Task 2': 'Schematic Creation and Editing'

def task2(path):
    path = path + "02_all.html"
    # print(path)
    return path


def task2_1(path):
    path = path + "02_1.html"
    # print(path)
    return path


def task2_2(path):
    path = path + "02_2.html"
    # print(path)
    return path


def task2_3(path):
    path = path + "02_3.html"
    # print(path)
    return path


def task2_4(path):
    path = path + "02_4.html"
    # print(path)
    return path


def task2_5(path):
    path = path + "02_5.html"
    # print(path)
    return path


def task2_6(path):
    path = path + "02_6.html"
    # print(path)
    return path


def task2_7(path):
    path = path + "02_7.html"
    # print(path)
    return path


def task2_8(path):
    path = path + "02_8.html"
    # print(path)
    return path


def task2_9(path):
    path = path + "02_9.html"
    # print(path)
    return path


def task2_10(path):
    path = path + "02_10.html"
    # print(path)
    return path


def task2_11(path):
    path = path + "02_11.html"
    # print(path)
    return path


def task2_12(path):
    path = path + "02_12.html"
    # print(path)
    return path


# 'Task 3': 'Hierarchical schematics'
def task3(path):
    path = path + "03_all.html"
    # print(path)
    return path


def task3_1(path):
    path = path + "03_1.html"
    # print(path)
    return path


def task3_2(path):
    path = path + "03_2.html"
    # print(path)
    return path


def task3_3(path):
    path = path + "03_3.html"
    # print(path)
    return path


def task3_4(path):
    path = path + "03_4.html"
    # print(path)
    return path


def task3_5(path):
    path = path + "03_5.html"
    # print(path)
    return path


# 'Task 4': 'Inspecting a schematic'
def task4(path):
    path = path + "04_all.html"
    # print(path)
    return path


def task4_1(path):
    path = path + "04_1.html"
    # print(path)
    return path


def task4_2(path):
    path = path + "04_2.html"
    # print(path)
    return path


def task4_3(path):
    path = path + "04_3.html"
    # print(path)
    return path


def task4_4(path):
    path = path + "04_4.html"
    # print(path)
    return path


# 'Task 5': 'Assigning Footprints'

def task5(path):
    path = path + "05_all.html"
    # print(path)
    return path


def task5_1(path):
    path = path + "05_1.html"
    # print(path)
    return path


def task5_2(path):
    path = path + "05_2.html"
    # print(path)
    return path


def task5_3(path):
    path = path + "05_3.html"
    # print(path)
    return path


# 'Task 6': 'Forward and back annotation'

def task6(path):
    path = path + "06_all.html"
    # print(path)
    return path


def task6_1(path):
    path = path + "06_1.html"
    # print(path)
    return path


def task6_2(path):
    path = path + "06_2.html"
    # print(path)
    return path


# 'Task 7': 'Schematic Editor Generating Outputs'

def task7(path):
    path = path + "07_all.html"
    # print(path)
    return path


def task7_1(path):
    path = path + "07_1.html"
    # print(path)
    return path


def task7_2(path):
    path = path + "07_2.html"
    # print(path)
    return path


def task7_3(path):
    path = path + "07_3.html"
    # print(path)
    return path


def task7_4(path):
    path = path + "07_4.html"
    # print(path)
    return path


# 'Task 8': 'Symbols and Symbol Libraries'

def task8(path):
    path = path + "08_all.html"
    # print(path)
    return path


def task8_1(path):
    path = path + "08_1.html"
    # print(path)
    return path


def task8_2(path):
    path = path + "08_2.html"
    # print(path)
    return path


def task8_3(path):
    path = path + "08_3.html"
    # print(path)
    return path


# 'Task 9': 'Simulator'

def task9(path):
    path = path + "09_all.html"
    # print(path)
    return path


def task9_1(path):
    path = path + "09_1.html"
    # print(path)
    return path


def task9_2(path):
    path = path + "09_2.html"
    # print(path)
    return path


def task9_3(path):
    path = path + "09_3.html"
    # print(path)
    return path


def task9_4(path):
    path = path + "09_4.html"
    # print(path)
    return path


# 'Task 10': 'Schematic Editor Advanced Topics'

def task10(path):
    path = path + "10_all.html"
    # print(path)
    return path


def task10_1(path):
    path = path + "10_1.html"
    # print(path)
    return path


def task10_2(path):
    path = path + "10_2.html"
    # print(path)
    return path


def task10_3(path):
    path = path + "10_3.html"
    # print(path)
    return path


def task10_4(path):
    path = path + "10_4.html"
    # print(path)
    return path


# 'Task 11': 'Schematic Editor Actions reference'

def task11(path):
    path = path + "11_all.html"
    # print(path)
    return path


def task11_1(path):
    path = path + "11_1.html"
    # print(path)
    return path


def task11_2(path):
    path = path + "11_2.html"
    # print(path)
    return path


# 'Task 12': '12-Introduction to the KiCad PCB Editor'
def task12(path):
    path = path + "01_all.html"
    # print(path)
    return path


def task12_1(path):
    path = path + "01_1.html"
    # print(path)
    return path


def task12_2(path):
    path = path + "01_2.html"
    # print(path)
    return path


def task12_3(path):
    path = path + "01_3.html"
    # print(path)
    return path


def task12_4(path):
    path = path + "01_4.html"
    # print(path)
    return path


# 'Task 13': '13-Display and selection controls'
def task13(path):
    path = path + "02_all.html"
    # print(path)
    return path


def task13_1(path):
    path = path + "02_1.html"
    # print(path)
    return path


def task13_2(path):
    path = path + "02_2.html"
    # print(path)
    return path


def task13_3(path):
    path = path + "02_3.html"
    # print(path)
    return path


def task13_4(path):
    path = path + "02_4.html"
    # print(path)
    return path


def task13_5(path):
    path = path + "02_5.html"
    # print(path)
    return path


def task13_6(path):
    path = path + "02_6.html"
    # print(path)
    return path


# 'Task 14': '14-Creating a PCB'
def task14(path):
    path = path + "03_all.html"
    # print(path)
    return path


def task14_1(path):
    path = path + "03_1.html"
    # print(path)
    return path


def task14_2(path):
    path = path + "03_2.html"
    # print(path)
    return path


def task14_3(path):
    path = path + "03_3.html"
    # print(path)
    return path


def task14_4(path):
    path = path + "03_4.html"
    # print(path)
    return path


def task14_5(path):
    path = path + "03_5.html"
    # print(path)
    return path


# 'Task 15': '15-Editing a board'

def task15(path):
    path = path + "04_all.html"
    # print(path)
    return path


def task15_1(path):
    path = path + "04_1.html"
    # print(path)
    return path


def task15_2(path):
    path = path + "04_2.html"
    # print(path)
    return path


def task15_3(path):
    path = path + "04_3.html"
    # print(path)
    return path


def task15_4(path):
    path = path + "04_4.html"
    # print(path)
    return path


def task15_5(path):
    path = path + "04_5.html"
    # print(path)
    return path


def task15_6(path):
    path = path + "04_6.html"
    # print(path)
    return path


def task15_7(path):
    path = path + "04_7.html"
    # print(path)
    return path


def task15_8(path):
    path = path + "04_8.html"
    # print(path)
    return path


def task15_9(path):
    path = path + "04_9.html"
    # print(path)
    return path


def task15_10(path):
    path = path + "04_10.html"
    # print(path)
    return path


def task15_11(path):
    path = path + "04_11.html"
    # print(path)
    return path


# 'Task 16': '16-Inspecting a board'

def task16(path):
    path = path + "05_all.html"
    # print(path)
    return path


def task16_1(path):
    path = path + "05_1.html"
    # print(path)
    return path


def task16_2(path):
    path = path + "05_2.html"
    # print(path)
    return path


def task16_3(path):
    path = path + "05_3.html"
    # print(path)
    return path


def task16_4(path):
    path = path + "05_4.html"
    # print(path)
    return path


def task16_5(path):
    path = path + "05_5.html"
    # print(path)
    return path


def task16_6(path):
    path = path + "05_6.html"
    # print(path)
    return path


# 'Task 17': '17-PCB Editor Generating outputs'

def task17(path):
    path = path + "06_all.html"
    # print(path)
    return path


def task17_1(path):
    path = path + "06_1.html"
    # print(path)
    return path


def task17_2(path):
    path = path + "06_2.html"
    # print(path)
    return path


def task17_3(path):
    path = path + "06_3.html"
    # print(path)
    return path


def task17_4(path):
    path = path + "06_4.html"
    # print(path)
    return path


def task17_5(path):
    path = path + "06_5.html"
    # print(path)
    return path


def task17_6(path):
    path = path + "06_6.html"
    # print(path)
    return path


# 'Task 18': '18-Footprints and footprint libraries'

def task18(path):
    path = path + "07_all.html"
    # print(path)
    return path


def task18_1(path):
    path = path + "07_1.html"
    # print(path)
    return path


def task18_2(path):
    path = path + "07_2.html"
    # print(path)
    return path


# 'Task 19': '19-PCB Editor Advanced topics'

def task19(path):
    path = path + "08_all.html"
    # print(path)
    return path


def task19_1(path):
    path = path + "08_1.html"
    # print(path)
    return path


def task19_2(path):
    path = path + "08_2.html"
    # print(path)
    return path


def task19_3(path):
    path = path + "08_3.html"
    # print(path)
    return path


def task19_4(path):
    path = path + "08_4.html"
    # print(path)
    return path


def task19_5(path):
    path = path + "08_5.html"
    # print(path)
    return path


# 'Task 20': '20-PCB Editor Actions reference'

def task20(path):
    path = path + "09_all.html"
    # print(path)
    return path


def task20_1(path):
    path = path + "09_1.html"
    # print(path)
    return path


def task20_2(path):
    path = path + "09_2.html"
    # print(path)
    return path


def task20_3(path):
    path = path + "09_3.html"
    # print(path)
    return path


def subtask_html_path(path_active_eeschema, path_active_pcbnew):
    # eeschema subtask
    Task1_plugins = [task1_1(path_active_eeschema), task1_2(path_active_eeschema), task1_3(path_active_eeschema),
                     task1_4(path_active_eeschema), task1_5(path_active_eeschema), task1_6(path_active_eeschema),
                     task1_7(path_active_eeschema)]
    Task2_plugins = [task2_1(path_active_eeschema), task2_2(path_active_eeschema), task2_3(path_active_eeschema),
                     task2_4(path_active_eeschema), task2_5(path_active_eeschema), task2_6(path_active_eeschema),
                     task2_7(path_active_eeschema), task2_8(path_active_eeschema), task2_9(path_active_eeschema),
                     task2_10(path_active_eeschema), task2_11(path_active_eeschema), task2_12(path_active_eeschema)]
    Task3_plugins = [task3_1(path_active_eeschema), task3_2(path_active_eeschema), task3_3(path_active_eeschema),
                     task3_4(path_active_eeschema), task3_5(path_active_eeschema)]
    Task4_plugins = [task4_1(path_active_eeschema), task4_2(path_active_eeschema), task4_3(path_active_eeschema),
                     task4_4(path_active_eeschema)]
    Task5_plugins = [task5_1(path_active_eeschema), task5_2(path_active_eeschema), task5_3(path_active_eeschema)]
    Task6_plugins = [task6_1(path_active_eeschema), task6_2(path_active_eeschema)]
    Task7_plugins = [task7_1(path_active_eeschema), task7_2(path_active_eeschema), task7_3(path_active_eeschema),
                     task7_4(path_active_eeschema)]
    Task8_plugins = [task8_1(path_active_eeschema), task8_2(path_active_eeschema), task8_3(path_active_eeschema)]
    Task9_plugins = [task9_1(path_active_eeschema), task9_2(path_active_eeschema), task9_3(path_active_eeschema),
                     task9_4(path_active_eeschema)]
    Task10_plugins = [task10_1(path_active_eeschema), task10_2(path_active_eeschema), task10_3(path_active_eeschema),
                      task10_4(path_active_eeschema)]
    Task11_plugins = [task11_1(path_active_eeschema), task11_2(path_active_eeschema)]

    # pcb subtask
    Task12_plugins = [task12_1(path_active_pcbnew), task12_2(path_active_pcbnew), task12_3(path_active_pcbnew),
                      task12_4(path_active_pcbnew)]
    Task13_plugins = [task13_1(path_active_pcbnew), task13_2(path_active_pcbnew), task13_3(path_active_pcbnew),
                      task13_4(path_active_pcbnew), task13_5(path_active_pcbnew), task13_6(path_active_pcbnew)]
    Task14_plugins = [task14_1(path_active_pcbnew), task14_2(path_active_pcbnew), task14_3(path_active_pcbnew),
                      task14_4(path_active_pcbnew), task14_5(path_active_pcbnew)]
    Task15_plugins = [task15_1(path_active_pcbnew), task15_2(path_active_pcbnew), task15_3(path_active_pcbnew),
                      task15_4(path_active_pcbnew), task15_5(path_active_pcbnew), task15_6(path_active_pcbnew),
                      task15_7(path_active_pcbnew), task15_8(path_active_pcbnew), task15_9(path_active_pcbnew),
                      task15_10(path_active_pcbnew), task15_11(path_active_pcbnew)]
    Task16_plugins = [task16_1(path_active_pcbnew), task16_2(path_active_pcbnew), task16_3(path_active_pcbnew),
                      task16_4(path_active_pcbnew), task16_5(path_active_pcbnew), task16_6(path_active_pcbnew)]
    Task17_plugins = [task17_1(path_active_pcbnew), task17_2(path_active_pcbnew), task17_3(path_active_pcbnew),
                      task17_4(path_active_pcbnew), task17_5(path_active_pcbnew), task17_6(path_active_pcbnew)]
    Task18_plugins = [task18_1(path_active_pcbnew), task18_2(path_active_pcbnew)]
    Task19_plugins = [task19_1(path_active_pcbnew), task19_2(path_active_pcbnew), task19_3(path_active_pcbnew),
                      task19_4(path_active_pcbnew), task19_5(path_active_pcbnew)]
    Task20_plugins = [task20_1(path_active_pcbnew), task20_2(path_active_pcbnew), task20_3(path_active_pcbnew)]

    Task_plugins = [Task1_plugins, Task2_plugins, Task3_plugins, Task4_plugins, Task5_plugins,
                    Task6_plugins, Task7_plugins, Task8_plugins, Task9_plugins, Task10_plugins,
                    Task11_plugins, Task12_plugins, Task13_plugins, Task14_plugins, Task15_plugins,
                    Task16_plugins, Task17_plugins, Task18_plugins, Task19_plugins, Task20_plugins]

    return Task_plugins