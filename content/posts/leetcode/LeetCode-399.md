---
title: "LeetCode 399"
date: 2022-12-31T20:46:47+08:00
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

利用并查集的思想，有倍数关系的变量通过并查集连接起来，并且将边的权值设为边两头的结点的倍数大小，当求两个变量的倍数关系时，判断这两个结点是否连通，并且求出两个结点到根节点的权值相除即可，要特别注意路径压缩时权值的更新，详见：<https://leetcode.cn/problems/evaluate-division/solutions/548634/399-chu-fa-qiu-zhi-nan-du-zhong-deng-286-w45d/>

### 代码

```java
class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int equationSize = values.length;
        UF uf = new UF(2 * equationSize);
        int id = 0;
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < equationSize; i++) {
            String v1 = equations.get(i).get(0);
            String v2 = equations.get(i).get(1);
            if (!map.containsKey(v1)) {
                map.put(v1, id);
                id++;
            }
            if (!map.containsKey(v2)) {
                map.put(v2, id);
                id++;
            }
            uf.union(map.get(v1), map.get(v2), values[i]);
        }

        int queriesSize = queries.size();
        double[] res = new double[queriesSize];
        for (int i = 0; i < queriesSize; i++) {
            Integer id1 = map.get(queries.get(i).get(0));
            Integer id2 = map.get(queries.get(i).get(1));
            if (id1 == null || id2 == null) {
                res[i] = -1;
            } else {
                res[i] = uf.isConnected(id1, id2);
            }
        }
        return res;
    }

    class UF {
        private int[] parent;
        private double[] weight;

        public UF(int n) {
            parent = new int[n];
            weight = new double[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                weight[i] = 1;
            }
        }

        public void union(int p, int q, double value) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ) {
                return;
            }
            parent[rootP] = rootQ;
            weight[rootP] = value * weight[q] / weight[p];
        }

        public double isConnected(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP != rootQ) {
                return -1;
            } else {
                return weight[p] / weight[q];
            }
        }

        public int find(int x) {
            if (x != parent[x]) {
                int origin = parent[x];
                parent[x] = find(parent[x]);
                weight[x] *= weight[origin];
            }
            return parent[x];
        }
    }
}
```

### References

---

#### 1. [除法求值](https://leetcode.cn/problems/evaluate-division/)
