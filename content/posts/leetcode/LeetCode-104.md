---
title: "LeetCode 104"
date: 2022-10-10T14:25:10+08:00
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

有两种思路，分别是**分解问题**和**遍历二叉树**

#### 思路一

把当前问题分解为左子树和右子树中深度较大的那个子树的深度+1，就是当前树的深度

#### 思路二

把二叉树遍历一遍，同时用一个外部变量记录最大的深度，注意需要在前序位置deep++，后序位置deep--

### 我的代码

#### 思路一

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```

#### 思路二

```java
class Solution {
    int res = 0, deep = 0;
    private void traverse(TreeNode root) {
        if (root == null) {
            return;
        }

        deep++;
        if (root.left == null && root.right == null) {
            res = Math.max(res, deep);
        }
        traverse(root.left);
        traverse(root.right);
        deep--;
    }
    public int maxDepth(TreeNode root) {
        traverse(root);
        return res;
    }
}
```

### References

---

#### 1. [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)
