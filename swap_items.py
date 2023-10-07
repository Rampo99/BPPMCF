from itertools import combinations


def count_colors(_bin):
    colors = set()
    for item in _bin['objects']:
        colors.add(item[1])
    return len(colors)


def swap_items(bins):
    # Calculate the initial color fragmentation
    initial_color_frag = sum(count_colors(_bin) for _bin in bins)

    # Generate all possible pairs of bins
    bin_pairs = combinations(bins, 2)

    # Perform local search by swapping items between bins
    improved = True
    while improved:
        improved = False
        for bin1, bin2 in bin_pairs:
            for item1 in bin1['objects']:
                for item2 in bin2['objects']:
                    # Swap items between bins
                    bin1['objects'].remove(item1)
                    bin2['objects'].remove(item2)
                    bin1['objects'].append(item2)
                    bin2['objects'].append(item1)

                    # Update bin sizes
                    bin1['size'] -= item1[0]
                    bin1['size'] += item2[0]
                    bin2['size'] -= item2[0]
                    bin2['size'] += item1[0]

                    # Calculate the new color fragmentation
                    new_color_frag = sum(count_colors(_bin) for _bin in bins)

                    if new_color_frag < initial_color_frag and (_bin["size"] <= _bin["cap"] for _bin in bins):
                        improved = True
                        initial_color_frag = new_color_frag
                        break

                    # Revert the swap if it doesn't improve the color fragmentation
                    bin1['objects'].remove(item2)
                    bin2['objects'].remove(item1)
                    bin1['objects'].append(item1)
                    bin2['objects'].append(item2)

                    # Revert the bin size changes
                    bin1['size'] -= item2[0]
                    bin1['size'] += item1[0]
                    bin2['size'] -= item1[0]
                    bin2['size'] += item2[0]

                if improved:
                    break
            if improved:
                break

    return bins
