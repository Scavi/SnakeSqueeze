class Day8MemoryManeuver:
    def __init__(self, use_reference_count=False):
        """
        Args:
            use_reference_count (bool):
                True: If an entry has child nodes, the meta data are referring to the results of
                    the child node
                False: Sum all meta data up
        """
        self._use_child_references = use_reference_count

    def solve(self, license_input):
        _, result = self._solve(license_input.split(" "), 0)
        return result

    def _solve(self, structure, pos):
        if pos >= len(structure):
            return pos, 0
        child_node_count = int(structure[pos])
        pos += 1
        meta_count = int(structure[pos])
        result = 0
        child_results = []
        for i in range(child_node_count):
            pos += 1
            pos, tmp = self._solve(structure, pos)
            if not self._use_child_references:
                result += tmp
            child_results.append(tmp)
        if meta_count > 0:
            for i in range(pos, pos + meta_count):
                current = int(structure[i + 1])
                if self._use_child_references and child_node_count > 0:
                    if current <= len(child_results):
                        result += child_results[current - 1]
                else:
                    result += current
                pos += 1
        return pos, result
