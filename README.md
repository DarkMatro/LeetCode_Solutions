# LeetCode Solutions
Solved problems from leetcode. Python

![Progress](https://img.shields.io/badge/progress-125%20%2F%203031-ff69b4.svg)&nbsp;

## Algorithms

* [Array (75/1550)](https://github.com/DarkMatro/LeetCode_Solutions#array)
* [Hash Table (16/515)](https://github.com/DarkMatro/LeetCode_Solutions#hash-table)
* [Binary Search (5/252)](https://github.com/DarkMatro/LeetCode_Solutions#Binary-Search)
* [Math (14/479)](https://github.com/DarkMatro/LeetCode_Solutions#math)
* [Bit Manipulation (8/189)](https://github.com/DarkMatro/LeetCode_Solutions#bit_manipulation)
* [String (20/667)](https://github.com/DarkMatro/LeetCode_Solutions#string)
* [Linked List (7/73)](https://github.com/DarkMatro/LeetCode_Solutions#linked-list)
* [Two Pointers (14/191)](https://github.com/DarkMatro/LeetCode_Solutions#two-pointers)
* [Tree (5/224)](https://github.com/DarkMatro/LeetCode_Solutions#tree)
* [Database (16/247)](https://github.com/DarkMatro/LeetCode_Solutions#database)


## Array
|  #  | Title                                                                                                                                              | Solution                                                                   | Time | Memory | Difficulty | Tag                                                             |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------|--------|------------|-----------------------------------------------------------------|
0001 | [Two Sum](https://leetcode.com/problems/two-sum)                                                                                                   | [###](./Array/Two-Sum.py)                                                  | O(N) | O(N)   | Easy       | Array, Hash Table                                               |
0026 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)                                           | [###](./Array/Remove-Duplicates-from-Sorted-Array.py)                      | O(N) | O(1)   | Easy       | Array, Two Pointers                                             |
0027 | [Remove Element](https://leetcode.com/problems/remove-element)                                                                                     | [###](./Array/Remove-Element.py)                                           | O(N) | O(1)   | Easy       | Array, Two Pointers                                             |
0066 | [Plus One](https://leetcode.com/problems/plus-one)                                                                                                 | [###](./Array/Plus-One.py)                                                 | O(N) | O(N)   | Easy       | Array, Math                                                     |
0088 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)                                                                             | [###](./Array/Merge-Sorted-Array.py)                                       | O(m+n) | O(1)   | Easy       | Array, Two Pointers, Sorting                                    |
0118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle)                                                                                | [###](./Array/Pascal's-Triangle.py)                                        | O(N^2) | O(1)   | Easy       | Array, Dynamic Programming                                      |
0121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)                                                   | [###](./Array/Best-Time-to-Buy-and-Sell-Stock.py)                          | O(N) | O(1)   | Easy       | Array, Dynamic Programming                                      |
0136 | [Single Number](https://leetcode.com/problems/single-number)                                                                                       | [###](./Array/Single-Number.py)                                            | O(N) | O(1)   | Easy       | Array, Bit Manipulation                                         |
0169 | [Majority Element](https://leetcode.com/problems/majority-element)                                                                                 | [###](./Array/Majority-Element.py)                                         | O(N) | O(1)   | Easy       | Array, Hash Table, Divide and Conquer, Sorting, Counting        |
0217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate)                                                                             | [###](./Array/Contains-Duplicate.py)                                       | O(N) | O(N)   | Easy       | Array, Hash Table, Sorting                                      |
0228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges)                                                                                     | [###](./Array/Summary-Ranges.py)                                           | O(N) | O(1)   | Easy       | Array                                      |
0268 | [Missing Number](https://leetcode.com/problems/missing-number)                                                                                     | [###](./Array/Missing-Number.py)                                           | O(N) | O(N)   | Easy       | Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting |
0283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes)                                                                                           | [###](./Array/Move-Zeroes.py)                                              | O(N) | O(1)   | Easy       | Array, Two Pointers                                             |
0350 | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii)                                                       | [###](./Array/Intersection-of-Two-Arrays-II.py)                            | O(N) | O(N)   | Easy       | Array, Hash Table, Two Pointers, Binary Search, Sorting         |
0485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones)                                                                         | [###](./Array/Max-Consecutive-Ones.py)                                     | O(N) | O(1)   | Easy       | Array                                                           |
0674 | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence)                               | [###](./Array/Longest-Continuous-Increasing-Subsequence.py)                | O(N) | O(1)   | Easy       | Array                                                           |
0717 | [1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters)                                                             | [###](./Array/1-bit-and-2-bit-Characters.py)                               | O(N) | O(1)   | Easy       | Array                                                           |
0849 | [Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person)                                                             | [###](./Array/Maximize-Distance-to-Closest-Person.py)                               | O(N) | O(1)   | Medium     | Array                                                           |
0896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array)                                                                                   | [###](./Array/Monotonic-Array.py)                                          | O(N) | O(1)   | Easy       | Array                                                           |
0915 | [Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals)                                                                                   | [###](./Array/Partition-Array-into-Disjoint-Intervals.py)                                          | O(N) | O(1)   | Medium     | Array                                                           |
0941 | [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array)                                                                         | [###](./Array/Valid-Mountain-Array.py)                                     | O(N) | O(1)   | Easy       | Array                                                           |
1018 | [Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5)                                                         | [###](./Array/Binary-Prefix-Divisible-By-5.py)                             | O(N) | O(1)   | Easy       | Array                                                           |
1184 | [Monotonic Array](https://leetcode.com/problems/distance-between-bus-stops)                                                                        | [###](./Array/Distance-Between-Bus-Stops.py)                               | O(N) | O(1)   | Easy       | Array                                                           |
1287 | [Element Appearing More Than 25% In Sorted Array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array)                    | [###](./Array/Element-Appearing-More-Than-25%-In-Sorted-Array.py)          | O(logN) | O(1)   | Easy       | Array                                                           |
1295 | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits)                                   | [###](./Array/Find-Numbers-with-Even-Number-of-Digits.py)                  | O(N) | O(1)   | Easy       | Array                                                           |
1299 | [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side)         | [###](./Array/Replace-Elements-with-Greatest-Element-on-Right-Side.py)     | O(N) | O(1)   | Easy       | Array                                                           |
1313 | [Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list)                                             | [###](./Array/Decompress-Run-Length-Encoded-List.py)                       | O(N) | O(1)   | Easy       | Array                                                           |
1365 | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number)         | [###](./Array/How-Many-Numbers-Are-Smaller-Than-the-Current-Number.py)     | O(NlogN) | O(N)   | Easy       | Array, Hash Table, Sorting, Counting                            |
1375 | [Number of Times Binary String Is Prefix-Aligned](https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/)                  | [###](./Array/Number-of-Times-Binary-String-Is-Prefix-Aligned.py)          | O(N) | O(1)   | Medium     | Array                           |
1389 | [Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order)                                     | [###](./Array/Create-Target-Array-in-the-Given-Order.py)                   | O(N^2) | O(1)   | Easy       | Array, Simulation                                               |
1431 | [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies)                                 | [###](./Array/Kids-With-the-Greatest-Number-of-Candies.py)                 | O(N) | O(1)   | Easy       | Array                                                           |
1437 | [Check If All 1's Are at Least Length K Places Away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away)              | [###](./Array/Check-If-All-1's-Are-at-Least-Length-K-Places-Away.py)       | O(N) | O(1)   | Easy       | Array                                                           |
1450 | [Number of Students Doing Homework at a Given Time](https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time)               | [###](./Array/Number-of-Students-Doing-Homework-at-a-Given-Time.py)        | O(N) | O(1)   | Easy       | Array                                                           |
1470 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array)                                                                               | [###](./Array/Shuffle-the-Array.py)                                        | O(N) | O(1)   | Easy       | Array                                                           |
1480 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array)                                                                   | [###](./Array/Running-Sum-of-1d-Array.py)                                  | O(N) | O(1)   | Easy       | Array, Prefix Sum                                               |
1512 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs)                                                                         | [###](./Array/Number-of-Good-Pairs.py)                                     | O(N^2) | O(1)   | Easy       | Array, Hash Table, Math, Counting                               |
1528 | [Shuffle String](https://leetcode.com/problems/shuffle-string)                                                                                     | [###](./Array/Shuffle-String.py)                                           | O(N) | O(1)   | Easy       | Array, String                                                   |
1550 | [Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds)                                                                     | [###](./Array/Three-Consecutive-Odds.py)                                   | O(N) | O(1)   | Easy       | Array                                                           |
1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth)                                                                   | [###](./Array/Richest-Customer-Wealth.py)                                  | O(M * N) | O(1)   | Easy       | Array, Matrix                                                   |
1725 | [Number Of Rectangles That Can Form The Largest Square](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square)       | [###](./Array/Number-Of-Rectangles-That-Can-Form-The-Largest-Square.py)    | O(N) | O(N)   | Easy       | Array                                                           |
1752 | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated)                                         | [###](./Array/Check-if-Array-Is-Sorted-and-Rotated.py)                     | O(N) | O(1)   | Easy       | Array                                                           |
1779 | [Find Nearest Point That Has the Same X or Y Coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate)     | [###](./Array/Find-Nearest-Point-That-Has-the-Same-X-or-Y-Coordinate.py)   | O(N) | O(1)   | Easy       | Array                                                           |
1800 | [Maximum Ascending Subarray Sum](https://leetcode.com/problems/maximum-ascending-subarray-sum)                                                     | [###](./Array/Maximum-Ascending-Subarray-Sum.py)                           | O(N) | O(1)   | Easy       | Array                                                           |
1848 | [Minimum Distance to the Target Element](https://leetcode.com/problems/minimum-distance-to-the-target-element)                                     | [###](./Array/Minimum-Distance-to-the-Target-Element.py)                   | O(N) | O(1)   | Easy       | Array                                                           |
1909 | [Remove One Element to Make the Array Strictly Increasing](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing) | [###](./Array/Remove-One-Element-to-Make-the-Array-Strictly-Increasing.py) | O(N) | O(1)   | Easy       | Array                                                           |
1920 | [Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation)                                                         | [###](./Array/Build-Array-from-Permutation.py)                             | O(N) | O(1)   | Easy       | Array, Simulation                                               |
1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array)                                                                     | [###](./Array/Concatenation-of-Array.py)                                   | O(N) | O(N)   | Easy       | Array, Simulation                                               |
2011 | [Final Value of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations)           | [###](./Array/Final-Value-of-Variable-After-Performing-Operations.py)      | O(N) | O(1)   | Easy       | Array, String, Simulation                                       |
2016 | [Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements)                     | [###](./Array/Maximum-Difference-Between-Increasing-Elements.py)           | O(N) | O(1)   | Easy       | Array (Variant of 0121)                                         |
2057 | [Smallest Index With Equal Value](https://leetcode.com/problems/smallest-index-with-equal-value)                                                   | [###](./Array/Smallest-Index-With-Equal-Value.py)                          | O(N) | O(1)   | Easy       | Array                                                           |
2114 | [Maximum Number of Words Found in Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences)                             | [###](./Array/Maximum-Number-of-Words-Found-in-Sentences.py)               | O(N) | O(1)   | Easy       | Array, String, Simulation                                       |
2155 | [All Divisions With the Highest Score of a Binary Array](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array)     | [###](./Array/All-Divisions-With-the-Highest-Score-of-a-Binary-Array.py)   | O(N) | O(1)   | Medium     | Array                                     |
2176 | [Count Equal and Divisible Pairs in an Array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array)                           | [###](./Array/Count-Equal-and-Divisible-Pairs-in-an-Array.py)              | O(N) | O(N)   | Easy       | Array                                                           |
2210 | [Count Hills and Valleys in an Array](https://leetcode.com/problems/count-hills-and-valleys-in-an-array)                                           | [###](./Array/Count-Hills-and-Valleys-in-an-Array.py)                      | O(N) | O(1)   | Easy       | Array                                                           |
2239 | [Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero)                                                           | [###](./Array/Find-Closest-Number-to-Zero.py)                              | O(N) | O(1)   | Easy       | Array                                                           |
2432 | [The Employee That Worked on the Longest Task](https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task)                         | [###](./Array/The-Employee-That-Worked-on-the-Longest-Task.py)             | O(N) | O(1)   | Easy       | Array                                                           |
2574 | [Left and Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences)                                                     | [###](./Array/Left-and-Right-Sum-Differences.py)                           | O(N) | O(N)   | Easy       | Array, Prefix Sum                                               |
2644 | [Find the Maximum Divisibility Score](https://leetcode.com/problems/find-the-maximum-divisibility-score)                                           | [###](./Array/Find-the-Maximum-Divisibility-Score.py)                      | O(N * D) | O(N)   | Easy       | Array                                               |
2672 | [Number of Adjacent Elements With the Same Color](https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color)                   | [###](./Array/Number-of-Adjacent-Elements-With-the-Same-Color.py)          | O(N | O(N)   | Medium     | Array                                               |
2798 | [Number of Employees Who Met the Target](https://leetcode.com/problems/number-of-employees-who-met-the-target)                                     | [###](./Array/Number-of-Employees-Who-Met-the-Target.py)                   | O(N) | O(1)   | Easy       | Array                                                           |
2824 | [Count Pairs Whose Sum is Less than Target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target)                               | [###](./Array/Count-Pairs-Whose-Sum-is-Less-than-Target.py)                | O(NlogN) | O(1)   | Easy       | Array, Two Pointers, Binary Search, Sorting                     |
2855 | [Minimum Right Shifts to Sort the Array](https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array)                                     | [###](./Array/Minimum-Right-Shifts-to-Sort-the-Array.py)                   | O(N) | O(1)   | Easy       | Array                                                           |
2873 | [Maximum Value of an Ordered Triplet I](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i)                                       | [###](./Array/Maximum-Value-of-an-Ordered-Triplet-I.py)                    | O(N) | O(1)   | Easy       | Array                                                           |
2908 | [Minimum Sum of Mountain Triplets I](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i)                                             | [###](./Array/Minimum-Sum-of-Mountain-Triplets-I.py)                       | O(N) | O(N)   | Easy       | Array                                                           |
2909 | [Minimum Sum of Mountain Triplets II](https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii)                                           | [###](./Array/Minimum-Sum-of-Mountain-Triplets-II.py)                      | O(N) | O(N)   | Medium     | Array                                                           |
3000 | [Maximum Area of Longest Diagonal Rectangle](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle)                             | [###](./Array/Maximum-Area-of-Longest-Diagonal-Rectangle.py)               | O(N) | O(1)   | Easy       | Array                                                           |


## Hash Table
|  #  | Title                                    | Solution                       |  Time        | Memory | Difficulty    | Tag          |
|-----|------------------------------------------|--------------------------------| ------------ |--------| ------------- |--------------|
0013 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer) | [###](./Hash-Table/Roman-to-Integer.py) | O(N) | O(1)   | Easy | Hash Table, Math, String|
0383 | [Ransom Note](https://leetcode.com/problems/ransom-note) | [###](./Hash-Table/Ransom-Note.py) | O(N) | O(1)   | Easy | Hash Table, String, Counting|
0387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string) | [###](./Hash-Table/First-Unique-Character-in-a-String.py) | O(N) | O(N)   | Easy | Hash Table, String, Queue, Counting|
0389 | [Find the Difference](https://leetcode.com/problems/find-the-difference) | [###](./Hash-Table/Find-the-Difference.py) | O(N) | O(N)   | Easy | Hash Table, String, Bit Manipulation, Sorting|
2367 | [Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets) | [###](./Hash-Table/Number-of-Arithmetic-Triplets.py) | O(N) | O(N)   | Easy | Array, Hash Table, Two Pointers, Enumeration|


## Binary Search
|  #  | Title                                    | Solution                       | Time    | Memory | Difficulty    | Tag                  |
|-----|------------------------------------------|--------------------------------|---------|--------| ------------- |----------------------|
0035 | [Search Insert Position](https://leetcode.com/problems/search-insert-position) | [###](./Hash-Table/Search-Insert-Position.py) | O(logN) | O(1)   | Easy | Array, Binary Search |


## Math
|  #  | Title           | Solution                           | Time    | Memory | Difficulty    | Tag                                    |
|-----|---------------- |------------------------------------|---------|--------| ------------- |----------------------------------------|
0009 | [Palindrome Number](https://leetcode.com/problems/palindrome-number) | [###](./Math/Palindrome-Number.py) | O(1)    | O(1)   | Easy | Math                                   |
0067 | [Add Binary](https://leetcode.com/problems/add-binary) | [###](./Math/Add-Binary.py) | O(1)    | O(1)   | Easy | Math, String, Bit Manipulation, Simulation                                  |
0069 | [Sqrt(x)](https://leetcode.com/problems/sqrtx) | [###](./Math/Sqrt(x).py)           | O(logN) | O(1)   | Easy | Math, Binary Search                    |
0070 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs) | [###](./Math/Climbing-Stairs.py) | O(N)    | O(1)   | Easy | Math, Dynamic Programming, Memoization |
0171 | [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number) | [###](./Math/Excel-Sheet-Column-Number.py) | O(N)    | O(1)   | Easy | Math, String                           |
0202 | [Happy Number](https://leetcode.com/problems/happy-number) | [###](./Math/Happy-Number.py) | O(k)    | O(k)   | Easy | Hash Table, Math, Two Pointers                           |
0326 | [Power of Three](https://leetcode.com/problems/power-of-three) | [###](./Math/Power-of-Three.py) | O(1)    | O(1)   | Easy | Math, Recursion                          |
0412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz) | [###](./Math/Fizz-Buzz.py) | O(N)    | O(1)   | Easy | Math, String, Simulation                         |
1342 | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero) | [###](./Math/Number-of-Steps-to-Reduce-a-Number-to-Zero.py) | O(logN) | O(1)   | Easy | Math, Bit Manipulation                        |
2535 | [Difference Between Element Sum and Digit Sum of an Array](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array) | [###](./Math/Difference-Between-Element-Sum-and-Digit-Sum-of-an-Array.py) | O(N)    | O(1)   | Easy | Array, Math                         |


## Bit Manipulation
|  #  | Title           | Solution                           | Time | Memory          | Difficulty    | Tag                                    |
|-----|---------------- |------------------------------------|------| --------------- | ------------- |----------------------------------------|
0190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits) | [###](./Bit-Manipulation/Reverse-Bits.py)           | O(1) | O(1) | Easy | Divide and Conquer, Bit Manipulation                  |
0191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits) | [###](./Bit-Manipulation/Number-of-1-Bits.py)           | O(1) | O(1) | Easy | Divide and Conquer, Bit Manipulation                  |
1720 | [Decode XORed Array](https://leetcode.com/problems/decode-xored-array) | [###](./Bit-Manipulation/Decode-XORed-Array.py)           | O(N) | O(1) | Easy | Array, Bit Manipulation                 |
2859 | [Sum of Values at Indices With K Set Bits](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits) | [###](./Bit-Manipulation/Sum-of-Values-at-Indices-With-K-Set-Bits.py)           | O(N) | O(1) | Easy | Array, Bit Manipulation                  |


## String
|  #  | Title                                    | Solution                                 | Time     | Memory | Difficulty | Tag           |
|-----|------------------------------------------|------------------------------------------|----------|--------|------------|---------------|
0014 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) | [###](./String/Longest-Common-Prefix.py) | O(NlogN) | O(1)   | Easy       | String, Trie  |
0020 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | [###](./String/Valid-Parentheses.py)     | O(N) | O(N)   | Easy       | String, Stack |
0058 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word) | [###](./String/Length-of-Last-Word.py)     | O(N) | O(1)   | Easy       | String|
0125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome) | [###](./String/Valid-Palindrome.py)      | O(N) | O(N)   | Easy       | Two Pointers, String |
0242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram) | [###](./String/Valid-Anagram.py)      | O(N) | O(N)   | Easy       | Hash Table, String, Sorting |
0316 | [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters) | [###](./String/Remove-Duplicate-Letters.py)      | O(N) | O(k)   | Medium     | String, Stack, Greedy, Monotonic Stack |
1662 | [Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent) | [###](./String/Check-If-Two-String-Arrays-are-Equivalent.py)      | O(N) | O(1)   | Easy     | Array, String |
1773 | [Count Items Matching a Rule](https://leetcode.com/problems/count-items-matching-a-rule) | [###](./String/Count-Items-Matching-a-Rule.py)      | O(N) | O(1)   | Easy     | Array, String |
1816 | [Truncate Sentence](https://leetcode.com/problems/truncate-sentence) | [###](./String/Truncate-Sentence.py)      | O(N) | O(1)   | Easy     | Array, String |


## Linked List
|  #  | Title                                    | Solution                                       | Time | Memory | Difficulty    | Tag           |
|-----|------------------------------------------|------------------------------------------------|------|--------| ------------- |---------------|
0021 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) | [###](./Linked-List/Merge-Two-Sorted-Lists.py) | O(N) | O(1)   | Easy | Linked list, Recursion  |
0083 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list) | [###](./Linked-List/Remove-Duplicates-from-Sorted-List.py) | O(N) | O(1)   | Easy | Linked list|
0141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle) | [###](./Linked-List/Linked-List-Cycle.py) | O(N) | O(1)   | Easy | Hash Table, Linked List, Two Pointers |
0160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists) | [###](./Linked-List/Intersection-of-Two-Linked-Lists.py) | O(M+N) | O(1)   | Easy | Hash Table, Linked List, Two Pointers|
0206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) | [###](./Linked-List/Reverse-Linked-List.py) | O(N) | O(1)   | Easy | Linked List, Recursion|
0234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list) | [###](./Linked-List/Palindrome-Linked-List.py) | O(N) | O(N)   | Easy | Linked List, Two Pointers, Stack, Recursion|
0876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list) | [###](./Linked-List/Middle-of-the-Linked-List.py) | O(N) | O(1)   | Easy | Linked list, Two Pointers|



## Two Pointers
|  #  | Title                                    | Solution                                       | Time     | Memory | Difficulty    | Tag           |
|-----|------------------------------------------|------------------------------------------------|----------|--------| ------------- |---------------|
0028 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string) | [###](./Two-Pointers/Find-the-Index-of-the-First-Occurrence-in-a-String.py) | O(N) | O(1)   | Easy | Two Pointers, String, String Matching  |
0344 | [Reverse String](https://leetcode.com/problems/reverse-string) | [###](./Two-Pointers/Reverse-String.py) | O(N) | O(1)   | Easy | Two Pointers, String  |



## Tree
|  #  | Title                                    | Solution                                       | Time     | Memory  | Difficulty    | Tag                                                              |
|-----|------------------------------------------|------------------------------------------------|----------|---------| ------------- |------------------------------------------------------------------|
0094 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal) | [###](./Tree/Binary-Tree-Inorder-Traversal.py) | O(N) | O(N)    | Easy | Stack, Tree, Depth-First Search, Binary Tree                     |
0100 | [Same Tree](https://leetcode.com/problems/same-tree) | [###](./Tree/Same-Tree.py) | O(N) | O(N)    | Easy | Tree, Depth-First Search, Breadth-First Search, Binary Tree      |
0101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree) | [###](./Tree/Symmetric-Tree.py)                | O(N) | O(N)    | Easy | Tree, Depth-First Search, Breadth-First Search, Binary Tree      |
0104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) | [###](./Tree/Maximum-Depth-of-Binary-Tree.py)                | O(N) | O(H)    | Easy | Tree, Depth-First Search, Breadth-First Search, Binary Tree      |
0108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) | [###](./Tree/Convert-Sorted-Array-to-Binary-Search-Tree.py)                | O(N) | O(logN) | Easy | Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree |



## Database
|  #  | Title                                    | Solution                                           | Difficulty  | Tag       |
|-----|------------------------------------------|----------------------------------------------------|------------ |-----------|
0175 | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables) | [###](./Database/Combine-Two-Tables.sql) | Easy | Database  |
0181 | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers) | [###](./Database/Employees-Earning-More-Than-Their-Managers.sql) | Easy | Database  |
0182 | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails) | [###](./Database/Duplicate-Emails.sql) | Easy | Database  |
0183 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order) | [###](./Database/Customers-Who-Never-Order.sql) | Easy | Database  |
0196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails) | [###](./Database/Delete-Duplicate-Emails.sql) | Easy | Database  |
0197 | [Rising Temperature](https://leetcode.com/problems/rising-temperature) | [###](./Database/Rising-Temperature.sql) | Easy | Database  |
0511 | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i) | [###](./Database/Game-Play-Analysis-I.sql) | Easy | Database  |
0577 | [Employee Bonus](https://leetcode.com/problems/employee-bonus) | [###](./Database/Employee-Bonus.sql) | Easy | Database  |
0584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee) | [###](./Database/Find-Customer-Referee.sql) | Easy | Database  |
0586 | [Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders) | [###](./Database/Customer-Placing-the-Largest-Number-of-Orders.sql) | Easy | Database  |
0595 | [Big Countries](https://leetcode.com/problems/big-countries) | [###](./Database/Big-Countries.sql) | Easy | Database  |
0596 | [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students) | [###](./Database/Classes-More-Than-5-Students.sql) | Easy | Database  |
0607 | [Sales Person](https://leetcode.com/problems/sales-person) | [###](./Database/Sales-Person.sql) | Easy | Database  |
0610 | [Triangle Judgement](https://leetcode.com/problems/triangle-judgement) | [###](./Database/Triangle-Judgement.sql) | Easy | Database  |
0619 | [Biggest Single Number](https://leetcode.com/problems/biggest-single-number) | [###](./Database/Biggest-Single-Number.sql) | Easy | Database  |
0620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies) | [###](./Database/Not-Boring-Movies.sql) | Easy | Database  |