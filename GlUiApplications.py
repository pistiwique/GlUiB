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


from .GlUiCore import GlSize, GlArea


class GlApplication:
    _applications = []

    def __init__(self, context):
        GlArea.set_context(context)

    @classmethod
    def add_application(cls, app):
        cls._applications.append(app)
    
    def connect_event(self, event):
        for app in self._applications:
            if hasattr(app, "connect_event"):
                app.connect_event(event)
            
            
class GlWindow(GlSize, GlArea):
    def __init__(self):
        self._alignment = None

    @property
    def alignment(self):
        return self._alignment

    def set_alignment(self, alignment):
        self._alignment = alignment

    def connect_event(self, event):
        print(self.get_view_3d_area())
        