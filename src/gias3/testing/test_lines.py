"""
FILE: test_lines.py
LAST MODIFIED: 24-12-2015 
DESCRIPTION: Tests for Line3D and LineSegment3D classes

===============================================================================
This file is part of GIAS2. (https://bitbucket.org/jangle/gias2)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
===============================================================================
"""
import unittest

from gias3.common import geoprimitives as gp


class TestDistanceToLine(unittest.TestCase):

    def test_distance_to_line(self):
        l1 = gp.Line3D([1, 1, 0], [0, 0, 0])
        l2 = gp.Line3D([1, 1, 0], [0, 0, 0])

        d, t1c, t2c = l1.calcClosestDistanceToLine(l2)

        self.assertAlmostEqual(d, 0.0, 7)
        self.assertAlmostEqual(t1c, 0.0, 7)
        self.assertAlmostEqual(t2c, 0.0, 7)

    def test_distance_to_line_2(self):
        l1 = gp.Line3D([1, 1, 0], [0, 0, 0])
        l2 = gp.Line3D([1, 2, 0], [0, 0, 0])

        d, t1c, t2c = l1.calcClosestDistanceToLine(l2)

        self.assertAlmostEqual(d, 0.0, 7)
        self.assertAlmostEqual(t1c, 0.0, 7)
        self.assertAlmostEqual(t2c, 0.0, 7)

    def test_distance_to_line_segment(self):
        s1 = gp.LineSegment3D([1, 0, 0], [0, 0, 0], -1, 0)
        s2 = gp.LineSegment3D([1, 0, 0], [0, 0, 0], -5, -4)

        d, t1c, t2c = s1.calcClosestDistanceToLine(s2)

        self.assertAlmostEqual(d, 0.0, 7)
        self.assertAlmostEqual(t1c, 0.0, 7)
        self.assertAlmostEqual(t2c, 0.0, 7)

    def test_distance_to_line_segment_2(self):
        s1 = gp.LineSegment3D([1, 0, 0], [0, 0, 0], -1, 0)
        s2 = gp.LineSegment3D([1, 2, 0], [0, 0, 0], -5, -4)

        d, t1c, t2c = s1.calcClosestDistanceToLine(s2)

        self.assertAlmostEqual(d, 0.0, 7)
        self.assertAlmostEqual(t1c, 0.0, 7)
        self.assertAlmostEqual(t2c, 0.0, 7)


if __name__ == '__main__':
    unittest.main()
