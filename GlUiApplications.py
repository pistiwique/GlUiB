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


import bpy

from .GlUiCore import GlArea
from .GlUiGui import GlBoxLayout


class GlApplication:
    _handler = None
    _applications = []

    def __init__(self, context):
        GlArea.set_context(context)
        self.setup_handler()

    @classmethod
    def add_application(cls, app):

        cls._applications.append(app)
    
    def connect_event(self, event):
        for app in self._applications:
            if hasattr(app, "connect_event"):
                app.connect_event(event)

    @classmethod
    def setup_handler(cls):
        cls._handler = bpy.types.SpaceView3D.draw_handler_add(
                cls.draw_applications, (), 'WINDOW', 'POST_PIXEL'
                )

    @classmethod
    def remove_handler(cls):
        bpy.types.SpaceView3D.draw_handler_remove(cls._handler, 'WINDOW')

    @classmethod
    def draw_applications(cls):
        for app in cls._applications:
            app.draw()
            
            
class GlWindow(GlBoxLayout, GlArea):
    def __init__(self, scale=150):
        GlBoxLayout.__init__(self)
        self._scale = scale

    def set_scale(self, value):
        self._scale = value

    def _set_geometry(self):
        a_left, a_top, a_right, a_bottom = self.get_view_3d_area()
        self.set_rect(a_left, a_bottom, a_right, self._scale)

    def connect_event(self, event):
        pass

    def draw(self):
        self._set_geometry()
        self.draw_widget(self.get_rect())