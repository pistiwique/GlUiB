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


from .GlUiCore import GlObject, GlRectangle
from .GlUiGl import GPU_RectanglePoly

class GlLayout(GlObject):
    def __init__(self):
        GlObject.__init__(self)
        self._left_margin = 0
        self._top_margin = 0
        self._right_margin = 0
        self._bottom_margin = 0

    @property
    def margins(self):
        """
        Property that hold the margins of the layout
        :return: tuple of int (left, top, right, bottom)
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


class GlBoxLayout(GlRectangle, GlLayout):
    def __init__(self):
        GlRectangle.__init__(self)
        GlLayout.__init__(self)
        self._layouts = []
        self._widgets = []
        self._background_color = (0.0, 0.0, 0.0, 0.0)

    @property
    def background_color(self):

        return self._background_color

    def set_background_color(self, r: float, g: float, b: float, a: float):
        self._background_color = (
            max(0, min(1, r)),
            max(0, min(1, g)),
            max(0, min(1, b)),
            max(0, min(1, a))
            )

    def add_layout(self, layout):
        self._layout.append(layout)

    def add_widget(self, widget):
        self._widgets.append(widget)

    def draw_widget(self, vertices):
        l, t, r, b = vertices
        ml, mt, mr, mb = self.margins

        verts = ((l+ml, b+mb), # bottom-left
                 (r-mr, b+mb), # bottom-right
                 (l+ml, t-mt), # top-left
                 (r-mr, t-mt)  # top-right
                 )
        GPU_RectanglePoly().draw(verts, self.background_color)