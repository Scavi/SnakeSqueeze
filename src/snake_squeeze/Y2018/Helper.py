from collections import defaultdict


class Cache:
    def __init__(self):
        self.cache = dict()
        self.order = []


    def add(self, key, value):
        self.cache[key] = value
        self.order.append(value)


    def has(self, key):
        return key in self.cache


    def pos_of(self, lookup):
        for i in range(len(self.order)):
            if self.order[i] == lookup:
                return i
        return -1


class Graph:
    def __init__(self):
        self._graph = dict()


    def add_edge(self, source_node, target_node):
        if target_node not in self._graph:
            self._graph[target_node] = set()
        if source_node in self._graph:
            self._graph[source_node].add(target_node)
        else:
            self._graph[source_node] = set()
            self._graph[source_node].add(target_node)


    def topological_sort(self):
        found = set()
        result = list()
        for node, _ in self._graph.items():
            if node not in found:
                self._topological_sort(result, found, node)
        return result


    def _topological_sort(self, result, found, node):
        found.add(node)

        for edge_node in self._graph.get(node):
            if edge_node not in found:
                self._topological_sort(result, found, edge_node)
        result.insert(0, node)


    @property
    def graph(self):
        return self._graph
