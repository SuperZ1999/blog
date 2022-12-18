---
title: "LeetCode 1971"
date: 2022-12-19T00:24:17+08:00
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

利用并查集的思想即可

### 代码

```java
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        UF uf = new UF(n);
        for (int[] edge : edges) {
            uf.union(edge[0], edge[1]);
        }
        return uf.isConnected(source, destination);
    }

    class UF {
        private int[] parent;

        public UF(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        private int find(int x) {
            if (x != parent[x]) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        private void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ) {
                return;
            }
            parent[rootP] = rootQ;
        }

        private boolean isConnected(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            return rootP == rootQ;
        }
    }
}
```

### References

---

#### 1. [寻找图中是否存在路径](https://leetcode.cn/problems/find-if-path-exists-in-graph/)
