---
title: "LeetCode 周赛-312"
date: 2022-09-25T15:22:34+08:00
tags: ["leetcode"]
draft: false
---

### 思路

#### 第一题

排序，不解释

#### 第二题

按位与只会越与越小，那既然要找最大的结果，那遍历一遍数组统计一下最大的数出现了几次就可以了

#### 第三题

暴力会超时，利用动态规划的思想，从左往右遍历一遍找各元素左边递减的元素个数，从右往左遍历一遍找各元素右边递增的元素个数，然后和k比较就可以了

### 我的代码

#### 第一题

```java
class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        People[] peoples = new People[names.length];
        for(int i = 0; i < peoples.length; i++) {
            peoples[i] = new People(names[i], heights[i]);
        }

        Arrays.sort(peoples, (a, b) -> b.height - a.height);

        for (int i = 0; i < peoples.length; i++) {
            names[i] = peoples[i].name;
        }

        return names;
    }

    static class People {
        String name;
        int height;

        public People(String name, int height) {
            this.name = name;
            this.height = height;
        }
    }
}
```

#### 第二题

```java
class Solution {
    public int longestSubarray(int[] nums) {
        int max = Integer.MIN_VALUE, ans = 0, count = 0;
        for (int num : nums) {
            if (num != max) {
                count = 0;
                if (num > max) {
                    max = num;
                    ans = 0;
                }
            }
            if (num == max) {
                count++;
            }
            if (count > ans) {
                ans = count;
            }
        }
        return ans;
    }
}
```

#### 第三题

动态规划：

```java
class Solution {
    public List<Integer> goodIndices(int[] nums, int k) {
        int[] decre = new int[nums.length];
        decre[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                decre[i] = decre[i - 1] + 1;
            } else {
                decre[i] = 1;
            }
        }
        int[] incre = new int[nums.length];
        incre[nums.length - 1] = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) {
                incre[i] = incre[i + 1] + 1;
            } else {
                incre[i] = 1;
            }
        }

        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = k; i < nums.length - k; i++) {
            if (decre[i - 1] >= k && incre[i+1] >= k) {
                ans.add(i);
            }
        }

        return ans;
    }
}
```

暴力解法：

```java
class Solution {
    private boolean isGoodIndex(int[] nums, int index, int k) {
        for (int i = index - 1; i > index - k; i--) {
            if (nums[i] > nums[i - 1]) {
                return false;
            }
        }
        for (int i = index + 1; i < index + k; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }

    public List<Integer> goodIndices(int[] nums, int k) {
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = k; i < nums.length - k; i++) {
            if (isGoodIndex(nums, i, k)) {
                ans.add(i);
            }
        }
        return ans;
    }
}
```

### References

---

#### 1. [按身高排序](https://leetcode.cn/problems/sort-the-people/)

#### 2. [按位与最大的最长子数组](https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and/)

#### 3. [找到所有好下标](https://leetcode.cn/problems/find-all-good-indices/)
