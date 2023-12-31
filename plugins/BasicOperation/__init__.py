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

try:
    from .action import BasicOperations
    # from .com_gitlab_dennevi_Board2Pdf.board2pdf_action import board2pdf
    # from .com_github_MitjaNemec_PlaceFootprints.action_place_footprints import PlaceFootprints
    # from .com_github_MitjaNemec_ReplicateLayout.action_replicate_layout import ReplicateLayout
    # from .com_github_MitjaNemec_SaveRestoreLayout.action_save_restore_layout import SaveRestoreLayout

    BasicOperations().register()
    # board2pdf().register()
    # PlaceFootprints().register()
    # ReplicateLayout().register()
    # SaveRestoreLayout().register()

except Exception as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))