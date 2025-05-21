import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dorplan.tests.data.graph_coloring import GraphColoring
from dorplan.app import DorPlan


class AppTest(unittest.TestCase):
    def test_open_app(self):
        DorPlan(GraphColoring, {})
        return 1


if __name__ == "__main__":
    unittest.main()
