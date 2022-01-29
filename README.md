# Sorting-Techniques
### Collection of Sorting Techniques implemented in Python

[1. Selection Sort](Selection_Sort.py)<br>
- Time complexity is O(N^2)
- 1st minimum element is brought to the 1st position, 2nd minimum element to the 2nd position, 3rd minimum element to the 3rd position and so on ...

[2. Bubble Sort](Bubble_Sort.py)<br>
- Time complexity is O(N^2)
- 1st largest element is brought to the last position, 2nd largest element to the 2nd last position, 3rd largest element to the 3rd last position and so on...

[3. Insertion Sort](Insertion_Sort.py)<br>
- Time complexity is O(N^2)
- Insert a new element at the correct position of the sorted list

[4. Merge Sort](Merge_Sort.py)<br>
- Time complexity is O(N*log(N))
- Divide a list into two equal halves and merge the sorted halves
- Extra space is required as a new list is created everytime

[5. Shell Sort](Shell_Sort.py)<br>
- Time complexity is O(N^2)

[6. Quick Sort](Quick_Sort.py)<br>
- Worst case time complexity is O(N^2)
- Avg. case time complexity is O(N*log(N))
- Choose 1st element as pivot and move elements that are smaller than the pivot towards left of the pivot and the larger ones to the right
- After moving, sort the elements that are smaller than the pivot separately and larger than the pivot separately
- Works in-place as no extra space is required
