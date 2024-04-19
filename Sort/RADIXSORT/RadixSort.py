
def radix_sort(arr):
    # Determine the maximum number of digits in any number in the array
    max_digit = len(str(max(arr)))

    # Iterate through each digit position, starting from the ones place
    for i in range(max_digit):
        # Create magical buckets, one for each digit (0-9)
        buckets = [[] for _ in range(10)]

        # Distribute numbers into buckets based on the current digit position
        for num in arr:
            # Extract the digit at the current position
            digit = (num // (10 ** i)) % 10
            # Place the number into the corresponding bucket based on the digit
            buckets[digit].append(num)

        # Collect numbers from buckets and reconstruct the array
        arr = [num for bucket in buckets for num in bucket]

    # Return the sorted array
    return arr

# Example usage of radix_sort
nums = [103, 45, 231, 78, 982, 12, 4]
sorted_nums = radix_sort(nums)
print("Sorted array:", sorted_nums)



"""
Sure! Let's break down the `radix_sort` function step by step:

1. **Determine Maximum Digit Length:**
    - `max_digit = len(str(max(arr)))`: Determine the maximum number of digits among all elements in the input array `arr`. This will determine the number of iterations needed to sort the array based on each digit's place value.

2. **Iterate through Digits:**
    - `for i in range(max_digit)`: Iterate through each digit position from the least significant digit (units place) to the most significant digit.

3. **Initialize Buckets:**
    - `buckets = [[] for _ in range(10)]`: Initialize 10 buckets, one for each possible digit value (0-9). These buckets will be used to temporarily store elements based on their digit value during each iteration.

4. **Distribute Elements into Buckets:**
    - `for num in arr:`: Iterate through each number `num` in the input array `arr`.
    - `(num // (10 ** i)) % 10`: Extract the current digit at position `i` (from right to left) by dividing `num` by `10^i` and then taking the remainder when divided by 10. This operation isolates the digit at position `i`.
    - `buckets[digit].append(num)`: Place the number `num` into the appropriate bucket based on its current digit value.

5. **Collect Elements from Buckets:**
    - `arr = [num for bucket in buckets for num in bucket]`: After distributing all elements into buckets based on their digit values, reconstruct the input array `arr` by concatenating all elements from each bucket in order.

6. **Repeat for Next Digit:**
    - Repeat steps 3-5 for each subsequent digit position, from the least significant digit to the most significant digit.

7. **Return Sorted Array:**
    - `return arr`: Return the sorted array after completing all iterations through each digit position.

Overall, radix sort works by sorting elements based on each digit's place value, from the least significant digit to the most significant digit. By iteratively distributing elements into buckets based on their digit values and then collecting them back in order, radix sort effectively sorts the entire array.
"""