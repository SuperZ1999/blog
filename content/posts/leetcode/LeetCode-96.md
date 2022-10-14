---
title: "LeetCode 96"
date: 2022-10-14T11:08:45+08:00
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

#### 递归思路

递归函数定义为n个结点可以组成几种BST，那么对于n个结点的BST的种类=将n个结点逐个当成root，左右子树的种类相乘，再把这些结果相加就是n个结点BST的种类

#### 动态规划

递归明显有重复计算的问题，我们可以对已经计算好的数据进行存储，需要时就不需要重新计算了，这种重复利用子问题的解的方式就是动态规划

### 我的代码

#### 递归

```java
class Solution {
    public int numTrees(int n) {
        if (n == 1 || n == 0) {
            return 1;
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += numTrees(i) * numTrees(n - i - 1);
        }

        return sum;
    }
}
```

#### 动态规划

```java
class Solution {
    public int numTrees(int n) {
        int[] num = new int[n + 1];
        num[0] = num[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                num[i] += num[j] * num[i - j - 1];
            }
        }
        return num[n];
    }
}
```

### References

---

#### 1. [不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/)
