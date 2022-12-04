---
title: "LeetCode 1514"
date: 2022-12-04T22:07:34+08:00
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

dijkstra问题的变种，利用dijkstra模板即可，主要有两个注意点：

- 首先需要构造图，构造图时注意无向图的一条边相当于两条有向边
- weight计算方式与普通的dijkstra不同，即需要修改weight函数

### 代码

```java
class Solution {
    class State {
        int id;
        double probFromStart;

        public State(int id, double probFromStart) {
            this.id = id;
            this.probFromStart = probFromStart;
        }
    }

    private double dijkstra(List<double[]>[] graph, int start, int end) {
        double[] probTo = new double[graph.length];
        Arrays.fill(probTo, -1);
        probTo[start] = 1;

        Queue<State> pq = new PriorityQueue<State>((a, b) -> {
            return Double.compare(b.probFromStart, a.probFromStart);
        });
        pq.offer(new State(start, 1));

        while (!pq.isEmpty()) {
            State curState = pq.poll();
            int curNodeId = curState.id;
            double curProbFromStart = curState.probFromStart;

            if (curNodeId == end) {
                return probTo[end];
            }

            if (curProbFromStart < probTo[curNodeId]) {
                continue;
            }

            for (double[] neighbor : graph[curNodeId]) {
                int nextId = (int) neighbor[0];
                double nextProbFromStart = curProbFromStart * neighbor[1];
                if (nextProbFromStart > probTo[nextId]) {
                    probTo[nextId] = nextProbFromStart;
                    pq.offer(new State(nextId, nextProbFromStart));
                }
            }
        }
        return 0.0;
    }

    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        List<double[]>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < succProb.length; i++) {
            int from = edges[i][0];
            int to = edges[i][1];
            double weight = succProb[i];
            graph[from].add(new double[]{to, weight});
            graph[to].add(new double[]{from, weight});
        }
        return dijkstra(graph, start, end);
    }
}
```

### References

---

#### 1. [概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/)
