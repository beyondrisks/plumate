import re

# Read the original file
with open(r'D:\projects\plumate\_data\products.yml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def categorize(title):
    t = title.lower()
    if 'water heater' in t or 'adapter for hose' in t:
        return 'Water Heater'
    if 'roof jack' in t or 'grade stake' in t:
        return 'Roof & Outdoor'
    if any(kw in t for kw in ['brush', 'drill pump', 'street key', 'steet key', '4 in 1']):
        return 'Tools & Accessories'
    if any(kw in t for kw in ['emt', 'anti short', 'ko seal', 'knock out', 'cable connector',
                               'strain relief', 'plastic bushing', 'snap-in stud bushing']):
        return 'Electrical'
    if any(kw in t for kw in ['valve', 'toilet flange', 'flanger', 'snap coupling', 'snap tee',
                               'snap wye', 'snap end cap', 'cleanout', 'pipe coupler',
                               'proforma adapter', 'gasket', 'test cap', 'test plug']):
        return 'Plumbing Fittings'
    if any(kw in t for kw in ['hanger', 'j hook']):
        return 'Hangers'
    if 'strap' in t:
        return 'Straps'
    if 'bracket' in t:
        return 'Brackets'
    if any(kw in t for kw in ['anchor', 'sammy screw', 'nail clip']):
        return 'Anchors & Fasteners'
    if any(kw in t for kw in ['plate', 'pad', 'pex bend', 'spacer bar', 'strut channel',
                               'ceiling wire', 'escutcheon']):
        return 'Supports & Plates'
    if 'wire hook' in t:
        return 'Wire & Cable'
    if any(kw in t for kw in ['clamp', 'clip', 'rubber']):
        return 'Clamps'
    if 'strut' in t:
        return 'Supports & Plates'
    if 'coupler' in t or 'coupling' in t:
        return 'Plumbing Fittings'
    return 'Other'

# Process: find title lines, then update next category line
current_title = None
new_lines = []
categories_count = {}

for line in lines:
    stripped = line.strip()
    # Match title line
    title_match = re.match(r'^- title:\s*(.+)', stripped)
    if title_match:
        current_title = title_match.group(1).strip()
    
    # Match category line and replace
    cat_match = re.match(r'^(\s+)category:\s*(.+)', line)
    if cat_match and current_title:
        indent = cat_match.group(1)
        new_cat = categorize(current_title)
        categories_count[new_cat] = categories_count.get(new_cat, 0) + 1
        new_lines.append(f'{indent}category: {new_cat}\n')
        current_title = None
        continue
    
    new_lines.append(line)

# Write back
with open(r'D:\projects\plumate\_data\products.yml', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# Summary
print("Category counts:")
for cat, count in sorted(categories_count.items()):
    print(f"  {cat}: {count}")
print(f"  Total: {sum(categories_count.values())}")
print("\nDone!")
