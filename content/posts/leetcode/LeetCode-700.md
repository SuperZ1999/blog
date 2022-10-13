---
title: "LeetCode 700"
date: 2022-10-13T16:06:44+08:00
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

利用二分查找的思想，不解释了

### 我的代码

```java
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) {
            return null;
        }
        if (val > root.val) {
            return searchBST(root.right, val);
        }
        if (val < root.val) {
            return searchBST(root.left, val);
        }
        return root;
    }
}
```

### References

---

#### 1. [二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/)
