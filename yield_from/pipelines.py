
for idx, line in enumerate(lines):
    if not line:
        continue
    lines[idx] = line.strip()

for line in lines:
    # do something

gen = (line for line in lines if line)
gen = (line.strip() for line in lines)
