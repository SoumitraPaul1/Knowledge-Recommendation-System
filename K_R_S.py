class KnowledgeGraph:
    def __init__(self):
        self.graph = {}  
        self.learned = set()

    def add_topic(self, topic):
        if topic not in self.graph:
            self.graph[topic] = []

    def add_prerequisite(self, topic, prereq):
        self.add_topic(topic)
        self.add_topic(prereq)
        self.graph[topic].append(prereq)

    def mark_learned(self, topic):
        self.learned.add(topic)

    def get_prerequisites(self, topic):
        visited = set()
        result = []

        def dfs(v):
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    result.append(neighbor)

        dfs(topic)
        result.reverse()
        return result

    def get_next_learnable(self):
        next_topics = []
        for topic in self.graph:
            if topic not in self.learned:
                if all(prereq in self.learned for prereq in self.graph[topic]):
                    next_topics.append(topic)
        return next_topics


kg = KnowledgeGraph()


kg.add_prerequisite("Machine Learning", "Algorithms")
kg.add_prerequisite("Deep Learning", "Machine Learning")
kg.add_prerequisite("Algorithms", "Data Structures")
kg.add_prerequisite("Data Structures", "Programming Basics")


print("To learn Deep Learning, you need:")
print(" <- ".join(kg.get_prerequisites("Deep Learning")))


kg.mark_learned("Programming Basics")
kg.mark_learned("Data Structures")


print("You can now learn:", kg.get_next_learnable())


