def algo(items, bin_cap, max_bins):
    items.sort(key=lambda x: (int(x[1]), x[0]), reverse=True)
    bins = [{'colors': [], 'size': 0, 'objects': [], 'cap': bin_cap} for _ in range(max_bins)]

    for item in items:
        color = item[1]
        weight = item[0]

        best_bin = None
        min_color_frag = float('inf')

        for _bin in bins:
            if _bin['size'] + weight <= bin_cap:
                color_frag = 0
                if color not in _bin['colors']:
                    color_frag += 1

                for existing_color in _bin['colors']:
                    if existing_color != color:
                        color_frag += 1

                if color_frag < min_color_frag:
                    min_color_frag = color_frag
                    best_bin = _bin

        if best_bin is None:
            return -1

        best_bin['objects'].append(item)
        best_bin['size'] += weight
        if color not in best_bin['colors']:
            best_bin['colors'].append(color)

    return [_bin for _bin in bins if _bin is not None]
