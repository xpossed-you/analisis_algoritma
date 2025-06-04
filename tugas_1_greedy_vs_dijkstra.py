#tfk_061

import heapq

graph = {
    # yang dalam kurung itu tetangga tiap titik dengan jaraknya
    'A': {'B': 5, 'C': 4, 'D': 4},
    'B': {'E': 8},
    'C': {'G': 3},
    'D': {'G': 8},
    'E': {'F': 3},
    'F': {'I': 7},
    'G': {'H': 6},
    'H': {'I': 20}, # jarak H - I diganti dari 4 ke 20
    'I': {}
}

def dijkstra(graph, start, goal):
    queue = [(0, start, [])]
    dilewati = set()
    while queue:
        jarak, titik, jalur = heapq.heappop(queue)
        if titik in dilewati:
            continue
        dilewati.add(titik)
        jalur = jalur + [titik]
        if titik == goal:
            return jalur, jarak
        for neighbor, weight in graph[titik].items():
            if neighbor not in dilewati:
                heapq.heappush(queue, (jarak + weight, neighbor, jalur))
    return None, float('inf')


def algo_greedy(graph, start, goal):
    titik = start
    jalur = [titik]
    total_jarak = 0
    dilewati = set()
    while titik != goal:
        dilewati.add(titik)
        neighbors = graph[titik]
        if not neighbors:
            break
        
        next_titik = min(neighbors, key=neighbors.get)
        total_jarak += neighbors[next_titik]
        titik = next_titik
        jalur.append(titik)
    if titik == goal:
        return jalur, total_jarak
    return None, float('inf')

start = 'A'
goal = 'I'

hasil_greedy = algo_greedy(graph, start, goal)
hasil_dijkstra = dijkstra(graph, start, goal)

print("greedy")
print(f"jalur: {' → '.join(hasil_greedy[0])}")
print(f"total jarak: {hasil_greedy[1]}")

print("dijkstra")
print(f"jalur: {' → '.join(hasil_dijkstra[0])}")
print(f"total jarak: {hasil_dijkstra[1]}")
