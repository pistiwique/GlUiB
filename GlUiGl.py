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


import gpu
import bgl
from gpu_extras.batch import batch_for_shader


class GPU_RectanglePoly:
    _indices = ((0, 1, 2), (2, 1, 3))

    def draw(self, vertices, color):
        shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
        batch = batch_for_shader(shader,
                                 'TRIS',
                                 {"pos": vertices},
                                 indices=self._indices
                                 )
        bgl.glEnable(bgl.GL_BLEND)
        shader.bind()
        shader.uniform_float("color", color)
        batch.draw(shader)
