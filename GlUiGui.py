# GlUiB Gui module for Blender
# Copyright (C) 2018 Legigan Jeremy AKA Pistiwique
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# <pep8 compliant>


class GlLayout:
    def __init__(self):
        self._left_margin = 0
        self._top_margin = 0
        self._right_margin = 0
        self._bottom_margin = 0

    @property
    def margins(self):
        """
        Property that hold the margins of the layout
        :return: (left, top, right, bottom)
        """
        return (self._left_margin,
                self._top_margin,
                self._right_margin,
                self._bottom_margin
                )

    def set_margin(self, *args):
        if len(args) == 1:
            self._left_margin =\
            self._top_margin =\
            self._right_margin =\
            self._bottom_margin = max(0, int(args[0]))
        elif len(args) == 4:
            self._left_margin = max(0, int(args[0]))
            self._top_margin = max(0, int(args[1]))
            self._right_margin = max(0, int(args[2]))
            self._bottom_margin = max(0, int(args[3]))
        else:
            raise ValueError(f"set_margin expected 4 arguments but "
                             f"{len(args)} were given")