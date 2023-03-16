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

#### 手写堆

由于面试不让用Java的优先队列，所以需要手写堆，核心思想就三个：

- 建堆：从从右往左的第一个非叶子结点开始下沉，遍历到根节点，堆就建好了
- 下沉：从子结点里选择一个较小（大）的，跟父节点比较，如果父节点需要下沉就交换两者的位置，然后继续这个过程
- 上浮：当前结点跟父节点比较，如果当前节点需要上浮就交换两者的位置，然后继续这个过程

注意点：

- 设根节点的编号从1开始（不是从0开始，这样方便一些），这样的话父节点就是root/2，左孩子就是root\*2，右孩子就是root\*2+1，第一个非叶子结点就是size/2，size为堆的结点个数，也是结点最大的编号

分为有类版和无类版

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

#### 手写堆

##### 有类版

```java
class Solution {
    // 手写堆
    public int findKthLargest(int[] nums, int k) {
        MinPQ pq = new MinPQ(k);
        for (int i = 0; i < k; i++) {
            pq.insert(nums[i]);
        }
        for (int i = k; i < nums.length; i++) {
            if (nums[i] > pq.min()) {
                pq.delMin();
                pq.insert(nums[i]);
            }
        }
        return pq.delMin();
    }

    class MinPQ {
        private int[] nums;
        private int size = 0;
        private int capacity;

        public MinPQ(int capacity) {
            this.capacity = capacity;
            nums = new int[capacity + 1];
        }

        public boolean isEmpty() {
            return size == 0;
        }

        public boolean isFull() {
            return size == capacity;
        }

        public int min() {
            return nums[1];
        }

        private int parent(int root) {
            return root / 2;
        }

        private int left(int root) {
            return root * 2;
        }

        private int right(int root) {
            return root * 2 + 1;
        }

        private void swap(int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }

        public void insert(int num) {
            size++;
            nums[size] = num;
            swim(size);
        }

        public int delMin() {
            int max = nums[1];
            nums[1] = nums[size];
            size--;
            sink(1);
            return max;
        }

        private void swim(int x) {
            while (x > 1 && nums[x] < nums[parent(x)]) {
                swap(x, parent(x));
                x = parent(x);
            }
        }

        private void sink(int x) {
            while (left(x) <= size) {
                int min = left(x);
                if (right(x) <= size && nums[right(x)] < nums[min]) {
                    min = right(x);
                }
                if (nums[x] < nums[min]) {
                    break;
                }
                swap(x, min);
                x = min;
            }
        }
    }
}
```

##### 无类版

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int[] heap = new int[k + 1];
        for (int i = 0; i < k; i++) {
            heap[i + 1] = nums[i];
        }
        buildHeap(heap);
        for (int i = k; i < nums.length; i++) {
            if (nums[i] > heap[1]) {
                heap[1] = nums[i];
                sink(heap, 1);
            }
        }
        return heap[1];
    }

    private void buildHeap(int[] heap) {
        int size = heap.length - 1;
        for (int i = size / 2; i >= 1; i--) {
            sink(heap, i);
        }
    }

    private void sink(int[] heap, int x) {
        int size = heap.length - 1;
        while (x * 2 <= size) {
            int min = x * 2;
            if (x * 2 + 1 <= size && heap[x * 2 + 1] < heap[min]) {
                min = x * 2 + 1;
            }
            if (heap[x] < heap[min]) {
                break;
            }
            swap(heap, x, min);
            x = min;
        }
    }

    private void swap(int[] heap, int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }
}
```

### References

---

#### 1. [数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/)
