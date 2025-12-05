# Given two lists of numbers called secret and key, use the following steps to decode the message.

# 1.Get the absolute value of each number in secret
# 2.For each index add the number in key to the result of step 1
# 3.Reverse the order of the numbers in the result of step 2
# 4.Use integer division to divide each number in the result of step 3 by 5
# 5.Add the index of each number in step 4 to its value
# 6.Convert each value to a character
# 7.use ''.join(list) to convert a list of characters to a string .    


# Example lists
secret = [10, -25, 30, -45, 50]
key    = [1, 2, 3, 4, 5]

# Step 1: Get absolute value of each number in secret
step1 = [abs(n) for n in secret]

# Step 2: Add corresponding number in key
step2 = [step1[i] + key[i] for i in range(len(secret))]

# Step 3: Reverse the list
step3 = step2[::-1]

# Step 4: Integer divide each number by 5
step4 = [n // 5 for n in step3]

# Step 5: Add the index to each number
step5 = [step4[i] + i for i in range(len(step4))]

# Step 6: Convert each value to a character
chars = [chr(n) for n in step5]

# Step 7: Join characters into a string
decoded_message = ''.join(chars)

print(decoded_message)
                                                                      