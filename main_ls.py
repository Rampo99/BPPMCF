from algo import algo
from read_file import read_file
import os  # import 'os' module: necessary to write on and read files
from swap_items import swap_items
from swap_items import count_colors

if __name__ == '__main__':
    current_directory = os.getcwd()  # store the current working directory path in the current_directory variable for further use

    for instance_file in os.listdir(current_directory+'/Instances/input'):  # for each file inside the instance/input directory
        with open(current_directory+'/Instances/input/'+instance_file, 'r') as f:  # open each file as f
            items, bin_cap, max_bins = read_file(f)  # calls read_file function for each file f
            bins = algo(items, bin_cap, max_bins)  # calls ffd function
            if bins == -1:  # eventually provide an error message
                color_frag = "ERROR: Too many bins required"
            else:  # it iterates over the bins and counts the number of distinct colors in each bin
                bins = swap_items(bins)
                color_frag = sum(count_colors(_bin) for _bin in bins)
                item_bins = {}
                for i, _bin in enumerate(bins):
                    for item in _bin['objects']:
                        item_bins[item[2]] = i + 1  # Store the associated bin number for each item

        with open(current_directory+'/Instances/output/'+instance_file, 'w') as f:  # open the output file as f
            f.write(f"{color_frag}\n")  # write color_frag's value on each file

            bin_list = list(item_bins.keys())  # create a list with the keys of the dictionary item_bins
            bin_list.sort()  # sort the list in increasing way
            sorted_dict = {i: item_bins[i] for i in bin_list}  # create a new dictionary
            for item_bin in sorted_dict:  # for each item in the dictionary
                f.write(f"{sorted_dict[item_bin]}\n")  # write on the file the number of the bin
