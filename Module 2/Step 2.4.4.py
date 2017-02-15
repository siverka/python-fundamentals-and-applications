with open('input_2.4.4.txt', 'r') as infile, open('output_2.4.4.txt', 'w') as outfile:
    lines = [line.strip() for line in infile.readlines()]
    out = '\n'.join(lines[::-1])
    outfile.write(out)

