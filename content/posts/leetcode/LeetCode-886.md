---
title: "LeetCode 886"
date: 2022-11-03T16:58:49+08:00
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

经典二分图判断，只不过需要先构造一个图，详见思想章节

### 代码

```java
class Solution {
    private boolean ok = true;
    private boolean[] color;
    private boolean[] visited;

    public boolean possibleBipartition(int n, int[][] dislikes) {
        color = new boolean[n + 1];
        visited = new boolean[n + 1];
        List<Integer>[] graph = buildGraph(n, dislikes);

        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                traverse(graph, i);
            }
        }
        return ok;
    }

    private List<Integer>[] buildGraph(int n, int[][] dislikes) {
        List<Integer>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new LinkedList<>();
        }

        for (int[] dislike : dislikes) {
            int s = dislike[0];
            int d = dislike[1];
            graph[s].add(d);
            graph[d].add(s);
        }

        return graph;
    }

    private void traverse(List<Integer>[] graph, int v) {
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

### References

---

#### 1. [可能的二分法](https://leetcode.cn/problems/possible-bipartition/)
