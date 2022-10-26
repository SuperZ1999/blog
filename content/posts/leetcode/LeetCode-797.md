---
title: "LeetCode 797"
date: 2022-10-26T23:21:47+08:00
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

经典图的遍历，只不过要同时记录路径

### 代码

```java
class Solution {
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        LinkedList<Integer> path = new LinkedList<>();
        traverse(graph, 0, path);
        return res;
    }

    private void traverse(int[][] graph, int s, LinkedList<Integer> path) {
        // 进入结点时
        path.add(s);
        int n = graph.length - 1;
        if (s == n) {
            res.add(new LinkedList<>(path));
            path.removeLast();
            return;
        }

        for (int v : graph[s]) {
            traverse(graph, v, path);
        }

        // 离开结点时
        path.removeLast();
    }
}
```

### References

---

#### 1. [所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)
