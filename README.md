This Python code defines a class called Searching_Sorting that encapsulates various searching and sorting algorithms. The class provides 
methods for sorting a list of numbers using different algorithms such as Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Two Way Merge Sort, Radix Sort, Bucket Sort, 
Shell Sort, and Counting Sort. Additionally, it includes methods for searching for elements within the sorted list using Binary Search, Sequential Search, Fibonacci Search, and Sentinel Search algorithms.

Here's a breakdown of the major components of the code:

1. Initialization:
  The Searching_Sorting class is initialized with an empty list self.arr.

2. Element Input:
   The ele() method prompts the user to input the number of elements and the elements themselves, which are added to the list self.arr.

3. Sorting Algorithms:
  Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Two Way Merge Sort, Radix Sort, Bucket Sort, Shell Sort, and Counting Sort are implemented as methods of the Searching_Sorting class.
Each sorting method sorts the list self.arr in place and returns the sorted list.

4. Searching Algorithms:
  Binary Search, Sequential Search, Fibonacci Search, and Sentinel Search are implemented as methods of the Searching_Sorting class.
Each searching method takes a target value as input and returns the index of the target element if found, or None or -1 otherwise.

5. Main Functionality:
  a. The main() function serves as the entry point of the program.
  b. It instantiates an object of the Searching_Sorting class, prompts the user to input elements, and displays a menu for selecting various sorting and searching operations.
  c. Users can choose between searching and sorting operations and then select specific algorithms to execute.
  d. The program continues running until the user chooses to exit.

6. User Interaction:
  The program interacts with the user through the console, allowing them to input elements, choose operations, and see the results of sorting and searching operations.
