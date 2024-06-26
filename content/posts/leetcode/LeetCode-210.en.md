---
title: "LeetCode 210"
date: 2022-10-28T21:47:32+08:00
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

寻找可行的选课顺序其实就是计算拓扑排序

#### 思路一

利用图的DFS，只要是无环的有向图，就有拓扑排序，所以需要像207题一样判断是否有环，如果无环，那么只需要反转该图的后序遍历序列就得到了该图的拓扑排序

#### 思路二

利用图的BFS，只不过只把入度为零的结点加入队列，队列出队的序列就是该图的拓扑排序

### 代码

#### 思路一

```java
class Solution {
    private boolean[] visited;
    private boolean[] onPath;
    private boolean hasCycle = false;
    private List<Integer> postorder = new LinkedList<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = buildGraph(numCourses, prerequisites);
        visited = new boolean[numCourses];
        onPath = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i]) {
                traverse(graph, i);
            }
        }
        if (hasCycle) {
            return new int[0];
        }
        Collections.reverse(postorder);
        int[] res = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            res[i] = postorder.get(i);
        }
        return res;
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
        postorder.add(s);
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
    public int[] findOrder(int numCourses, int[][] prerequisites) {
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
        int[] res = new int[numCourses];
        while (!queue.isEmpty()) {
            int node = queue.poll();
            res[count] = node;
            count++;
            for (Integer next : graph[node]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }

        if (count != numCourses) {
            return new int[0];
        }
        return res;
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

#### 1. [课程表 II](https://leetcode.cn/problems/course-schedule-ii/)
