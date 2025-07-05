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

