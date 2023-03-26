# Define two arrays
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]

# Create an empty result array
result_array = []

# Add corresponding elements of both arrays and store the result in the result array
for i in range(len(array1)):
    result_array.append(array1[i] + array2[i])

# Print the result array
print(result_array)
