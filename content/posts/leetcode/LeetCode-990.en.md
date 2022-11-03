---
title: "LeetCode 990"
date: 2022-11-03T23:57:29+08:00
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

利用并查集的思想，先将相等的连接起来，然后再判断不相等的是否与并查集里的连通状态冲突

### 代码

```java
class Solution {
    public boolean equationsPossible(String[] equations) {
        UF uf = new UF(26);
        for (String equation : equations) {
            if (equation.charAt(1) == '=') {
                uf.union(equation.charAt(0) - 'a', equation.charAt(3) - 'a');
            }
        }
        for (String equation : equations) {
            if (equation.charAt(1) == '!') {
                if (uf.isConnected(equation.charAt(0) - 'a', equation.charAt(3) - 'a')) {
                    return false;
                }
            }
        }
        return true;
    }

    class UF {
        private int[] parent;
        private int count;

        public UF(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
            count = n;
        }

        public int find(int x) {
            if (x != parent[x]) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int x, int y) {
            int xRoot = find(x);
            int yRoot = find(y);
            if (xRoot == yRoot) {
                return;
            }
            parent[xRoot] = yRoot;
            count--;
        }

        public boolean isConnected(int x, int y) {
            int xRoot = find(x);
            int yRoot = find(y);
            return xRoot == yRoot;
        }

        public int getCount() {
            return count;
        }
    }
}
```

### References

---

#### 1. [等式方程的可满足性](https://leetcode.cn/problems/satisfiability-of-equality-equations/)
