class ProbabilityTree:
    def __init__(self):
        self.tree = {}

    def add_path(self, path, probability):
        """
        Add a path to the probability tree.
        :param path: List of events (e.g., ["A", "B", "C"]).
        :param probability: Probability of the path (e.g., 0.2).
        """
        current = self.tree
        for event in path[:-1]:
            if event not in current:
                current[event] = {}
            current = current[event]
        # Add the last event with its probability
        current[path[-1]] = probability

    def display_tree(self, current=None, indent=0):
        """
        Display the tree in a readable format.
        """
        if current is None:
            current = self.tree
        for key, value in current.items():
            print("  " * indent + f"{key}: {value}" if isinstance(value, float) else "  " * indent + key)
            if isinstance(value, dict):
                self.display_tree(value, indent + 1)


# Example Usage
if __name__ == "__main__":
    tree = ProbabilityTree()
    tree.add_path(["Start", "A", "B"], 0.3)
    tree.add_path(["Start", "A", "C"], 0.2)
    tree.add_path(["Start", "D", "E"], 0.5)

    print("Probability Tree:")
    tree.display_tree()
