import os.path

my_dir = 'main'
os.chdir(my_dir)

dirs = []
for current_dir, _, files in os.walk('.'):
    if any([f.endswith('.py') for f in files]):
        dirs.append(current_dir.replace('.', my_dir))

os.chdir('..')

with open('output_2.4.6_main.txt', 'w') as output:
    output.write('\n'.join(sorted(dirs)))

