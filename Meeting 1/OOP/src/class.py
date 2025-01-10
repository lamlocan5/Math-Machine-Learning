class StringUtils:
    # Thuộc tính lớp
    default_prefix = "Hello"

    def __init__(self, text):
        self.text = text

    @staticmethod 
    def reverse_string(text):
        return text[::-1] 

    @classmethod
    def greet(cls, name):
        return f"{cls.default_prefix}, {name}!"

    def display(self):
        print(f"Original: {self.text}")
        print(f"Reversed: {self.reverse_string(self.text)}")

# Sử dụng phương thức tĩnh
reversed_text = StringUtils.reverse_string("Python")
print(f"Reversed Text: {reversed_text}")  # Output: Reversed Text: nohtyP

# Sử dụng phương thức lớp
greeting = StringUtils.greet("Alice")
print(greeting)  # Output: Hello, Alice!

# Sử dụng instance và phương thức
utils = StringUtils("Object-Oriented Programming")
utils.display()
# Output:
# Original: Object-Oriented Programming
# Reversed: gnimmargorP detneirO-tcejbO

