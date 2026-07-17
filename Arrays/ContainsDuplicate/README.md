# 217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/

## Brute Force
Time: O(n²) | Space: O(1)
Compare every pair of elements.

## Hash Set (optimal)
Time: O(n) | Space: O(n)
Track seen elements in a set. Membership check is O(1) on average,
so one pass through the array is enough.

## Sorting
Time: O(n log n) | Space: O(1)
Sort the array, then check adjacent elements for equality.
Trades time for lower memory usage compared to the hash set approach.