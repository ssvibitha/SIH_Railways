import os

for f in os.listdir("raw"):
    path = os.path.join("raw", f)
    print(f"{f:25} {os.path.getsize(path)/1024:.1f} KB")