---
title: "LeetCode 周赛 330"
date: 2023-01-29T15:36:14+08:00
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

脑筋急转弯，直接看代码

#### 第二题

其实就是计算2^n - 2，用快速幂计算即可，只不过要注意：

- 求的时候同时取余，模板在思想篇章
- 计算过程有可能超过int类型范围，所以需要用long存储
- 最后的结果最好写成(2^n - 2 + MOD) % MOD，因为有可能2^n - 2 < 0

#### 第三题

先转换问题，可以把原问题转换为用挡板将数组分成k个子数组，那么共有k - 1个挡板，答案就是数组第一个元素加最后一个元素加挡板两边的元素，所以可以把原数组的元素两两合并，然后找出最大的k-1个数之和与最小的k-1个数之和，两数之差就是答案

#### 第四题

其实枚举所有四元组就可以了，但是枚举所有四元组，时间复杂度较高，所以可以使用有技巧的枚举，只枚举中间两个数，剩下两个数其实大小范围和位置范围是确定的，问题就转换为了怎么获取这些位置范围和大小范围确定的数，可以用一个数组greater\[j\]\[x\]来记录位置j右边比x大的数的数量，具体看代码

### 代码

#### 第一题

```java
class Solution {
    public int distinctIntegers(int n) {
        if (n == 1) {
            return 1;
        }
        return n - 1;
    }
}
```

#### 第二题

```java
class Solution {
    int base = 1000000007;

    int mypow(int a, int k) {
        if (k == 0) return 1;
        a %= base;

        if (k % 2 == 1) {
            // k 是奇数
            return (int) (((long)a * mypow(a, k - 1)) % base);
        } else {
            // k 是偶数
            int sub = mypow(a, k / 2);
            return (int) (((long)sub * sub) % base);
        }
    }

    public int monkeyMove(int n) {
        int res = mypow(2, n);
        return res >= 2 ? res - 2 : res + base - 2;
    }
}
```

#### 第三题

```java
class Solution {
    public long putMarbles(int[] weights, int k) {
        int n = weights.length;
        long[] temp = new long[n - 1];
        for (int i = 0; i < n - 1; i++) {
            temp[i] = weights[i] + weights[i + 1];
        }
        Arrays.sort(temp);
        long max = 0, min = 0;
        for (int i = 0; i < k - 1; i++) {
            max += temp[n - 2 - i];
            min += temp[i];
        }
        return max - min;
    }
}
```

#### 第四题

```java
class Solution {
    public long countQuadruplets(int[] nums) {
        int n = nums.length;
        int[][] greater = new int[n][n + 1];
        for (int i = n - 2; i > 0; i--) {
            greater[i] = greater[i + 1].clone();
            for (int j = 1; j < nums[i + 1]; j++) {
                greater[i][j]++;
            }
        }

        long res = 0;
        for (int j = 1; j < n - 2; j++) {
            for (int k = j + 1; k < n - 1; k++) {
                int x = nums[k];
                if (nums[j] > x) {
                    res += (long) greater[k][nums[j]] * (x - (n - 1 - j - greater[j][x]));
                }
            }
        }
        return res;
    }
}
```

### References

---

#### 1. [统计桌面上的不同数字](https://leetcode.cn/problems/count-distinct-numbers-on-board/)

#### 2. [猴子碰撞的方法数](https://leetcode.cn/problems/count-collisions-of-monkeys-on-a-polygon/)

#### 3. [将珠子放入背包中](https://leetcode.cn/problems/put-marbles-in-bags/)

#### 4. [统计上升四元组](https://leetcode.cn/problems/count-increasing-quadruplets/)
