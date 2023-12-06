import sys
import os
from urllib.request import urlopen

PY_TEMPLATE = """def main():
    print('Hello World!')

if __name__ == '__main__':
    main()
"""


def fetch_project_euler_content(n):
    # Pad n with 0s to make it 3 characters long
    padded_n = str(n).zfill(3)

    # Construct the URL
    url = f'https://projecteuler.net/minimal={n}'
    file_header = f'<h1><a href="https://projecteuler.net/problem={n}">https://projecteuler.net/problem={n}</a></h1>'

    try:
        # Make a GET request to the URL using urlopen
        with urlopen(url) as response:
            # Read the content from the response
            content = response.read().decode('utf-8')

            # Check if the content is non-empty
            if content:
                # Create the directory if it doesn't exist
                directory = f'src/{padded_n}'
                os.makedirs(directory, exist_ok=True)

                # Write the content to a Markdown file
                file_path = f'{directory}/problem_{padded_n}.md'
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f'{file_header}\n{content.strip()}\n')
                with open(f'{directory}/main.py', 'w') as f:
                    f.write(PY_TEMPLATE)
                print(f"Problem written to: {file_path}")
                print(f"Template written to: {directory}/main.py")
            else:
                print(f"Error: Empty content received from the URL.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if a command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <integer_n>")
    else:
        try:
            # Get the integer value from the command line argument
            n = int(sys.argv[1])
            fetch_project_euler_content(n)
        except ValueError:
            print("Error: Please provide a valid integer value.")
