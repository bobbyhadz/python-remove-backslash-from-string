# Remove backslashes from a String in Python

string = '\\bobby\\hadz\\com\\'
print(string)  # 👉️ \bobby\hadz\com\

# ✅ Remove all backslashes from a string
new_string = string.replace('\\', '')
print(new_string)  # 👉️ bobbyhadzcom

# ---------------------------------------------------

# ✅ Remove first occurrence of backslash from a string

new_string = string.replace('\\', '', 1)
print(new_string)  # 👉️ bobby\hadz\com\