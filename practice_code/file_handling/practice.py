# 'r' - used for read
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# 'w' - used for write (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello, world!")

# 'a' - used for append
with open("file.txt", "a") as f:
    f.write("\nAppended line")

# 'r+' - used for both read and write
with open("file.txt", "r+") as f:
    data = f.read()
    f.seek(0)
    f.write("Updated")

# 'w+' - used for write and read (overwrites) and also it create the file if not exist
with open("file.txt", "w+") as f:
    f.write("New content")
    f.seek(0)
    print(f.read())

# 'a+' - used for append and read and also it create the file if not exsit
with open("file.txt", "a+") as f:
    f.write("\nAnother line")
    f.seek(0)
    print(f.read())
