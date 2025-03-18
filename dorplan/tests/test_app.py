import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

DATADIR = os.path.join(os.path.dirname(__file__), "data")
ALMOST_KEYS = ["best_solution", "best_bound"]

from data.graph_coloring import GraphColoring
from dorplan.app import DorPlan


class AppTest(unittest.TestCase):
    def test_open_app(self):
        return DorPlan(GraphColoring, {})


if __name__ == "__main__":
    unittest.main()
