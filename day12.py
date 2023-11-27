from helper.fetchInput import get_input
from collections import defaultdict


day_input = get_input(12).strip().split("\n")


edges = defaultdict(set)
for line in day_input:
    lhs, rhs = line.strip().split("-", maxsplit=2)
    edges[lhs].add(rhs)
    edges[rhs].add(lhs)


def walk(current, path, bonus, edges):
    if current == "end":
        yield path
    else:
        for next_edge in edges[current]:
            if next_edge == "start":
                pass
            elif next_edge.isupper() or next_edge not in path:
                yield from walk(next_edge, path + [next_edge], bonus, edges)
            elif next_edge.islower() and bonus:
                yield from walk(next_edge, path + [next_edge], False, edges)

sum(1 for _ in walk("start", ["start"], True, edges))
