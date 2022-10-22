---
title: "LeetCode 235"
date: 2022-10-22T23:19:23+08:00
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

跟236类似，只不过不需要一个一个遍历，因为是BST，可以根据结点的大小选择去左子树还是右子树，第一个在val1和val2之间的结点就是LCA

### 代码

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int val1 = Math.min(p.val, q.val);
        int val2 = Math.max(p.val, q.val);
        return find(root, val1, val2);
    }

    private TreeNode find(TreeNode root, int val1, int val2) {
        if (root == null) {
            return null;
        }
        if (root.val > val2) {
            return find(root.left, val1, val2);
        }
        if (root.val < val1) {
            return find(root.right, val1, val2);
        }
        return root;
    }
}
```

### References

---

#### 1. [二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)
