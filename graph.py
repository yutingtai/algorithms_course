from typing import Dict, List
from unittest import TestCase
from queue import SimpleQueue


def can_bike(graph: Dict[str, List[str]], start_node: str, end_node: str) -> bool:
    q = SimpleQueue()
    visited = set()
    q.put(start_node)
    while not q.empty():
        element = q.get()
        if element == end_node:
            return True
        if element not in visited:
            visited.add(element)
            for neighbor in graph[element]:
                q.put(neighbor)

    return False


class CanBikeFromTest(TestCase):
    @staticmethod
    def get_graph():
        return {
            "a": ["b", "c", "z"],
            "b": ["a", "c", "y"],
            "c": ["a", "b", "d"],
            "d": ["f", "c", "e"],
            "e": ["d", "x"],
            "f": ["g", "d"],
            "g": ["f"],
            "h": [],
            "x": ["e"],
            "y": ["b"],
            "z": ["a"]
        }

    def test_reachable_neighbor(self):
        result = can_bike(self.get_graph(), start_node="b", end_node="a")
        self.assertTrue(result)

    def test_unreachable(self):
        result = can_bike(self.get_graph(), start_node="h", end_node="f")
        self.assertIsNotNone(result)
        self.assertFalse(result)

    def test_reachable_not_neighbor(self):
        result = can_bike(self.get_graph(), start_node="e", end_node="a")
        self.assertTrue(result)
