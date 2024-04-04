import os


def generate_index():
    index_content = "# Index\n\n"
    for root, dirs, files in os.walk('PKM'):
        for file in files:
            if file.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, file), 'PKM')
                index_content += f"- [{file}]({rel_path})\n"
    with open('PKM/index.md', 'w') as index_file:
        index_file.write(index_content)


if __name__ == '__main__':
    # Example usage
    generate_index()
