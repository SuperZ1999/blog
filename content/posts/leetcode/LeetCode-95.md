---
title: "LeetCode 95"
date: 2022-10-14T11:32:09+08:00
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

类似LeetCode 96，利用分解问题的思想，将原问题分解为：构造root+构造左子树+构造右子树即可，但是注意root不能重复利用

### 我的代码

```java
class Solution {
    private List<TreeNode> generateTrees(int min, int max) {
        List<TreeNode> res = new ArrayList<>();
        if (min > max) {
            res.add(null);
            return res;
        }

        for (int i = min; i <= max; i++) {
            List<TreeNode> leftList = generateTrees(min, i - 1);
            List<TreeNode> rightList = generateTrees(i + 1, max);
            for (TreeNode leftNode : leftList) {
                for (TreeNode rightNode : rightList) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftNode;
                    root.right = rightNode;
                    res.add(root);
                }
            }
        }

        return res;
    }

    public List<TreeNode> generateTrees(int n) {
        return generateTrees(1, n);
    }
}
```

### References

---

#### 1. [不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/)
