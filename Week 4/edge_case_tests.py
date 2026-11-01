"""Edge-case tests for the Week 4 A* implementation."""
from lab4_astar_audit import astar


def run_tests():
    same_node = astar({"S": []}, {"S": 0}, "S", "S")
    assert same_node["cost"] == 0
    assert same_node["path"] == ["S"]
    assert same_node["processed"] == ["S"]
    assert same_node["expanded"] == []

    disconnected = {"S": [("A", 2)], "A": [], "G": []}
    no_path = astar(disconnected, {"S": 0, "A": 0, "G": 0}, "S", "G")
    assert no_path["cost"] is None
    assert no_path["path"] == []
    assert no_path["processed"] == ["S", "A"]
    assert no_path["expanded"] == ["S", "A"]

    print("PASS: start equals goal -> path ['S'], cost 0, zero expansions")
    print("PASS: unreachable goal -> no path, search terminates")
    print("All Week 4 edge-case tests passed.")


if __name__ == "__main__":
    run_tests()
