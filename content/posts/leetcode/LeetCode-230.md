---
title: "LeetCode 230"
date: 2022-10-13T14:07:42+08:00
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

BST的中序遍历就是升序序列，所以先中序遍历，然后找第k大的就行了，但是可以优化一下，找到第k大的就直接return

### 我的代码

```java
class Solution {
    private int rank = 0;

    public int kthSmallest(TreeNode root, int k) {
        if (root == null) {
            return 0;
        }
        int res;
        if ((res = kthSmallest(root.left, k)) != 0) {
            return res;
        }
        rank++;
        if (rank == k) {
            return root.val;
        }
        return kthSmallest(root.right, k);
    }
}
```

### References

---

#### 1. [二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)
