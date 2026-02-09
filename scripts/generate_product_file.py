import os
from pathlib import Path
data_path = Path(r"C:\Users\mikez\Downloads\products")
file_names = []
file_paths = []
for file in data_path.glob("*.jpg"):
    file_name = file.name
    file_names.append(file_name)
    file_name = file_name.lower().replace(" ", "_")    
    file_paths.append(f"assets/images/products/{file_name}")
    file.rename(file.parent / file_name)

# write to a yaml file
with open("products.yaml", "w") as f:
    f.write("products:\n")
    for i in range(len(file_names)):
        f.write(f"  - title: {file_names[i]}\n")
        f.write(f"    image: {file_paths[i]}\n")
        f.write(f"    category: Category A\n")
        f.write(f"    price: 0\n")
        f.write(f"    description: {file_names[i]}\n")
