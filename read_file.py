def read_file(f):
    f.readline()  # skip a line
    max_bins = int(f.readline().strip())  # read bins capacity
    bin_cap = int(f.readline().strip())  # read max bins

    for i in range(max_bins + 4):
        f.readline()  # skip the matrix

    color_numbers = int(f.readline().strip())  # read the number of colors
    total_numbers = int(f.readline().strip())  # read the total amount of numbers
    f.readline().strip()
    items = []  # create an array for the items
    index = 0
    for line in f.readlines():  # for all the lines
        if line.strip() == "":
            continue
        parts = line.strip().split()  # create a variable without whitespaces and split it into two substrings
        color = parts[0]  # create a variable color that is equal to the first substring of 'parts'
        size = int(parts[1])  # create a variable color that is equal to the second substring of 'parts'
        index += 1  # assign an index to each item
        items.append((size, color, index))  # adds to items the two variables defined above

    return items, bin_cap, max_bins
