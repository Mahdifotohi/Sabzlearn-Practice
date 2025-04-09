import os
if os.path.exists("file_to_delete.txt"):
    os.remove("file_to_delete.txt")
    print(f"The file '{"file_to_delete.txt"}' has been deleted. ")
else:
    print(f"The file '{"file_to_delete.txt"}' has been deleted. ")
    

