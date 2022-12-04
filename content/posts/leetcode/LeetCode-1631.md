---
title: "LeetCode 1631"
date: 2022-12-04T21:20:32+08:00
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

利用dijkstra的思想，只不过需要把矩阵里的每个元素当成一个结点，求一个结点的相邻结点与一般的图不同（即adj函数），而且最后求的体力消耗是路径上体力的最大值，不是体力消耗之和，所以刷新权重的时候需要编写相应的weight函数

其实dijsktra问题的变种只要编写相应的adj函数和weight函数即可

### 代码

```java
class Solution {
    class State {
        int x, y;
        int effortFromStart;

        public State(int x, int y, int effortFromStart) {
            this.x = x;
            this.y = y;
            this.effortFromStart = effortFromStart;
        }
    }

    private int[][] dirs = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    private List<int[]> adj(int[][] matrix, int x, int y) {
        int m = matrix.length, n = matrix[0].length;
        List<int[]> neighbors = new ArrayList<>();
        for (int[] dir : dirs) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                continue;
            }
            neighbors.add(new int[]{nx, ny});
        }
        return neighbors;
    }

    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] effortTo = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(effortTo[i], Integer.MAX_VALUE);
        }
        effortTo[0][0] = 0;

        Queue<State> pq = new PriorityQueue<>((a, b) -> {
            return a.effortFromStart - b.effortFromStart;
        });
        pq.offer(new State(0, 0, 0));

        while (!pq.isEmpty()) {
            State curState = pq.poll();
            int curX = curState.x;
            int curY = curState.y;
            int curEffortFromStart = curState.effortFromStart;

            if (curX == m -1 && curY == n - 1) {
                return curEffortFromStart;
            }

            if (curEffortFromStart > effortTo[curX][curY]) {
                continue;
            }

            for (int[] neighbor : adj(heights, curX, curY)) {
                int nextX = neighbor[0];
                int nextY = neighbor[1];
                int nextEffort = Math.max(effortTo[curX][curY], Math.abs(heights[nextX][nextY] - heights[curX][curY]));
                if (nextEffort < effortTo[nextX][nextY]) {
                    effortTo[nextX][nextY] = nextEffort;
                    pq.offer(new State(nextX, nextY, nextEffort));
                }
            }
        }
        return -1;
    }
}
```

### References

---

#### 1. [最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/)

