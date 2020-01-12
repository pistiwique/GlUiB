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

    def get_3d_view(self):
        for area in self.context.screen.areas:
            if area.type != 'VIEW_3D':
                continue
            return area

    def get_view_3d_area(self):
        if self.context is None:
            return

        area = self.get_3d_view()
        if area is None:
            return

        system = self.context.preferences.system
        width = area.width
        height = area.height

        left = 0
        top = height
        right = width
        bottom = 0

        if system.use_region_overlap:
            for region in area.regions:
                if region.type == 'TOOLS':
                    left += region.width
                elif region.type == 'UI':
                    right -= region.width
                elif region.type == 'HEADER':
                    top -= region.height

        return left, top, right, bottom


class GlRectangle:
    def __init__(self, x=0, y=0, w=10, h=10):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    @property
    def x(self):
        """
        Returns the x-coordinate of the rectangle’s left edge relative to
        its parent.
        Equivalent to GlUiB.GlUiCore.GlRectangle.left().
        :return: int
        """
        return self._x

    @property
    def y(self):
        """
        Returns the y-coordinate of the rectangle’s bottom edge relative to
        its parent.
        Equivalent to GlUiB.GlUiCore.GlRectangle.bottom().
        :return: int
        """
        return self._y

    def set_location(self, x: int, y: int):
        """
        Set the position of the rectangle's bottom-left corner with the
        given 'x' and 'y'.
        :param x: int
        :param y: int
        """
        self._x, self._y = max(0, int(x)), max(0, int(y))

    @property
    def left(self):
        """
        Return the x-coordinate of the rectangle's left edge.
        Equivalent to GlUiB.GlUiCore.GlRectangle.x
        :return: int
        """
        return self.x

    @property
    def top(self):
        """
        Return the y-coordinate of the rectangle's top edge.
        :return: int
        """
        return self.y + self.height

    @property
    def right(self):
        """
        Return the x-coordinate of the rectangle's right edge.
        Equivalent to GlUiB.GlUiCore.GlRectangle.x
        :return: int
        """
        return self.x + self.width

    @property
    def bottom(self):
        """
        Return the y-coordinate of the rectangle's bottom edge.
        Equivalent to GlUiB.GlUiCore.GlRectangle.y
        :return: int
        """
        return self.y

    @property
    def width(self):
        """
        Return the width of the rectangle.
        :return: int
        """
        return self._width

    @property
    def height(self):
        """
        Return the height of the rectangle.
        :return: int
        """
        return self._height

    def set_width(self, w: int):
        """
        Set the width of the rectangle
        :param w: int
        """
        self._width = max(0, int(w))

    def set_height(self, h: int):
        """
        Set the height of the rectangle
        :param h: int
        """
        self._height = max(0, int(h))

    def set_size(self, w: int, h: int):
        """
        Set the size of the rectangle with to the given 'width' and 'height'.
        :param w: int
        :param h: int
        """
        self._width, self._height = max(0, int(w)), max(0, int(h))

    def get_rect(self):
        """
        Return the position of the rectangle's bottom-left corner to 'x' and 'y',
        and its dimensions to 'width' and 'height'.
        :return: (x: int, y: int, width: int, height: int)
        """
        return (self.x, self.y, self.width, self.height)

    def set_rect(self, x: int, y: int, w: int, h: int):
        """
        Sets the coordinates of the rectangle’s bottom-left corner to
        'x' and 'y', and its size to the given 'width' and 'height'.
        :param x: int
        :param y: int
        :param w: int
        :param h: int
        """
        self.set_location(x, y)
        self.set_size(w, h)