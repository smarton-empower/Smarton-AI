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

import inspect
from .basicop_helpers import *

def plugin_preinput():
    functions_list = [o for o in globals().items() if inspect.isfunction(o[1])]
    plugin_names = []
    plugin_args = []
    plugin_docstrings = []
    for i in range(len(functions_list)-1):
        function_name, function = functions_list[i]
        parameters = inspect.signature(function).parameters
        default_args = []
        for name, parameter in parameters.items():
            if parameter.default != inspect.Parameter.empty:
                default_args.append(name)
        plugin_args.append(default_args)
        plugin_names.append(function_name)
        plugin_docstrings.append(inspect.getdoc(function))

    plugin_description_msg = [
        {"role": "system", "content": f"The following describes the plugins and their corresponding functions. Please select a suitable plugin according to the user's requirements and the description of the plugin functions"}
    ]

    for i in range(len(plugin_names)-1):
        plugin_name = plugin_names[i]
        plugin_arg = plugin_args[i]
        plugin_descriptions = plugin_docstrings[i]
        plugin_description_msg.append({"role": "system", "content": f"{plugin_name}: The id is {i+1}, {plugin_descriptions} and its parameters are {plugin_arg}"})

    return plugin_names, plugin_args, plugin_description_msg

# plugin_names, plugin_with_args, plugin_description_msg = plugin_preinput()
# print(plugin_names)
# print(plugin_with_args)
# print(plugin_description_msg)
