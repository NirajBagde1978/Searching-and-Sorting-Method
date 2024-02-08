from time import sleep


class Searching_Sorting():
    def __init__(self) -> None:
        self.arr = []

    def ele(self):
        num = int(input("How many elements are there : "))
        for i in range(num):
            try:
                ele = int(input("Elements : "))
                self.arr.append(ele)
            except Exception as e:
                print(
                    f"Please Enter a valid Number, this number would not be taken into consideration due to : {e}")
                continue

    def show(self):
        print(self.arr)
        print("\n")

    # <<-----------------------SORTING------------------------->>

    def Bubble_Sort(self):  # O(n^2)
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-1-i):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

        return self.arr

    def Selection_sort(self):  # O(n^2)
        n = len(self.arr)
        for i in range(n):
            min_inx = i
            for j in range(i+1, n):
                if self.arr[min_inx] > self.arr[j]:
                    self.arr[min_inx], self.arr[j] = self.arr[j], self.arr[min_inx]
        return self.arr

    def Insertion_sort(self):  # O(n^2)
        for i in range(1, len(self.arr)):  # this loop is for the original array
            temp = self.arr[i]
            j = i-1
            # this loop is for the sorted array from backwards
            while j >= 0 and temp < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = temp
        return self.arr

    def Quick_sort(self, arr):  # O(n*log(n))
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return self.Quick_sort(less) + [pivot] + self.Quick_sort(greater)

    def Two_way_merge_sort(self, l_r_arr):  # O(n*log(n))
        def merge(left_half, right_half):
            result = []
            i = j = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    result.append(left_half[i])
                    i += 1
                else:
                    result.append(right_half[j])
                    j += 1

            result.extend(left_half[i:])
            result.extend(right_half[j:])

            return result

        if len(l_r_arr) <= 1:
            return l_r_arr

        mid = len(l_r_arr)//2
        left_half = [i for i in l_r_arr[:mid]]
        right_half = [i for i in l_r_arr[mid:]]

        left_half = self.Two_way_merge_sort(left_half)
        right_half = self.Two_way_merge_sort(right_half)

        return merge(left_half, right_half)

    def Radix_sort(self):  # O(n)
        max_element = max(self.arr)
        passes = 0

        while max_element > 0:
            passes += 1
            max_element = max_element // 10

        div = 1

        for i in range(passes):
            count = [0 for i in range(10)]

            for j in range(len(self.arr)):
                idx_number = (self.arr[j] // div) % 10
                count[idx_number] += 1

            for k in range(1, len(count)):
                count[k] = count[k] + count[k - 1]

            sorted_list = [0] * len(self.arr)

            for u in range(len(self.arr) - 1, -1, -1):
                idx_number = (self.arr[u] // div) % 10
                count[idx_number] -= 1
                sorted_list[count[idx_number]] = self.arr[u]

            for y in range(len(self.arr)):
                self.arr[y] = sorted_list[y]

            div *= 10

        return self.arr

    def Bucket_sort(self):  # O(n)
        if len(self.arr) <= 1:
            return self.arr

        # Create buckets
        buckets = [[] for _ in range(10)]

        # Distribute elements into buckets
        for num in self.arr:
            # Since we are dealing with floating points.
            # Use min to avoid index out of range
            index = min(int(10 * num), 9)
            buckets[index].append(num)

        # Sort each bucket using an efficient sorting algorithm
        for i in range(10):
            # Using list's built-in sort method which has O(k log k) time complexity
            buckets[i].sort()

        # Concatenate sorted buckets
        result = [num for bucket in buckets for num in bucket]
        return result

    def Shell_sort(self):  # O(n^2)
        n = len(self.arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                # Insertion sort
                temp = self.arr[i]
                j = i

                while j >= gap and self.arr[j - gap] > temp:
                    self.arr[j] = self.arr[j - gap]
                    j -= gap

                self.arr[j] = temp

            gap = gap // 2

        return self.arr

    def Counting_sort(self):  # O(n)
        max_element = max(self.arr)
        min_element = min(self.arr)
        range_of_elements = max_element - min_element + 1

        # forming the counting array
        counting = [0] * range_of_elements

        # giving the count of the elements in self.arr in the counting array at the adjusted index
        for i in range(len(self.arr)):
            counting[self.arr[i]] += 1

        for i in range(1, range_of_elements):
            counting[i] += counting[i-1]

        # forming the sorted array
        sorted_array = [0]*len(self.arr)

        # giving the specified elements position in the sorted array
        for i in range(len(self.arr)-1, -1, -1):
            counting[self.arr[i]] -= 1
            sorted_array[counting[self.arr[i]]] = self.arr[i]

        # copying the elements of sorted array in the original array
        for i in range(len(self.arr)):
            self.arr[i] = sorted_array[i]

        return self.arr

# <<-----------------SEARCHING----------------->>

    def Binary_search(self, target):  # O(log2(n))
        # In the Binary Search, It is important to sort the array
        # first and then search it,
        # hence the answer may be different, but it is correct if input array elements are sorted
        self.Bubble_Sort()
        n = len(self.arr)
        i = 0
        j = n

        while i <= j:
            c = (i + j) // 2
            if self.arr[c] == target:
                return c
            elif self.arr[c] < target:
                i = c + 1
            else:
                j = c - 1

        return None

    def Sequential_search(self, target):  # O(n)
        n = len(self.arr)
        i = 0
        while i < n and self.arr[i] != target:
            i += 1

        if i < n:
            return i
        else:
            return None

    def Fibonacci_search(self, target):  # O(log n)
        Fibbanocci = [0, 1]
        while Fibbanocci[-1] < len(self.arr):
            next_term = Fibbanocci[-1] + Fibbanocci[-2]
            Fibbanocci.append(next_term)

        offset = -1
        while len(Fibbanocci) > 2:
            i = min(offset + Fibbanocci[-2], len(self.arr) - 1)

            if self.arr[i] == target:
                return i
            elif self.arr[i] < target:
                Fibbanocci = Fibbanocci[:-1]
                offset = i
            else:
                Fibbanocci = Fibbanocci[:-2]

        if len(Fibbanocci) == 2 and self.arr[offset + 1] == target:
            return offset + 1

        return None

    def Sentinel_search(self, target):  # O(n)
        # Append the target as a sentinel at the end of the array
        self.arr.append(target)

        i = 0
        while self.arr[i] != target:
            i += 1

        # Remove the sentinel to maintain the original array
        self.arr.pop()

        if i < len(self.arr):
            return i  # Target found at index i
        else:
            return -1  # Target not found


def main():
    a = Searching_Sorting()
    a.ele()
    a.show()

    print("<============ Operations ============>")
    print("\n")

    flag1 = 0
    while (flag1 != 1):
        choice1 = int(input("1.Searching\n2.Sorting\n3.Exit\nChoice : "))
        print("\n")
        match choice1:
            case 1:
                flag2 = 0
                while (flag2 != 1):
                    choice2 = int(input("1.Binary Search\n2.Sequential Search\n3.Fibonacci Search\n4.Sentinel Search\n5.Exit\nChoice : "))
                    match choice2:
                        case 1:
                            y = int(input("What is to be Searched : "))
                            print(
                                f"The element to be found is at the location : {a.Binary_search(y)}")
                            print("\n")
                            break

                        case 2:
                            t = int(input("What is to be Searched : "))
                            print(
                                f"The element to be found is at the location : {a.Sequential_search(t)}")
                            print('\n')
                            break

                        case 3:
                            u = int(input("What is to be Searched : "))
                            print(
                                f"The element to be found is at the location : {a.Fibonacci_search(u)}")
                            print('\n')
                            break

                        case 4:
                            i = int(input("What is to be Searched : "))
                            print(
                                f"The element to be found is at the location : {a.Sentinel_search(i)}")
                            print('\n')
                            break

                        case 5:
                            print("Exit")
                            flag2 = 1
                            break

                        case _:
                            print("Please, enter a valid Number")
                            print('\n')

            case 2:
                flag3 = 0
                while (flag3 != 1):
                    choice3 = int(input("1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n4.Quick Sort\n5.Two Way Merge Sort\n6.Radix Sort\n7.Bucket Sort\n8.Shell Sort\n9.Counting Sort\n10.Exit\nChoice : "))
                    match choice3:
                        case 1:
                            print(f"The Sorted Array is : {a.Bubble_Sort()}")
                            print('\n')
                            break

                        case 2:
                            print(
                                f"The Sorted Array is : {a.Selection_sort()}")
                            print('\n')
                            break

                        case 3:
                            print(
                                f"The Sorted Array is : {a.Insertion_sort()}")
                            print('\n')
                            break

                        case 4:
                            print(f"The Sorted Array is : {a.Quick_sort()}")
                            print('\n')
                            break

                        case 5:
                            print(
                                f"The Sorted Array is : {a.Two_way_merge_sort(a.arr)}")
                            print('\n')
                            break

                        case 6:
                            print(f"The Sorted Array is : {a.Radix_sort()}")
                            print('\n')
                            break

                        case 7:
                            print(f"The Sorted Array is : {a.Bucket_sort()}")
                            print('\n')
                            break

                        case 8:
                            print(f"The Sorted Array is : {a.Shell_sort()}")
                            print('\n')
                            break

                        case 9:
                            print(f"The Sorted Array is : {a.Counting_sort()}")
                            print('\n')
                            break

                        case 10:
                            print("Exit")
                            flag3 = 1
                            break

                        case _:
                            print("Please Enter A valid Choice")
                            print('\n')

            case 3:
                print("You have Chosen to Exit, Thank you")
                sleep(1)
                flag1 = 1
                break

            case _:
                print("Please Enter a Valid Number", end="")
                print('\n')


if __name__ == "__main__":
    main()
