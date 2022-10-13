---
title: "LeetCode 543"
date: 2022-10-10T14:53:44+08:00
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

直径等于左子树的深度加右子树的深度，那么遍历一遍树，找出直径里的最大值即可，不过需要注意，因为要获得每个节点子树的深度，需要用后序遍历，因为只有后序遍历能获得左右子树的信息。

### 代码

```java
class Solution {
    int maxDiameter = 0;

    private int maxDeep(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftDeep = maxDeep(root.left);
        int rightDeep = maxDeep(root.right);
        maxDiameter = Math.max(maxDiameter, leftDeep + rightDeep);

        return Math.max(leftDeep, rightDeep) + 1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        maxDeep(root);
        return maxDiameter;
    }
}
```

### References

---

#### 1. [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)
