---
title: "LeetCode 743"
date: 2022-12-04T20:17:02+08:00
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

经典dijkstra问题，利用dijkstra模板即可，详见思想章节

### 代码

```java
class Solution {
    class State {
        int id;
        int distFromStart;

        public State(int id, int distFromStart) {
            this.id = id;
            this.distFromStart = distFromStart;
        }
    }

    private int[] dijkstra(List<int[]>[] graph, int start) {
        int[] distTo = new int[graph.length];
        Arrays.fill(distTo, Integer.MAX_VALUE);
        distTo[start] = 0;

        Queue<State> pq = new PriorityQueue<>((a, b) -> {
            return a.distFromStart - b.distFromStart;
        });
        pq.offer(new State(start, 0));

        while (!pq.isEmpty()) {
            State curState = pq.poll();
            int curNodeId = curState.id;
            int curDistFromStart = curState.distFromStart;

            if (curDistFromStart > distTo[curNodeId]) {
                continue;
            }

            for (int[] neighbor : graph[curNodeId]) {
                int neighborId = neighbor[0];
                int distToNeighbor = distTo[curNodeId] + neighbor[1];
                if (distToNeighbor < distTo[neighborId]) {
                    distTo[neighborId] = distToNeighbor;
                    pq.offer(new State(neighborId, distToNeighbor));
                }
            }
        }

        return distTo;
    }

    public int networkDelayTime(int[][] times, int n, int k) {
        List<int[]>[] graph = new List[n + 1];
        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] time : times) {
            int from =  time[0];
            int to =  time[1];
            int weight =  time[2];
            graph[from].add(new int[]{to, weight});
        }

        int[] distTo = dijkstra(graph, k);

        int res = 0;
        for (int i = 1; i < n + 1; i++) {
            if (distTo[i] == Integer.MAX_VALUE) {
                return -1;
            }
            res = Math.max(res, distTo[i]);
        }
        return res;
    }
}
```

### References

---

#### 1. [网络延迟时间](https://leetcode.cn/problems/network-delay-time/)
