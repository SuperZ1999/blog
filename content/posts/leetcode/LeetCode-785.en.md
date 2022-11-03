---
title: "LeetCode 785"
date: 2022-11-03T16:17:09+08:00
categories: ["leetcode"]
tags: ["leetcode"]
description: ""
weight:
slug: ""
draft: false
disableShare: false
cover:
    image: ""
    caption: ""
    alt: ""
    relative: false
---

### 思路

经典二分图判断问题，利用二分图判断模板即可，有dfs和bfs两种做法，详见思想章节

### 代码

#### DFS

```java
class Solution {
    private boolean ok = true;
    private boolean[] color;
    private boolean[] visited;

    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        color = new boolean[n];
        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                traverse(graph, i);
            }
        }
        return ok;
    }
    
    private void traverse(int[][] graph, int v) {
        if (!ok) {
            return;
        }
        
        visited[v] = true;
        for (int neighbor : graph[v]) {
            if (!visited[neighbor]) {
                color[neighbor] = !color[v];
                traverse(graph, neighbor);
            } else {
                if (color[v] == color[neighbor]) {
                    ok = false;
                    return;
                }
            }
        }
    }
}
```

#### BFS

```java
class Solution {
    private boolean ok = true;
    private boolean[] color;
    private boolean[] visited;

    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        color = new boolean[n];
        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                traverse(graph, i);
            }
        }
        return ok;
    }

    private void traverse(int[][] graph, int start) {
        if (!ok) {
            return;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        visited[start] = true;
        queue.offer(start);
        while (!queue.isEmpty() && ok) {
            int v = queue.poll();
            for (int n : graph[v]) {
                if (!visited[n]) {
                    color[n] = !color[v];
                    visited[n] = true;
                    queue.offer(n);
                } else {
                    if (color[n] == color[v]) {
                        ok = false;
                        return;
                    }
                }
            }
        }
    }
}
```

### References

---

#### 1. [判断二分图](https://leetcode.cn/problems/is-graph-bipartite/)
