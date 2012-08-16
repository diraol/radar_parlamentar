# coding=utf8

# Copyright (C) 2012, Leonardo Leite
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
from django.test import TestCase
from analises import analise
from importadores import cmsp

class AnaliseTest(TestCase):

    def setUp(self):

        # usa só dados de 2010 pra deixar o teste mais rápido
        importer = cmsp.ImportadorCMSP()
        importer._from_xml_to_bd(cmsp.XML2010) 

    def test_partidos_2d(self):
        """Testa função partido_2d com os dados da câmara municipal de são paulo"""

        an = analise.Analise()
        grafico = an.partidos_2d()

        self.assertAlmostEqual(grafico['PT'][0], -0.44818132, 4)
        self.assertAlmostEqual(grafico['PT'][1], -0.47516022, 4)
        self.assertAlmostEqual(grafico['PSDB'][0], 0.11672679, 4)
        self.assertAlmostEqual(grafico['PSDB'][1], -0.00805108, 4)


