import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}  # Initialize all nodes

        for u, v, w in times:
            graph[u].append((v, w))  # Directed edge

        distances = [float('inf')] * (n + 1)  # 1-based indexing
        distances[k] = 0  # Starting node distance is 0

        pq = [(0, k)]  # (distance, node)

        while pq:
            d, node = heapq.heappop(pq)
            if d > distances[node]:
                continue

            for neighbor, weight in graph.get(node, []):
                new_dist = d + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        max_dist = max(distances[1:])  # Ignore index 0

        return max_dist if max_dist != float('inf') else -1
