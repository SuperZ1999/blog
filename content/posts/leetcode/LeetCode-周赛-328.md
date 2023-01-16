---
title: "LeetCode 周赛 328"
date: 2023-01-15T22:37:46+08:00
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

#### 第一题

遍历一遍即可，直接看代码

#### 第二题

二维数组一片区域同时增加一个数，可以使用差分数组的思想，跟一维的一样，一维的是把两头修改一下就可以了，二维的需要在以下位置修改：

![image.png](https://pic.leetcode-cn.com/1641658840-YrICJa-image.png)

为什么要这么修改？因为差分数组的前缀和就是原数组，这么修改的话，差分数组求前缀和后刚好就是那一块被修改了，又因为差分数组的前缀和是原数组，所以把修改后的差分数组求前缀和后就得到了答案

所以这道题的解答有三步：

1. 构建差分数组，注意二维差分数组的构建方式：差分值=当前位置的值-左边的-上边的+左上的，本题全是0所以可以省略
2. 修改差分数组，具体做法如上所示
3. 对差分数组求前缀和，获取原数组，这里因为将前缀和数组放在一个新数组里还得复制到结果数组里面，所以可以将前缀和数组放到之前的差分数组里面，然后再复制到结果数组，以此来节省时间

#### 第三题

利用滑动窗口的思想，时刻保持当前窗口是以right为底，窗口内是好数组的最短数组，那么以当前right为底的好数组个数就是left+1个，我的代码和标准解法的区别是，我的left比标准解答往后挪了1

#### 第四题

没看

### 代码

#### 第一题

```java
class Solution {
    public int differenceOfSum(int[] nums) {
        int sum1 = 0, sum2 = 0;
        for (int num : nums) {
            sum1 += num;
            sum2 += getVal(num);
        }
        return Math.abs(sum1 - sum2);
    }

    private int getVal(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```

#### 第二题

```java
class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] diff = new int[n + 2][n + 2];
        for (int[] query : queries) {
            diff[query[0] + 1][query[1] + 1]++;
            diff[query[0] + 1][query[3] + 2]--;
            diff[query[2] + 2][query[1] + 1]--;
            diff[query[2] + 2][query[3] + 2]++;
        }
        int[][] res = new int[n][n];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                diff[i][j] = diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1] + diff[i][j];
                res[i - 1][j - 1] = diff[i][j];
            }
        }
        return res;
    }
}
```

#### 第三题

```java
class Solution {
    public long countGood(int[] nums, int k) {
        long res = 0;
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0, right = 0, count = 0;
        while (right < n) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);
            count += map.get(nums[right]) - 1;
            right++;
            while (count - map.get(nums[left]) + 1 >= k) {
                map.put(nums[left], map.get(nums[left]) - 1);
                count -= map.get(nums[left]);
                left++;
            }
            if (count >= k) {
                res += left + 1;
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [数组元素和与数字和的绝对差](https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array/)

#### 2. [子矩阵元素加 1](https://leetcode.cn/problems/increment-submatrices-by-one/)

#### 3. [统计好子数组的数目](https://leetcode.cn/problems/count-the-number-of-good-subarrays/)
