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

import pcbnew


def rotate_fp_by_fp_name(board, footprint_name=None, rotate_angle=45):
    """
    Its function is to rotate one footprint by name
    """
    footprints = board.GetFootprints()
    for fp in footprints:
        if fp.GetReference() == footprint_name:
            fp.SetOrientationDegrees(fp.GetOrientationDegrees() + rotate_angle)


def rotate_fp_by_mouse(board, rotate_angle=10):
    """
    Its function is to rotate multiple footprints (mutiple) which are selected by mouse clicking
    """
    footprints = board.GetFootprints()
    fps = [x for x in footprints if x.IsSelected()]
    for fp in fps:
        fp.SetOrientationDegrees(fp.GetOrientationDegrees() + rotate_angle)


def move_fp_by_fp_name(board, footprint_name=None, X_offset=0, Y_offset=0):
    """
    Its function is to move one footprint by name
    """
    footprints = board.GetFootprints()
    for fp in footprints:
        if fp.GetReference() == footprint_name:
            new_pos = [fp.GetX() + X_offset, fp.GetY() + Y_offset]
            fp.SetPosition(pcbnew.VECTOR2I(*new_pos))


def move_fp_by_mouse(board, X_offset=0, Y_offset=0):
    """
    Its function is to move multiple footprints which are selected by mouse clicking
    """
    footprints = board.GetFootprints()
    fps = [x for x in footprints if x.IsSelected()]
    for fp in fps:
        new_pos = [fp.GetX() + X_offset, fp.GetY() + Y_offset]
        fp.SetPosition(pcbnew.VECTOR2I(*new_pos))


def flip_fp_by_fp_name(board, footprint_name=None):
    """
    Its function is to flip one footprint by name
    """
    footprints = board.GetFootprints()
    for fp in footprints:
        if fp.GetReference() == footprint_name:
            fp.Flip(fp.GetPosition(), True)


def flip_fp_by_mouse(board):
    """
    Its function is to flip multiple footprints which are selected by mouse clicking
    """
    footprints = board.GetFootprints()
    fps = [x for x in footprints if x.IsSelected()]
    for fp in fps:
        fp.Flip(fp.GetPosition(), True)
