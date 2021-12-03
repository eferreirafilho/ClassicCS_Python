# Add a counter to dfs(), bfs(), and astar() to see how many states each
# searches through for the same maze. Find the counts for 100 different mazes to
# get statistically significant results.

import timeit
from datetime import timedelta
from generic_search import dfs, bfs, node_to_path, astar, Node
import numpy as np
from maze import Maze, MazeLocation, manhattan_distance
from typing import List, NamedTuple, Callable, Optional

if __name__ == '__main__':

    trials = 100

    dfs_total,dfs_solutions,bfs_total,bfs_solutions,astar_total,astar_solutions = 0,0,0,0,0,0  # Initialize Counter

    for i in range(trials):
        m: Maze = Maze()
        solution1: Optional[Node[MazeLocation]] = dfs(m.start, m.goal_test, m.successors)
        if solution1 is not None:
            path1: List[MazeLocation] = node_to_path(solution1)
            m.mark(path1)
            m.clear(path1)
            dfs_total=dfs_total+len(path1)
            dfs_solutions=dfs_solutions+1
        solution2: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successors)
        if solution2 is not None:
            path2: List[MazeLocation] = node_to_path(solution2)
            m.mark(path2)
            m.clear(path2)
            bfs_total = bfs_total+len(path2)
            bfs_solutions = bfs_solutions+1
        distance: Callable[[MazeLocation], float] = manhattan_distance(m.goal)
        solution3: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test, m.successors, distance)
        if solution3 is not None:
            path3: List[MazeLocation] = node_to_path(solution3)
            m.mark(path3)
            m.clear(path3)
            astar_total = astar_total+len(path3)
            astar_solutions = astar_solutions+1

    print('DFS | Solutions found: ',dfs_solutions,' Path sum: ',dfs_total)
    print('BFS | Solutions found: ', bfs_solutions, ' Path sum: ', bfs_total)
    print('A* | Solutions found: ', astar_solutions, ' Path sum: ', astar_total)
