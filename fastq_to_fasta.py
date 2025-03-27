#!/usr/bin/env python3

# Import the sys module for command-line argument handling

import argparse
import os

# Define the main function to convert FASTQ to FASTA format
def fastq_to_fasta(input_file, output_file):
    # Open input FASTQ file for reading and output FASTA file for writing
    with open(input_file, 'r') as fastq, open(output_file, 'w') as fasta:
        while True:
            # Read the sequence identifier line (starts with '@')
            header = fastq.readline().strip()
            # If we've reached the end of the file, exit the loop
            if not header:
                break
            # Read the sequence line
            seq = fastq.readline().strip()
            fastq.readline()  # Skip the '+' line (it's not used in FASTA format)
            fastq.readline()  # Skip the quality score line (not used in FASTA format)
            
            # Write the sequence in FASTA format
            # Remove the '@' from the header and use '>' instead
            fasta.write(f">{header[1:]}\n{seq}\n")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # create argument parses
    parser = argparse.ArgumentParser(description='Convert FASTQ to FASTA', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # add arguments
    parser.add_argument('-i', '--input', required=True, help='Input FASTQ File')
    parser.add_argument('-o', '--output', help='Output FASTA File (defaults to .fasta files)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print detailed progress information')
    #parse command line arguments
    args = parser.parse_args()
    #set input and output file names
    input_file = args.input
    if not args.output:
        output_file = os.path.splitext(input_file)[0] + '.fasta'
    else:
        output_file = args.output
    # check if files exists
    if not os.path.isfile(input_file): parser.error(f"Input file '{input_file}' does not exists")
    if args.verbose: print(f"Converting '{input_file}' to '{output_file}'")
    # call conversion function
    fastq_to_fasta(input_file, output_file)
    print(f"Conversion complete. FASTA file saves as {output_file}")