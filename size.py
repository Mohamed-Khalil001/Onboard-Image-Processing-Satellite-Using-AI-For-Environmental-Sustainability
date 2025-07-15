import os

# Traverse all files and collect sizes
big_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root, file)
        try:
            size = os.path.getsize(path)
            if size > 10 * 1024 * 1024:  # أكبر من 10MB
                big_files.append((size, path))
        except:
            pass

# Sort by size and show top 10
big_files.sort(reverse=True)
for size, path in big_files[:10]:
    print(f"{size / 1024 / 1024:.2f} MB\t{path}")
