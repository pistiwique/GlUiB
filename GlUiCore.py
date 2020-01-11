# -*- coding:utf-8 -*-

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


class GlObject:
    def __init__(self, parent=None):
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent


class GlArea:

    _context = None

    @property
    def context(self):
        return self._context

    @classmethod
    def set_context(cls, context):
        cls._context = context

    def get_view_3d_area(self):
        if self.context is None:
            return

        system = self.context.preferences.system
        width = self.context.region.width
        height = self.context.region.height

        left = 0
        top = height
        right = width
        bottom = 0

        if system.use_region_overlap:
            for region in self.context.area.regions:
                if region.type == 'TOOLS':
                    left += region.width
                elif region.type == 'UI':
                    right -= region.width
                elif region.type == 'HEADER':
                    top -= region.height

        return left, top, right, bottom


class GlLocation:
    def __init__(self):
        self._location_x = 0
        self._location_y = 0

    @property
    def location_x(self):
        """
        This property holds the x coordinate of the widget relative to its parent
        :return: int
        """
        return self._location_x

    @property
    def location_y(self):
        """
        This property holds the y coordinate of the widget relative to its
        parent
        :return: int
        """
        return self._location_y

    @property
    def location(self):
        """
        This property holds the coordinates of the widget relative to its
        parent
        :return: (x: int, y: int)
        """
        return (self.location_x, self.location_y)

    def set_location(self, x: int, y: int):
        self._location_x, self._location_y = max(0, int(x)), max(0, int(y))


class GlSize:
    def __init__(self):
        self._width = 0
        self._height = 0

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def size(self):
        return (self.width, self.height)

    def set_size(self, w: int, h: int):
        self._width, self._height = max(0, int(w)), max(0, int(h))