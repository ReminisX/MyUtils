import os.path

folder_path = r"D:\CPU-Z"
full_size = 0
for parent, dirs, files in os.walk(folder_path):
    full_size = sum(os.path.getsize(os.path.join(parent, file)) for file in files)
print(full_size, "%.2f MB" % (full_size/1024/1024))
