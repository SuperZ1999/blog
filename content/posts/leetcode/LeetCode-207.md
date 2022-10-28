---
title: "LeetCode 207"
date: 2022-10-28T20:32:56+08:00
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

这道题其实就是检测图里是否有环

#### 思路一

利用图的DFS，首先构建图，把prerequisites当成图的边，然后利用图的DFS遍历模板遍历该图，同时记录路径里的结点，如果路径里的结点重复就是有环，记录结果并返回

#### 思路二

利用图的BFS，首先构建图，把prerequisites当成图的边，注意BFS时，只能让入度为零的结点入队列即可，最后判断访问过的结点个数是否等于总结点个数

### 代码

#### 思路一

```java
class Solution {
    private boolean[] visited;
    private boolean[] onPath;
    private boolean hasCycle = false;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        visited = new boolean[numCourses];
        onPath = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i]) {
                traverse(graph, i);
            }
        }
        return !hasCycle;
    }

    private void traverse(List<Integer>[] graph, int s) {
        if (onPath[s]) {
            hasCycle = true;
            return;
        }
        if (visited[s]) {
            return;
        }

        visited[s] = true;
        onPath[s] = true;

        for (Integer n : graph[s]) {
            traverse(graph, n);
        }

        onPath[s] = false;
    }

    private List<Integer>[] buildGraph(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int[] edge : prerequisites) {
            int from = edge[1], to = edge[0];
            graph[from].add(to);
        }
        return graph;
    }
}
```

#### 思路二

```java
class Solution {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        int[] indegree = new int[numCourses];
        for (int[] edge : prerequisites) {
            int to = edge[0];
            indegree[to]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        int count = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            count++;
            for (Integer next : graph[node]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }

        return count == numCourses;
    }

    private List<Integer>[] buildGraph(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new List[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int[] edge : prerequisites) {
            int from = edge[1], to = edge[0];
            graph[from].add(to);
        }
        return graph;
    }
}
```

### References

---

#### 1. [课程表](https://leetcode.cn/problems/course-schedule/)
