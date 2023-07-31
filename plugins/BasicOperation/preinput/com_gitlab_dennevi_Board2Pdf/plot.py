
import os
import shutil
import pcbnew
import wx
import re
import traceback

from .pypdf import PdfReader, PdfWriter, generic, _utils

try:
    import fitz  # This imports PyMuPDF
except:
    pass

def print_exception():
    etype, value, tb = exc_info()
    info, error = format_exception(etype, value, tb)[-2:]
    print(f'Exception in:\n{info}\n{error}')

def hex_to_rgb(value):
    """Return (red, green, blue) in float between 0-1 for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    rgb = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    rgb = (rgb[0]/255, rgb[1]/255, rgb[2]/255)
    return rgb

def colorize_pdf_fitz(folder, inputFile, outputFile, color):
    try:
        with fitz.open(os.path.join(folder, inputFile)) as doc:
            xref_number = doc[0].get_contents()
            stream_bytes =doc.xref_stream(xref_number[0])
            new_color = str(color[0]) + ' ' + str(color[1]) + ' ' + str(color[2]) + ' '  
            new_color_RG = bytes(new_color + 'RG', 'ascii')
            new_color_rg = bytes(new_color + 'rg', 'ascii')

            stream_bytes = re.sub(b'0.0.0.RG', new_color_RG, stream_bytes)
            stream_bytes = re.sub(b'0.0.0.rg', new_color_rg, stream_bytes)
            
            doc.update_stream(xref_number[0], stream_bytes)
            doc.save(os.path.join(folder, outputFile), clean=True)

    except RuntimeError as e:
        if "invalid key in dict" in str(e):
            wx.MessageBox("colorize_pdf_fitz failed\nOn input file " + inputFile + " in " + folder + "\n\nThis error can be due to PyMuPdf not being able to handle pdfs created by KiCad 7.0.1 due to a bug in KiCad 7.0.1. Upgrade KiCad or switch to pypdf instead.\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
        return False

    except:
        wx.MessageBox("colorize_pdf_fitz failed\nOn input file " + inputFile + " in " + folder + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
        return False

    return True

def colorize_pdf_pypdf(folder, inputFile, outputFile, color):
    try:
        with open(os.path.join(folder, inputFile), "rb") as f:
            import sys
            class error_handler(object):
                def write(self, data):
                    if not "UserWarning" in data:
                        wx.MessageBox("colorize_pdf_pypdf failed\nOn input file " + inputFile + " in " + folder + "\n\n" + data, 'Error', wx.OK | wx.ICON_ERROR)
                        return False

            if (sys.stderr == None):
                handler = error_handler()
                sys.stderr = handler

            source = PdfReader(f, "rb")
            output = PdfWriter()

            page = source.pages[0]
            content_object = page["/Contents"].get_object()
            content = generic.ContentStream(content_object, source)

            i = 0
            for operands, operator in content.operations:
                if operator == _utils.b_("rg") or operator == _utils.b_("RG"):
                    if operands == [0, 0, 0]:
                        rgb = content.operations[i][0]
                        content.operations[i] = (
                            [generic.FloatObject(color[0]), generic.FloatObject(color[1]),
                             generic.FloatObject(color[2])], content.operations[i][1])
                    #else:
                    #    print(operator, operands[0], operands[1], operands[2], "The type is : ", type(rgb[0]),
                    #          type(rgb[1]), type(rgb[2]))
                i = i + 1

            page.__setitem__(generic.NameObject('/Contents'), content)
            output.add_page(page)

            with open(os.path.join(folder, outputFile), "wb") as outputStream:
                output.write(outputStream)

    except:
        wx.MessageBox("colorize_pdf_pypdf failed\nOn input file " + inputFile + " in " + folder + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
        return False

    return True

def merge_pdf_fitz(input_folder, input_files, output_folder, output_file):
    try:
        output = fitz.open()
        i = 0
        for filename in reversed(input_files):
            try:
                # using "with" to force RAII and avoid another "for" closing files
                with fitz.open(os.path.join(input_folder, filename)) as file:

                    if i == 0:
                        output.insert_pdf(file)
                    else:
                        output[0].show_pdf_page(file[0].rect,  # select output rect
                                                file,  # input document
                                                0,  # input page number
                                                overlay=False)
                i = i + 1
            except:
                wx.MessageBox("merge_pdf failed\n\nOn input file " + filename + " in " + input_folder + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
                return False

        output.save(os.path.join(output_folder, output_file))

    except:
        wx.MessageBox("merge_pdf failed\n\nOn output file " + output_file + " in " + output_folder + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
        return False

    return True

def merge_pdf_pypdf(input_folder, input_files, output_folder, output_file):
    try:
        open_files = []
        #merged_page = _page.PageObject()
        for filename in input_files:
            try:
                file = open(os.path.join(input_folder, filename), 'rb')
                open_files.append(file)
                pdfReader = PdfReader(file, "rb")
                pageObj = pdfReader.pages[0]
                if 'merged_page' in locals():
                    merged_page.merge_page(pageObj)
                else:
                    merged_page = pageObj
            except:
                error_bitmap = ""
                error_msg = traceback.format_exc()
                if 'KeyError: 0' in error_msg:
                    error_bitmap = "This error can be caused by the presence of a bitmap image on this layer. Bitmaps are only allowed on the layer furthest down in the layer list. See Issue #11 for more information.\n\n"
                wx.MessageBox("merge_pdf failed\n\nOn input file " + filename + " in " + input_folder + "\n\n" + error_bitmap + error_msg, 'Error', wx.OK | wx.ICON_ERROR)
                return False

        output = PdfWriter()
        output.add_page(merged_page)
        with open(os.path.join(output_folder, output_file), "wb") as outputStream:
            output.write(outputStream)

    except:
        wx.MessageBox("merge_pdf failed\n\nOn output file " + output_file + " in " + output_folder + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
        return False

    # Close the input files. I don't know why, but merged_page.merge_page(pageObj) doesn't work if I close the files in the merge-loop.
    for f in open_files:
        f.close()

    return True

def create_pdf_from_pages(input_folder, input_files, output_folder, output_file):
    try:
        output = PdfWriter()
        for filename in input_files:
            try:
                with open(os.path.join(input_folder, filename), "rb") as file:
                    #file = open(os.path.join(input_folder, filename), 'rb')
                    pdfReader = PdfReader(file, "rb")
                    pageObj = pdfReader.pages[0]
                    output.add_page(pageObj)
                    #pdfReader.stream.close()
            except:
                wx.MessageBox("create_pdf_from_pages failed\n\nOn input file " + filename + " in " + input_folder + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
                return False

        for page in output.pages:
            # This has to be done on the writer, not the reader!
            page.compress_content_streams()  # This is CPU intensive!

        with open(os.path.join(output_folder, output_file), "wb") as outputStream:
            output.write(outputStream)

    except:
        wx.MessageBox("create_pdf_from_pages failed\n\nOn output file " + output_file + " in " + output_folder + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
        return False

    return True

def plot_gerbers(board, output_path, templates, enabled_templates, del_temp_files, create_svg, del_single_page_files, dialog_panel):
    def setProgress(value):
        dialog_panel.m_progress.SetValue(value)
        dialog_panel.Refresh()
        dialog_panel.Update()

    if dialog_panel.m_radio_fitz.GetValue() or dialog_panel.m_radio_merge_fitz.GetValue() or create_svg:
        try:
            fitz.open()
        except:
            wx.MessageBox("PyMuPdf (fitz) wasn't loaded.\n\nIt must be installed for it to be used for coloring, for merging and for creating SVGs.\n\nMore information under Install dependencies in the Wiki at board2pdf.dennevi.com", 'Error', wx.OK | wx.ICON_ERROR)
            progress = 100
            setProgress(progress)
            dialog_panel.m_staticText_status.SetLabel("Status: Failed to load PyMuPDF.")
            return False

    os.chdir(os.path.dirname(board.GetFileName()))
    output_dir = os.path.abspath(os.path.expanduser(os.path.expandvars(output_path)))

    temp_dir = os.path.abspath(os.path.join(output_dir, "temp"))

    dialog_panel.m_staticText_status.SetLabel("Status: Started plotting...")
    progress = 5
    setProgress(progress)

    steps = 1
    # Count number of process steps
    for t in enabled_templates:
        steps = steps + 1
        if "enabled_layers" in templates[t]:
            enabled_layers = templates[t]["enabled_layers"].split(',')
            enabled_layers[:] = [l for l in enabled_layers if l != '']  # removes empty entries
            if enabled_layers:
                for el in enabled_layers:
                    steps = steps + 1
                    if "layers" in templates[t]:
                        if el in templates[t]["layers"]:
                            if templates[t]["layers"][el] != "#000000":
                                steps = steps + 1
    progress_step = 95//steps

    plot_controller = pcbnew.PLOT_CONTROLLER(board)
    plot_options = plot_controller.GetPlotOptions()

    base_filename = os.path.basename(os.path.splitext(board.GetFileName())[0])
    final_assembly_file = base_filename + "__Assembly.pdf"
    final_assembly_file_with_path = os.path.abspath(os.path.join(output_dir, final_assembly_file))

    # Create the directory if it doesn't exist already
    os.makedirs(output_dir, exist_ok=True)

    # Check if we're able to write to the output file.
    try:
        #os.access(os.path.join(output_dir, final_assembly_file), os.W_OK)
        open(os.path.join(output_dir, final_assembly_file), "w")
    except:
        wx.MessageBox("The output file is not writeable. Perhaps it's open in another " +
                      "application?\n\n" + final_assembly_file_with_path, 'Error', wx.OK | wx.ICON_ERROR)
        dialog_panel.m_staticText_status.SetLabel("Status: Failed to write to output file.")
        return False

    plot_options.SetOutputDirectory(temp_dir)

    templates_list = []
    for t in enabled_templates:
        temp = []
        #{  "Test-template": {"mirrored": true, "enabled_layers": "B.Fab,B.Mask,Edge.Cuts,F.Adhesive", "frame": "In4.Cu",
        #          "layers": {"B.Fab": "#000012", "B.Mask": "#000045"}}  }
        if t in templates:
            temp.append(t) # Add the template name

            if "mirrored" in templates[t]:
                temp.append(templates[t]["mirrored"]) # Add if the template is mirrored or not
            else:
                temp.append(False)
                
            if "tented" in templates[t]:
                temp.append(templates[t]["tented"]) # Add if the template is tented or not
            else:
                temp.append(False)

            frame_layer = "None"
            if "frame" in templates[t]:
                frame_layer = templates[t]["frame"] # Layer with frame

            # Build a dict to translate layer names to layerID
            layer_names = {}
            i = pcbnew.PCBNEW_LAYER_ID_START
            while i < pcbnew.PCBNEW_LAYER_ID_START + pcbnew.PCB_LAYER_ID_COUNT:
                layer_names[board.GetStandardLayerName(i)] = i
                i += 1

            settings = []

            if "enabled_layers" in templates[t]:
                enabled_layers = templates[t]["enabled_layers"].split(',')
                enabled_layers[:] = [l for l in enabled_layers if l != '']  # removes empty entries
                if enabled_layers:
                    for el in enabled_layers:
                        s = []
                        s.append(el) # Layer name string
                        s.append(layer_names[el]) # Layer ID
                        if el in templates[t]["layers"]:
                            s.append(templates[t]["layers"][el]) # Layer color
                        else:
                            s.append("#000000") # Layer color black
                        if el == frame_layer:
                            s.append(True)
                        else:
                            s.append(False)

                        if "layers_negative" in templates[t]:
                            if el in templates[t]["layers_negative"]: # Bool specifying if layer is negative
                                if templates[t]["layers_negative"][el] == "true":
                                    s.append(True)
                                else:
                                    s.append(False)
                            else:
                                s.append(False)
                        else:
                            s.append(False)

                        if "layers_footprint_values" in templates[t]:
                            if el in templates[t]["layers_footprint_values"]: # Bool specifying if footprint values shall be plotted
                                if templates[t]["layers_footprint_values"][el] == "false":
                                    s.append(False)
                                else:
                                    s.append(True)
                            else:
                                s.append(True)
                        else:
                            s.append(True)

                        if "layers_reference_designators" in templates[t]:
                            if el in templates[t]["layers_reference_designators"]: # Bool specifying if reference designators shall be plotted
                                if templates[t]["layers_reference_designators"][el] == "false":
                                    s.append(False)
                                else:
                                    s.append(True)
                            else:
                                s.append(True)
                        else:
                            s.append(True)

                        settings.insert(0, s) # Prepend to settings

            temp.append(settings)
            templates_list.append(temp)
    #wx.MessageBox("Newly created template_list:\n" + str(templates_list))


    """
    [
        ["Greyscale Top", False,
            [
             ("F_Cu", pcbnew.F_Cu, "#F0F0F0", False, True, True, True),
             ("F_Paste", pcbnew.F_Paste, "#C4C4C4", False, False, True, True),
            ]
        ],
    ]
    """
    try:
        # Set General Options:
        plot_options.SetPlotInvisibleText(False)
        # plot_options.SetPlotPadsOnSilkLayer(False);
        plot_options.SetUseAuxOrigin(False)
        plot_options.SetScale(1.0)
        plot_options.SetAutoScale(False)
        # plot_options.SetPlotMode(PLOT_MODE)
        # plot_options.SetLineWidth(2000)
        if (pcbnew.Version()[0:3] == "6.0"):
            # This method is only available on V6, not V6.99/V7
            plot_options.SetExcludeEdgeLayer(True);
    except:
        wx.MessageBox(traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
        dialog_panel.m_staticText_status.SetLabel("Status: Failed to set plot_options")
        return False

    template_filelist = []

    # Iterate over the templates
    for template in templates_list:
        template_name = template[0]
        # wx.MessageBox("Now starting with template: " + template_name)
        # Plot layers to pdf files
        for layer_info in template[3]:
            dialog_panel.m_staticText_status.SetLabel("Status: Plotting " + layer_info[0] + " for template " + template_name)
            progress = progress + progress_step
            setProgress(progress)

            if (pcbnew.Version()[0:3] == "6.0"):
                if pcbnew.IsCopperLayer(layer_info[1]): # Should probably do this on mask layers as well
                    plot_options.SetDrillMarksType(2)  # NO_DRILL_SHAPE = 0, SMALL_DRILL_SHAPE = 1, FULL_DRILL_SHAPE  = 2
                else:
                    plot_options.SetDrillMarksType(0)  # NO_DRILL_SHAPE = 0, SMALL_DRILL_SHAPE = 1, FULL_DRILL_SHAPE  = 2
            else: # API changed in V6.99/V7
                try:
                    if pcbnew.IsCopperLayer(layer_info[1]):  # Should probably do this on mask layers as well
                        plot_options.SetDrillMarksType(pcbnew.DRILL_MARKS_FULL_DRILL_SHAPE)
                    else:
                        plot_options.SetDrillMarksType(pcbnew.DRILL_MARKS_NO_DRILL_SHAPE)
                except:
                    wx.MessageBox("Unable to set Drill Marks type.\n\nIf you're using a V6.99 build from before Dec 07 2022 then update to a newer build.\n\n"+traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
                    dialog_panel.m_staticText_status.SetLabel("Status: Failed to set Drill Marks type")
                    return False

            try:
                plot_options.SetPlotFrameRef(layer_info[3])
                plot_options.SetNegative(layer_info[4])
                plot_options.SetPlotValue(layer_info[5])
                plot_options.SetPlotReference(layer_info[6])
                plot_options.SetMirror(template[1])
                plot_options.SetPlotViaOnMaskLayer(template[2])
                plot_controller.SetLayer(layer_info[1])
                plot_controller.OpenPlotfile(layer_info[0], pcbnew.PLOT_FORMAT_PDF, template_name)
                plot_controller.PlotLayer()
            except:
                wx.MessageBox(traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
                dialog_panel.m_staticText_status.SetLabel("Status: Failed to set plot_options or plot_controller")
                return False

        plot_controller.ClosePlot()

        filelist = []
        # Change color of pdf files
        for layer_info in template[3]:
            ln = layer_info[0].replace('.', '_')
            inputFile = base_filename + "-" + ln + ".pdf"
            if(layer_info[2] != "#000000"):
                dialog_panel.m_staticText_status.SetLabel("Status: Coloring " + layer_info[0] + " for template " + template_name)
                progress = progress + progress_step
                setProgress(progress)

                outputFile = base_filename + "-" + ln + "-colored.pdf"

                if(dialog_panel.m_radio_fitz.GetValue()):
                    if not colorize_pdf_fitz(temp_dir, inputFile, outputFile, hex_to_rgb(layer_info[2])):
                        dialog_panel.m_staticText_status.SetLabel("Status: Failed when coloring " + layer_info[0] + " for template " + template_name + " using PyMuPdf")
                        return False
                else:
                    if not colorize_pdf_pypdf(temp_dir, inputFile, outputFile, hex_to_rgb(layer_info[2])):
                        dialog_panel.m_staticText_status.SetLabel("Status: Failed when coloring " + layer_info[0] + " for template " + template_name + " using pypdf")
                        return False

                filelist.append(outputFile)
            else:
                filelist.append(inputFile)

        # Merge pdf files
        dialog_panel.m_staticText_status.SetLabel("Status: Merging all layers of template " + template_name)
        progress = progress + progress_step
        setProgress(progress)

        assembly_file = base_filename + "_" + template[0] + ".pdf"

        if (dialog_panel.m_radio_merge_fitz.GetValue()):
            if not merge_pdf_fitz(temp_dir, filelist, output_dir, assembly_file):
                dialog_panel.m_staticText_status.SetLabel("Status: Failed when merging all layers of template " + template_name + " using PyMuPdf")
                return False
        else:
            if not merge_pdf_pypdf(temp_dir, filelist, output_dir, assembly_file):
                dialog_panel.m_staticText_status.SetLabel("Status: Failed when merging all layers of template " + template_name + " using pypdf")
                return False

        template_filelist.append(assembly_file)

    # Add all generated pdfs to one file
    dialog_panel.m_staticText_status.SetLabel("Status: Adding all templates to a single file")
    setProgress(progress)

    if not create_pdf_from_pages(output_dir, template_filelist, output_dir, final_assembly_file):
        dialog_panel.m_staticText_status.SetLabel("Status: Failed when adding all templates to a single file")
        return False

    # Create SVG(s) if settings says so
    if create_svg:
        for template_file in template_filelist:
            template_pdf = fitz.open(os.path.join(output_dir, template_file))
            try:
                svg_image = template_pdf[0].get_svg_image()
                svg_filename = os.path.splitext(template_file)[0]+".svg"
                file=open(os.path.join(output_dir, svg_filename), "w")
                file.write(svg_image)
                file.close()
            except:
                wx.MessageBox("Failed to create SVG in " + output_dir + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
                dialog_panel.m_staticText_status.SetLabel("Status: Failed to create SVG(s)")
                return False
            template_pdf.close()

    # Delete temp files if setting says so
    if (del_temp_files):
        try:
            shutil.rmtree(temp_dir)
        except:
            wx.MessageBox("del_temp_files failed\n\nOn dir " + temp_dir + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
            dialog_panel.m_staticText_status.SetLabel("Status: Failed to delete temp files")
            return False

    # Delete single page files if setting says so
    if (del_single_page_files):
        for template_file in template_filelist:
            delete_file = os.path.join(output_dir, os.path.splitext(template_file)[0] + ".pdf")
            try:
                os.remove(delete_file)
            except:
                wx.MessageBox("del_single_page_files failed\n\nOn file " + delete_file + "\n\n" + traceback.format_exc(), 'Error', wx.OK | wx.ICON_ERROR)
                dialog_panel.m_staticText_status.SetLabel("Status: Failed to delete single files")
                return False

    dialog_panel.m_staticText_status.SetLabel("Status: All done!")

    progress = 100
    setProgress(progress)

    endmsg = "All done!\n\nAssembly pdf created: " + os.path.abspath(os.path.join(output_dir, final_assembly_file))
    if (not del_single_page_files):
        endmsg = endmsg + "\n\nSingle page pdf files created:"
        for template_file in template_filelist:
            endmsg = endmsg + "\n" + os.path.abspath(os.path.join(output_dir, os.path.splitext(template_file)[0]+".pdf"))

    if (create_svg):
        endmsg = endmsg + "\n\nSVG files created:"
        for template_file in template_filelist:
            endmsg = endmsg + "\n" + os.path.abspath(os.path.join(output_dir, os.path.splitext(template_file)[0]+".svg"))

    wx.MessageBox(endmsg, 'All done!', wx.OK)
