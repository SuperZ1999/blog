---
title: "LeetCode 236"
date: 2022-10-22T22:47:12+08:00
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

使用二叉树遍历的思想，遍历每一个节点，当左子树找到了q或p，右子树也找到了的话，该节点就是LCA，直接返回即可，注意返回值只有可能是p或q或qp的LCA

明确函数的定义，这个函数的定义就是如果在root的树中只找到了p就返回p，只找到了q就返回q，两个都找到了就返回公共祖先，都没找到就返回null

### 代码

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        }
        if (root == p || root == q) {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) {
            return root;
        }
        return left != null ? left : right;
    }
}
```

### References

---

#### 1. [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)
