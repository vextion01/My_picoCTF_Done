file_path = 'dictionary.txt'

with open(file_path, 'r') as file:
    # Read the content of the file
    text = file.read()

    # Split the multiline string into lines
    lines = text.split('\n')

    # Use a list comprehension to strip whitespaces from each line
    stripped_lines = [line.strip() for line in lines]

    # Join the stripped lines back into a single string
    result = '\n'.join(stripped_lines)

    print(result)