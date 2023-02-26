---
title: "LeetCode 101"
date: 2023-02-26T23:54:56+08:00
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

两种思路：

#### 递归

因为是判断树是否镜像对称，所以需要递归判断左子树的左子树与右子树的右子树和左子树的右子树与右子树的左子树是否镜像对称，这样就找到了递归的地方，详见代码

#### 迭代

创建一个队列，首先从队列中拿出两个节点(left 和 right)比较，将 left 的 left 节点和 right 的 right 节点放入队列，将 left 的 right 节点和 right 的 left 节点放入队列，再比较，循环往复即可

### 代码

#### 递归

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode leftRoot, TreeNode rightRoot) {
        if (leftRoot == null && rightRoot == null) {
            return true;
        }
        if (leftRoot == null || rightRoot == null) {
            return false;
        }
        if (leftRoot.val != rightRoot.val) {
            return false;
        }
        return isSymmetric(leftRoot.right, rightRoot.left) && isSymmetric(leftRoot.left, rightRoot.right);
    }
}
```

#### 迭代

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.add(root.left);
        queue.add(root.right);
        while (!queue.isEmpty()) {
            TreeNode left = queue.remove();
            TreeNode right = queue.remove();
            if (left == null && right == null) {
                continue;
            }
            if (left == null || right == null) {
                return false;
            }
            if (left.val != right.val) {
                return false;
            }
            queue.add(left.left);
            queue.add(right.right);
            queue.add(left.right);
            queue.add(right.left);
        }
        return true;
    }
}
```

### References

---

#### 1. [对称二叉树](https://leetcode.cn/problems/symmetric-tree/)
