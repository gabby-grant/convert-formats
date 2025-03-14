#!/usr/bin/env python3

# Import necessary modules
import sys
import argparse

# Define the main function to convert GFF3 to BED format
def gff3_to_bed(input_file, output_file):
    # Open input GFF3 file for reading and output BED file for writing
    with open(input_file, 'r') as gff, open(output_file, 'w') as bed:
        # Iterate through each line in the GFF3 file
        for line in gff:
            # Skip comment lines (starting with #)
            if line.startswith('#'):
                continue
            
            # Split the line into fields
            fields = line.strip().split('\t')
            # Skip lines that don't have the expected 9 fields
            if len(fields) != 9:
                continue
            
            # Extract relevant information from GFF3 fields
            chrom = fields[0]  # Chromosome name
            start = int(fields[3]) - 1  # Convert 1-based GFF3 start to 0-based BED start
            end = int(fields[4])  # End position
            name = '.'  # Default name (will be updated if possible)
            score = '0'  # Default score
            strand = fields[6]  # Strand information
            
            # Parse the attributes field to extract name information
            attributes = dict(item.split('=') for item in fields[8].split(';') if '=' in item)
            # Use ID or Name as the feature name if available
            if 'ID' in attributes:
                name = attributes['ID']
            elif 'Name' in attributes:
                name = attributes['Name']
            
            # Write the formatted BED line to the output file
            bed.write(f"{chrom}\t{start}\t{end}\t{name}\t{score}\t{strand}\n")

# Define the main execution function
def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Convert GFF3 to BED format')
    parser.add_argument('input', help='Input GFF3 file')
    parser.add_argument('output', help='Output BED file')
    args = parser.parse_args()

    # Call the conversion function with input and output file names
    gff3_to_bed(args.input, args.output)
    # Print a completion message
    print(f"Conversion complete. BED file saved as {args.output}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # If so, call the main function
    main()