---
title: "LeetCode 287"
date: 2022-12-26T16:39:16+08:00
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

#### 原地哈希

将元素和索引一一对应，不对应的交换元素使其对应，当碰到对应索引已经有相应的元素时，就找到了重复的元素

#### 快慢指针

将索引对应的元素当成下一个索引，按照这个逻辑把数组转换为链表，由于肯定存在重复元素，所以肯定会有多对一的映射，所以该链表一定会有环，那么这个问题就转换为了存在环的链表中寻找环起点，利用快慢指针的思想并且稍做分析，即可得出结论：当快慢指针相遇时，让其中任一个指针指向头节点，然后让它俩以相同速度前进，再次相遇时所在的节点位置就是环开始的位置，直接返回即可，详见：<https://leetcode.cn/problems/find-the-duplicate-number/solutions/58841/287xun-zhao-zhong-fu-shu-by-kirsche/>

#### 二分查找

可以在1-n中取中点mid，遍历一边nums，如果小于等于mid的元素>mid说明重复元素一定在mid的左边，然后二分查找即可，这样比1-n一个一个查找要快，因为一次可以排除一半

#### 二进制

没看，感觉没什么卵用

### 代码

#### 原地哈希

```java
class Solution {
    public int findDuplicate(int[] nums) {
        int n = nums.length, i = 0;
        while (i < n) {
            if (nums[i] == i + 1) {
                i++;
                continue;
            }
            if (nums[nums[i] - 1] == nums[i]) {
                return nums[i];
            }
            swap(nums, i, nums[i] - 1);
        }
        return -1;
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
```

#### 快慢指针

```java
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0, fast = 0;
        slow = nums[slow];
        fast = nums[nums[fast]];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        fast = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}
```

#### 二分查找

```java
class Solution {
    public int findDuplicate(int[] nums) {
        int left = 1, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            for (int num : nums) {
                if (num <= mid) {
                    count++;
                }
            }
            if (count > mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

### References

---

#### 1. [寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)
