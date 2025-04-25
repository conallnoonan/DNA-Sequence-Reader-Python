# Name: Conall Noonan
# CSE 160
# Homework 2: DNA analysis

# This program reads in DNA sequencer output and computes statistics, such as
# the GC content, AT content, nucleotide counts, etc.  Run it from the command
# line like this:
#   python dna_analysis.py myfile.fastq
#
# For teaching purposes, a few more comments than normal have been added in
# to explain in detail what some Python constructs are doing.

# The sys module supports reading files, command-line arguments, etc.
import sys


# Function to convert the contents of dna_filename into a string of nucleotides
def filename_to_string(dna_filename):
    '''
    dna_filename - the name of a file in expected file format
    Expected file format is: Starting with the second line of the file,
    every fourth line contains nucleotides.
    The function will read in all lines from the file containing nucleotides,
    concatenate them all into a single string, and return that string.
    '''

    # YOU DO NOT NEED TO MODIFY THIS FUNCTION.

    # Creates a file object from which data can be read.
    input_file = open(dna_filename)

    # String containing all nucleotides that have been read from the file so
    # far.
    seq = ""

    # The current line number (= the number of lines read so far).
    line_num = 0

    for line in input_file:
        line_num = line_num + 1
        # if we are on the 2nd, 6th, 10th line...
        if line_num % 4 == 2:
            # Remove the newline characters from the end of the line
            line = line.rstrip()
            # Concatenate this line to the end of the current string
            seq = seq + line
    # close file
    input_file.close()
    return seq


# Function to return GC Classification
def classify(gc_content):
    '''
    gc_content - a number representing the GC content
    Returns a string representing GC Classification. Must return one of
    these: "low", "moderate", or "high" based on the cutoffs in the spec
    '''
    if gc_content > 58:
        classification = "high"
    elif gc_content < 35:
        classification = "low"
    else:
        classification = "moderate"
    return classification


def nano_suitable(gc_content):
    '''
    gc_content - a number representing the GC content
    Returns a boolean representing if the given GC Content is suitable for
    DNA nanotechnology
    '''
    if gc_content > 50 and gc_content < 60:
        return True
    else:
        return False


###########################################################################
# Main program begins here
#

# Check if the user provided an argument
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this "
          "program.")
    sys.exit(2)

# Save the 1st argument provided by the user, as a string.
# Note: sys.argv[0] is the name of the program itself (dna_analysis.py)
file_name = sys.argv[1]

# Open the file and read in all nucleotides into a single string of letters
nucleotides = filename_to_string(file_name)

###
# Compute DNA sequence statistics
###

# YOUR CODE GOES BELOW THIS POINT
# Total nucleotides seen so far.
total_count = 0

# Number of G, C, A, and T nucleotides seen so far, as well as the total count
# and the length of the nucleotide string
a_count = 0
t_count = 0
g_count = 0
c_count = 0
total_count = a_count + c_count + g_count + t_count
len_nuc = len(nucleotides)

for base in nucleotides:
    total_count = total_count + 1

# if and elif statements to calculate nucleotide contents
    if base == 'A':
        a_count = a_count + 1
    elif base == 'C':
        c_count = c_count + 1
    elif base == 'G':
        g_count = g_count + 1
    elif base == 'T':
        t_count = t_count + 1
    elif base in 'TGAC':
        total_count = total_count + 1
# calculate the AT and GC content and the sum of all of the valid nucleotides
gc_count = g_count + c_count
at_count = a_count + t_count
sum_counts = a_count + c_count + g_count + t_count
# calculate the GC and AT content and the AT/GC ratio and classify the GC
# content
gc_content = float(gc_count) / sum_counts
at_content = float(at_count) / sum_counts
atgc_ratio = (a_count + t_count) / (g_count + c_count)
gc_content_percent = gc_content * 100
classification = classify(gc_content_percent)
# print statements for output
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G count:', g_count)
print('C count:', c_count)
print('A count:', a_count)
print('T count:', t_count)
print('Sum of G+C+A+T counts:', sum_counts)
print('Total count:', total_count)
print('Length of nucleotides:', len_nuc)
print('AT/GC Ratio:', atgc_ratio)
print("GC Classification: " + classification + " GC content")
print("Is suitable for nanotech:", nano_suitable(gc_content_percent))
# You can add more assertions here to check properties that you think
# should be true about your results. If the condition listed is false,
# then the given message will be printed.
assert total_count == len(nucleotides), "total_count != length of nucleotides"
