---
title: "LeetCode 437"
date: 2022-12-29T22:31:28+08:00
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

#### DFS

遍历二叉树的所有结点，遍历到每个结点同时计算以此结点为头部，往下拓展有几个路径之和为target的情况，求和即可

#### 前缀和

基本思想同[LeetCode-560](https://superz1999.github.io/blog/posts/leetcode/leetcode-560/)，我们利用先序遍历二叉树，记录下根节点 root 到当前节点 p 的路径上除当前节点以外所有节点的前缀和，在已保存的路径前缀和中查找是否存在前缀和刚好等于当前节点到根节点的前缀和 curr 减去 targetSum，其实跟[LeetCode-560](https://superz1999.github.io/blog/posts/leetcode/leetcode-560/)一样，就是变成了二叉树的前缀和，而且要注意需要提前记录前缀和0，遍历完当前结点记得从map中去除当前的前缀和

### 代码

#### DFS

```java
class Solution {
    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return 0;
        }
        int res = 0;
        res += rootSum(root, targetSum);
        res += pathSum(root.left, targetSum);
        res += pathSum(root.right, targetSum);
        return res;
    }

    private int rootSum(TreeNode root, long targetSum) {
        if (root == null) {
            return 0;
        }
        int res = 0;
        if (targetSum == root.val) {
            res++;
        }
        return rootSum(root.left, targetSum - root.val)
                + rootSum(root.right, targetSum - root.val)
                + res;
    }
}
```

#### 前缀和

```java
class Solution {
    private Map<Long, Integer> preSumMap = new HashMap<>();

    public int pathSum(TreeNode root, int targetSum) {
        preSumMap.put(0L, 1);
        return dfs(root, 0, targetSum);
    }

    private int dfs(TreeNode root, long preSum, int targetSum) {
        if (root == null) {
            return 0;
        }
        preSum += root.val;
        int res = 0;
        res += preSumMap.getOrDefault(preSum - targetSum, 0);
        preSumMap.put(preSum, preSumMap.getOrDefault(preSum, 0) + 1);
        res += dfs(root.left, preSum, targetSum);
        res += dfs(root.right, preSum, targetSum);
        preSumMap.put(preSum, preSumMap.get(preSum) - 1);
        return res;
    }
}
```

### References

---

#### 1. [路径总和 III](https://leetcode.cn/problems/path-sum-iii/)
