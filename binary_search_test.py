from binary_search import binary_search_iterative

# Test iterative binary_search
test_list = [1, 3, 9, 11, 15, 19, 29]
test_val = 25
print(binary_search_iterative(test_list, test_val)) # -1, that is, not found

test_val = 15
print(binary_search_iterative(test_list, test_val)) # 4, that is, 15 found at index 4

