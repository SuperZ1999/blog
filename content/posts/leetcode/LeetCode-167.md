---
title: "LeetCode 167"
date: 2022-09-24T14:58:51+08:00
tags: ["leetcode"]
draft: false
---

### 思路

利用左右指针的思想，从两边向中间逼近，如果左右之和太大，那就right--，否则left++，直到左右之和等于target。

### 我的代码

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum > target) {
                right--;
            } else if (sum < target) {
                left++;
            } else {
                return new int[]{left + 1, right + 1};
            }
        }

        return new int[]{0, 0};
    }
}
```

### References

---

#### 1. [两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)
