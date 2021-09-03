def is_palindrome(input_string):
	new_string = input_string.replace(' ','').upper()
	if new_string == new_string[::-1]:
		return True
	else:
		return False
	

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("Kaiak")) # Should be True