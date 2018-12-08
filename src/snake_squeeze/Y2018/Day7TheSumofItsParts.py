import re

ASCII_SUB = 64


class Day7TheSumOfItsParts:
    def __init__(self, worker_count=1, step_duration=0):
        self.all_worker = list()
        for i in range(0, worker_count):
            self.all_worker.append(_Worker(i, step_duration))

    def solve1(self, steps):
        step_order = ""
        step_graph = self._create_step_graph(steps)
        processable = self._find_start(step_graph)
        while len(processable) != 0:
            current_node = step_graph.get(processable.pop(0))
            for next_node in current_node.next:
                next_node.prev.remove(current_node)
                if len(next_node.prev) == 0:
                    processable.append(next_node.node_id)
            list.sort(processable)
            step_order += current_node.node_id
            current_node.is_processed = True
            if len(processable) == 0:
                processable = self._find_start(step_graph)
        return step_order

    def solve2(self, steps):
        step_order = ""
        step_graph = self._create_step_graph(steps)
        processable = self._find_start(step_graph)
        i = -1
        while self._is_working(processable):
            i += 1
            for worker in self.all_worker:
                if worker.is_available() and len(processable) > 0:
                    worker.work(step_graph.get(processable.pop(0)))
                else:
                    if worker.has_finished(processable):
                        if len(processable) > 0:
                            worker.work(step_graph.get(processable.pop(0)))
                        step_order += worker.current_node.node_id
        return i

    def _is_working(self, processable):
        if len(processable) != 0:
            return True
        for worker in self.all_worker:
            if not worker.is_available():
                return True
        return False

    @staticmethod
    def _find_start(step_graph):
        steps = []
        for _, value in step_graph.items():
            if len(value.prev) == 0 and not value.is_processed:
                steps.append(value.node_id)
        list.sort(steps)
        return steps

    def _create_step_graph(self, steps):
        graph = dict()
        for current_steps in steps:
            lookup = self._get_step(current_steps, "(?<=Step\s)[^m]*")
            if lookup in graph:
                parent = graph.get(lookup)
            else:
                parent = _Node(lookup)
                graph[lookup] = parent
            parent.add(graph, self._get_step(current_steps, "(?<=step\s)[^c]*"))
        return graph

    @staticmethod
    def _get_step(current_steps, pattern):
        lookup = re.search(pattern, current_steps)
        if not lookup:
            raise ValueError("Illegal lookup for the steps in '{}'!".format(current_steps))
        return lookup.group(0).strip()


class _Worker:
    def __init__(self, worker_id, duration):
        self.duration = duration
        self.worker_id = worker_id
        self.current_node = None
        self.working_time = 0

    def is_available(self):
        return self.working_time == 0

    def work(self, current_node):
        if self.working_time > 0:
            raise ValueError("I am already working...")
        self.current_node = current_node
        self.working_time = self.duration + ord(current_node.node_id) - ASCII_SUB

    def has_finished(self, processable):
        if self.working_time > 0:
            self.working_time -= 1
            if self.is_available():
                for next_node in self.current_node.next:
                    next_node.prev.remove(self.current_node)
                    if len(next_node.prev) == 0:
                        processable.append(next_node.node_id)
                list.sort(processable)
                self.current_node.is_processed = True
                return True
        return False


class _Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.prev = set()
        self.next = []
        self.is_processed = False

    def add(self, graph, lookup):
        if lookup in graph:
            child = graph.get(lookup)
        else:
            child = _Node(lookup)
            graph[lookup] = child
        child.prev.add(self)
        self.next.append(child)
        list.sort(self.next)

    def __lt__(self, other):
        return self.node_id < other.node_id

    def __repr__(self):
        return "{} (prev={})".format(self.node_id, len(self.prev))
