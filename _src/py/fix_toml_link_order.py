toml_file = 'videos.toml'

new_toml = []
counter = 1

with open(toml_file, 'r') as file:
    for line in file:
        if line.startswith("["):
            string = '[' + '{0:03d}'.format(counter) + ']' + '\n'
            counter += 1
        else:
            string = line
        new_toml.append(string)

with open("new.toml", 'w') as file:
    file.writelines(new_toml)
