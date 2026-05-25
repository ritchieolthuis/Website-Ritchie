with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # Skip line 1768 (index 1767)
    if i == 1767 and line.strip() == "</div>":
        print("Skipping 1768")
        continue
    # Skip lines 1821 to 1832 (indices 1820 to 1831)
    if 1820 <= i <= 1831:
        print("Skipping", i+1)
        continue
    new_lines.append(line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
