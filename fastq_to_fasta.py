#!/usr/bin/env python3

# Import the sys module for command-line argument handling
import sys

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
    # Check if at least one command-line argument (input file) is provided
    if len(sys.argv) < 2:
        # If not, print usage instructions and exit
        print(f"Usage: {sys.argv[0]} <input.fastq> [output.fasta]")
        sys.exit(1)

    # Get the input file name from the first command-line argument
    input_file = sys.argv[1]
    # If a second argument is provided, use it as the output file name
    # Otherwise, create an output file name by replacing .fastq with .fasta
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.rsplit('.', 1)[0] + '.fasta'

    # Call the conversion function
    fastq_to_fasta(input_file, output_file)
    # Print a completion message
    print(f"Conversion complete. FASTA file saved as {output_file}")