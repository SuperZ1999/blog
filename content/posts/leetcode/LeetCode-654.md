---
title: "LeetCode 654"
date: 2022-10-12T11:18:53+08:00
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

利用二叉树分解问题的思想，将原问题分解为找出root结点+构造左子树+构造右子树，找出root结点，遍历数组即可，构造左右子树递归调用即可

### 我的代码

```java
class Solution {
    private TreeNode build(int[] nums, int low, int high) {
        if (low > high) {
            return null;
        }

        int max = nums[low], index = low;
        for (int i = low + 1; i <= high; i++) {
            if (nums[i] > max) {
                max = nums[i];
                index = i;
            }
        }

        TreeNode root = new TreeNode(max);
        TreeNode left = build(nums, low, index - 1);
        TreeNode right = build(nums, index + 1, high);
        root.left = left;
        root.right = right;

        return root;
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return build(nums, 0 , nums.length - 1);
    }
}
```

### References

---

#### 1. [最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/)
