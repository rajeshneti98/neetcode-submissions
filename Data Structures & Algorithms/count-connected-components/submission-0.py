class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        visited = set()
        components = 0
        for node in range(n):
            if node in visited:
                continue
            q = deque([node])
            while q:
                size = len(q)
                for i in range(size):
                    curr = q.popleft()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    for neighbor in d[curr]:
                        if neighbor  in visited:
                            continue
                        q.append(neighbor)
            components+=1               

        return components
        