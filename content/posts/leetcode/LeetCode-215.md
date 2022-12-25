---
title: "LeetCode 215"
date: 2022-12-25T20:54:23+08:00
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

#### 最小堆

维护一个有 `K` 个元素的最小堆：

- 如果当前堆不满，直接添加；

- 堆满的时候，如果新读到的数小于等于堆顶，肯定不是我们要找的元素，只有新遍历到的数大于堆顶的时候，才将堆顶拿出，然后放入新读到的数，进而让堆自己去调整内部结构。
- 数组遍历完之后堆顶就是要找的元素

#### 快速选择

像快排一样随机确定一个中枢所在的位置，如果这个位置刚好就是要求的第k大的元素，就直接返回，否则根据中枢与target的大小关系选择是中枢左边还是右边继续随机确定一个中枢所在的位置，直到找到target，详见思想篇章

### 代码

#### 最小堆

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> queue = new PriorityQueue<>();
        for (int i = 0; i < k; i++) {
            queue.offer(nums[i]);
        }
        for (int i = k; i < nums.length; i++) {
            if (nums[i] > queue.peek()) {
                queue.poll();
                queue.offer(nums[i]);
            }
        }
        return queue.peek();
    }
}
```

#### 快速选择

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int target = nums.length - k, left = 0, right = nums.length - 1;
        while (left <= right) {
            int pivotIndex = partition(nums, left, right);
            if (pivotIndex > target) {
                right = pivotIndex - 1;
            } else if (pivotIndex < target) {
                left = pivotIndex + 1;
            } else {
                return nums[target];
            }
        }
        return -1;
    }

    private int partition(int[] nums, int left, int right) {
        int randomIndex = new Random().nextInt(right - left + 1) + left;
        swap(nums, left, randomIndex);
        int pivot = nums[left];
        while (left < right) {
            while (left < right && nums[right] >= pivot) {
                right--;
            }
            nums[left] = nums[right];
            while (left < right && nums[left] <= pivot) {
                left++;
            }
            nums[right] = nums[left];
        }
        nums[left] = pivot;
        return left;
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
```

### References

---

#### 1. [数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/)
