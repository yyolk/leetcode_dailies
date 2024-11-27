# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/


class Solution:
    """3243. Shortest Distance After Road Addition Queries I

    You are given an integer `n` and a 2D integer array `queries`.

    There are `n` cities numbered from `0` to `n - 1`. Initially, there is a
    **unidirectional** road from city `i` to city `i + 1` for all `0 <= i < n - 1`.

    `queries[i] = [ui, vi]` represents the addition of a new **unidirectional** road
    from city `ui` to city `vi`. After each query, you need to find the **length** of
    the **shortest path** from city `0` to city `n - 1`.

    Return an array `answer` where for each `i` in the range `[0, queries.length - 1]`,
    `answer[i]` is the *length of the shortest path* from city `0` to city `n - 1` after
    processing the **first** `i + 1` queries."""

    def shortest_distance_after_queries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        # Initialize the graph with n cities, each represented by an empty list of neighbors
        road_network = [[] for _ in range(n)]
        
        # Add initial unidirectional roads from i to i+1 for all cities except the last one
        for current_city in range(n - 1):
            road_network[current_city].append((current_city + 1, 1))  # (next_city, distance)
    
        # Initialize answer list and the array to keep track of minimum distances from city 0 to each city
        shortest_path_answers, min_distances = [], list(range(n))
        
        # Process each query
        for origin, destination in queries:
            # Add the new road from origin to destination with distance 1
            road_network[origin].append((destination, 1))
            
            # Use a priority queue to perform Dijkstra's algorithm
            priority_queue = [(min_distances[origin], origin)]
            
            # Continue until the queue is empty
            while priority_queue:
                current_distance, current_city = heapq.heappop(priority_queue)
                
                # Only process if this distance is the shortest known so far
                if current_distance == min_distances[current_city]:
                    for neighbor, distance_to_neighbor in road_network[current_city]:
                        new_distance = current_distance + distance_to_neighbor
                        
                        # If new distance is shorter, update and add to queue
                        if new_distance < min_distances[neighbor]:
                            heapq.heappush(priority_queue, (new_distance, neighbor))
                            min_distances[neighbor] = new_distance
            
            # After processing the query, append the shortest distance to the last city
            shortest_path_answers.append(min_distances[-1])
        
        return shortest_path_answers

    shortestDistanceAfterQueries = shortest_distance_after_queries
