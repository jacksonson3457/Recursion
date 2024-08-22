import sys

def reverse_file(input_path, output_path):
    with open(input_path, 'r') as file:
        content = file.read()
    with open(output_path, 'w') as file:
        file.write(content[::-1])

def copy_file(input_path, output_path):
    with open(input_path, 'r') as file:
        content = file.read()
    with open(output_path, 'w') as file:
        file.write(content)

def duplicate_contents(input_path, n):
    with open(input_path, 'r') as file:
        content = file.read()
    with open(input_path, 'w') as file:
        file.write(content * n)

def replace_string(input_path, needle, newstring):
    with open(input_path, 'r') as file:
        content = file.read()
    content = content.replace(needle, newstring)
    with open(input_path, 'w') as file:
        file.write(content)

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <command> <inputpath> <other-args>...")
        return

    command = sys.argv[1]
    input_path = sys.argv[2]

    if command == 'reverse' and len(sys.argv) == 4:
        output_path = sys.argv[3]
        reverse_file(input_path, output_path)
    elif command == 'copy' and len(sys.argv) == 4:
        output_path = sys.argv[3]
        copy_file(input_path, output_path)
    elif command == 'duplicate-contents' and len(sys.argv) == 4:
        n = int(sys.argv[3])
        duplicate_contents(input_path, n)
    elif command == 'replace-string' and len(sys.argv) == 5:
        needle = sys.argv[3]
        newstring = sys.argv[4]
        replace_string(input_path, needle, newstring)
    else:
        print("Invalid command or arguments")

if __name__ == "__main__":
    main()
