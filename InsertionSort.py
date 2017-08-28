'''
An implementation of insertion sort
API: insertion_sort(sample_str)
'''

# TODO 1: Add better degugging
# TODO 2: Use better constants

sample_str = list('insertionsort')

def swap_chars(unsorted_str, indx1, indx2):
    temp_char = unsorted_str[indx1]
    unsorted_str[indx1] = unsorted_str[indx2]
    unsorted_str[indx2] = temp_char

def insertion_sort(unsorted_str):

    ''' Divide the array into two parts
        1. Sorted Part: At the beginning to the marker
        2. Unsorted Part: From the marker to the end
        For every marker, check against the sorted part and stop when you get to the part where the earlier
        character is lesser than marker. Else keep going.
        After the iteration, advance the marker by one.
    '''

    for unsorted_indx in range(1, len(unsorted_str)):
        for sorted_indx in range(unsorted_indx, 0, -1):

            if unsorted_str[sorted_indx] < unsorted_str[sorted_indx -1]:
                # swap it in that spot
                swap_chars(unsorted_str, sorted_indx, sorted_indx-1)

if __name__ == '__main__':

    print "Initial Str: ", sample_str
    insertion_sort(sample_str)
    print "Sorted Str: ", sample_str