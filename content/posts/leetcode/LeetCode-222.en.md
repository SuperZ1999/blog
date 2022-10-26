---
title: "LeetCode 222"
date: 2022-10-26T22:38:25+08:00
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

普通二叉树需要对二叉树进行遍历才能统计结点个数，满二叉树只需要知道树的高度就可以计算出来，那么完全二叉树可以结合这两个的做法，如果左边和右边高度相同，就用满二叉树的计算方式，如果不同那就遍历二叉树，同时判断该节点为root的树是不是满二叉树

这种做法时间复杂度是O(logn*logn)，详见：<https://labuladong.gitee.io/algo/2/21/48/>

### 代码

```java
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        TreeNode left = root, right = root;
        int lh = 0, rh = 0;
        while (left != null) {
            left = left.left;
            lh++;
        }
        while (right != null) {
            right = right.right;
            rh++;
        }
        if (lh == rh) {
            return (int) (Math.pow(2, lh) - 1);
        }

        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
```

### References

---

#### 1. [完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/)
