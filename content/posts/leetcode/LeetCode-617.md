---
title: "LeetCode 617"
date: 2022-12-27T21:48:18+08:00
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

#### 递归（DFS）

直接看代码

#### 迭代（BFS）

构建三个队列，分别存放需要合并子结点的合并后的结点、相应的第一颗树的结点、相应的第二颗树的结点，然后每次从三个队列里各取一个，然后看看应该怎么合并他们的子结点，详见：<https://leetcode.cn/problems/merge-two-binary-trees/solutions/424201/he-bing-er-cha-shu-by-leetcode-solution/>

### 代码

#### 递归（DFS）

```java
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return null;
        }

        if (root1 != null && root2 != null) {
            root1.val = root1.val + root2.val;
            root1.left = mergeTrees(root1.left, root2.left);
            root1.right = mergeTrees(root1.right, root2.right);
            return root1;
        }

        return root1 != null ? root1 : root2;
    }
}
```

#### 迭代（BFS）

```java
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null) {
            return root2;
        }
        if (root2 == null) {
            return root1;
        }
        TreeNode root = new TreeNode(root1.val + root2.val);
        Queue<TreeNode> queue = new LinkedList<>();
        Queue<TreeNode> queue1 = new LinkedList<>();
        Queue<TreeNode> queue2 = new LinkedList<>();
        queue.offer(root);queue1.offer(root1);queue2.offer(root2);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll(), node1 = queue1.poll(), node2 = queue2.poll();
            TreeNode left1 = node1.left, left2 = node2.left, right1 = node1.right, right2 = node2.right;
            if (left1 != null || left2 != null) {
                if (left1 != null && left2 != null) {
                    TreeNode left = new TreeNode(left1.val + left2.val);
                    node.left = left;
                    queue.offer(left);
                    queue1.offer(left1);
                    queue2.offer(left2);
                } else {
                    node.left = left1 != null ? left1 : left2;
                }
            }
            if (right1 != null || right2 != null) {
                if (right1 != null && right2 != null) {
                    TreeNode right = new TreeNode(right1.val + right2.val);
                    node.right = right;
                    queue.offer(right);
                    queue1.offer(right1);
                    queue2.offer(right2);
                } else {
                    node.right = right1 != null ? right1 : right2;
                }
            }
        }
        return root;
    }
}
```

### References

---

#### 1. [合并二叉树](https://leetcode.cn/problems/merge-two-binary-trees/)
