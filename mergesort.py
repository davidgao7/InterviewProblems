def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)  # for subarr with only one element, it will just go to the next line
        mergeSort(
            right)  # in thread, it will go to forth thread, return , out to third thread and moving down to 14th line

        # ======================================================#
        # Two iterators for traversing the two halves
        i = 0  # the 14th line
        j = 0

        # Iterator for the main list
        k = 0

        # inside first half and second half...
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # left is less than right, sorted, just put to list
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                # left is greater than right, not sorted, put right in
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        # append unsorted at the end
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(myList)
mergeSort(myList)
print(myList)
