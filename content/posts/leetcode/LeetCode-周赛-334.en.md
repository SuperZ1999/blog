---
title: "LeetCode 周赛 334"
date: 2023-02-26T23:00:13+08:00
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

模拟即可，直接看代码

#### 第二题

从左往右遍历字符串，每碰到一个数字，就计算前面mod m的余数 * 10 + 当前数字是否能整除m，然后再将除以m的余数赋值到前面mod m的余数上，看代码即可

#### 第三题

两种思路：

##### 二分查找

由于是查找能标记的最大值，由于标记数和不能成立成正比，具有单调性，所以可以使用二分查找，范围是[0, nums.lenght / 2]，每次选择中点，并判断中点能不能成立，具体判断方法就是判断最小的mid个数和最大的mid个数能否满足2*nums[i] <= nums[j]

##### 双指针

利用双指针的思想，i指向0， j指向中点，判断i 和 j是否满足条件，如果满足条件，i++，寻找下一个标记对，最后i的值就是可标记对的数目

#### 第四题

没做出来

### 代码

#### 第一题

```java
class Solution {
    public int[] leftRigthDifference(int[] nums) {
        int n = nums.length;
        int[] res = new int[n], leftSum = new int[n], rightSum = new int[n];
        for (int i = 1; i < n; i++) {
            leftSum[i] = leftSum[i - 1] + nums[i - 1];
        }
        for (int i = n - 2; i >= 0; i--) {
            rightSum[i] = rightSum[i + 1] + nums[i + 1];
        }
        for (int i = 0; i < n; i++) {
            res[i] = Math.abs(leftSum[i] - rightSum[i]);
        }
        return res;
    }
}
```

#### 第二题

```java
class Solution {
    public int[] divisibilityArray(String word, int m) {
        int n = word.length();
        int[] res = new int[n];
        long r = 0;
        for (int i = 0; i < n; i++) {
            char c = word.charAt(i);
            r = r * 10 + c - '0';
            if (r % m == 0) {
                res[i] = 1;
            }
            r %= m;
        }
        return res;
    }
}
```

#### 第三题

##### 二分查找

```java
class Solution {
    public int maxNumOfMarkedIndices(int[] nums) {
        int n = nums.length;
        int left = 0, right = n / 2;
        Arrays.sort(nums);
        while (left < right) {
            int mid = (right - left + 1) / 2 + left;
            if (canMark(nums, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left * 2;
    }
    
    private boolean canMark(int[] nums, int n) {
        for (int i = 0; i < n; i++) {
            if (2 * nums[i] > nums[nums.length - n + i]) {
                return false;
            }
        }
        return true;
    }
}
```

##### 双指针

```java
class Solution {
    public int maxNumOfMarkedIndices(int[] nums) {
        Arrays.sort(nums);
        int i = 0;
        for (int j = (nums.length + 1) / 2;j < nums.length;j++) {
            if (2 * nums[i] <= nums[j]) {
                i++;
            }
        }
        return 2 * i;
    }
}
```

### References

---

#### 1. [左右元素和的差值](https://leetcode.cn/problems/left-and-right-sum-differences/)

#### 2. [找出字符串的可整除数组](https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/)

#### 3. [求出最多标记下标](https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/)

#### 4. [在网格图中访问一个格子的最少时间](https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/)
