#!/usr/bin/env python

# Copyright (C) 2006-2016  Music Technology Group - Universitat Pompeu Fabra
#
# This file is part of Essentia
#
# Essentia is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the Affero GNU General Public License
# version 3 along with this program. If not, see http://www.gnu.org/licenses/

from essentia.standard import MinMax

from essentia_test import TestCase, TextTestRunner, allTests

class TestMinMax(TestCase):

    def testDefaultIsMin(self):
        """Making the Algorithm with no type defaults to min"""
        value, index = MinMax()([3,1,2])
        self.assertEqual(value, 1.0)
        self.assertEqual(index, 0)

    def testEmpty(self):
        self.assertComputeFails(MinMax()(), [])

    def testAllSame(self):
        value, index = MinMax()([0]*10)
        self.assertEqual(value, 0.0)
        self.assertEqual(index, 0)

    def testOne(self):
        value, index = MinMax()([100])
        self.assertEqual(value, 100.0)
        self.assertEqual(index, 0)

    def testMulti(self):
        value, index = MinMax()([5, 8, 4, 9, 1])
        self.assertEqual(value, 1.0)
        self.assertEqual(index, 4)

    def testNegatives(self):
        value, index = MinMax()([3, 7, -45, 2, -1, 0])
        self.assertEqual(value, -45.0)
        self.assertEqual(index, 2)

    def testMixedTypes(self):
        value, index = MinMax()([4, 5, 3.3])
        self.assertAlmostEqual(value, 3.3)
        self.assertEqual(index, 2)

    def testNonNumeric(self):
        self.assertComputeFails(MinMax()(['a', 1]))

    def testMax(self):
        value, index = MinMax(type="max")([3, 7, -45, 2, -1, 0])
        self.assertEqual(value, 7)
        self.assertEqual(index, 1)

suite = allTests(TestMinMax)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
