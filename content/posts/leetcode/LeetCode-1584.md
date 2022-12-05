---
title: "LeetCode 1584"
date: 2022-12-05T12:46:30+08:00
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

两种思路：

#### kruskal

利用kruskal算法即可，只不过这里的边需要自己生成，详见思想章节

#### prim

利用prim算法即可，只不过这里的边需要自己生成，详见思想章节

### 代码

#### kruskal

```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xi = points[i][0], yi = points[i][1];
                int xj = points[j][0], yj = points[j][1];
                edges.add(new int[]{i, j, Math.abs(xi - xj) + Math.abs(yi- yj)});
            }
        }
        Collections.sort(edges, (a, b) -> a[2] - b[2]);

        UF uf = new UF(n);
        int mst = 0;
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];
            if (uf.connected(u, v)) {
                continue;
            }

            mst += weight;
            uf.union(u, v);
        }
        return mst;
    }

    class UF {
        // 连通分量个数
        private int count;
        // 存储每个节点的父节点
        private int[] parent;

        // n 为图中节点的个数
        public UF(int n) {
            this.count = n;
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        // 将节点 p 和节点 q 连通
        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);

            if (rootP == rootQ)
                return;

            parent[rootQ] = rootP;
            // 两个连通分量合并成一个连通分量
            count--;
        }

        // 判断节点 p 和节点 q 是否连通
        public boolean connected(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            return rootP == rootQ;
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        // 返回图中的连通分量个数
        public int count() {
            return count;
        }
    }
}
```

#### prim

```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        List<int[]>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xi = points[i][0], yi = points[i][1];
                int xj = points[j][0], yj = points[j][1];
                int weight = Math.abs(xi - xj) + Math.abs(yi- yj);
                graph[i].add(new int[]{i, j, weight});
                graph[j].add(new int[]{j, i, weight});
            }
        }
        return new Prim(graph).getWeightSum();
    }

    class Prim {
        private List<int[]>[] graph;
        private Queue<int[]> pq;
        private boolean[] inMST;
        private int weightSum = 0;

        public Prim(List<int[]>[] graph) {
            this.graph = graph;
            this.pq = new PriorityQueue<>((a, b) -> {
                return a[2] - b[2];
            });
            int n = graph.length;
            inMST = new boolean[n];

            inMST[0] = true;
            cut(0);
            while (!pq.isEmpty()) {
                int[] edge = pq.poll();
                int to = edge[1];
                int weight = edge[2];

                if (inMST[to]) {
                    continue;
                }

                weightSum += weight;
                inMST[to] = true;
                cut(to);
            }
        }

        private void cut(int s) {
            for (int[] edge : graph[s]) {
                int to = edge[1];
                if (inMST[to]) {
                    continue;
                }
                pq.offer(edge);
            }
        }

        private int getWeightSum() {
            return weightSum;
        }

        private boolean allConnected() {
            for (boolean b : inMST) {
                if (!b) {
                    return false;
                }
            }
            return true;
        }
    }
}
```

### References

---

#### 1. [连接所有点的最小费用](https://leetcode.cn/problems/min-cost-to-connect-all-points/)
