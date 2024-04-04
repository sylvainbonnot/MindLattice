import fnmatch
import os

def search_notes(keyword):
    matches = []
    for root, dirnames, filenames in os.walk('PKM'):
        for filename in fnmatch.filter(filenames, '*.md'):
            note_path = os.path.join(root, filename)
            with open(note_path, 'r') as file:
                if keyword.lower() in file.read().lower():
                    matches.append(note_path)
    return matches

if __name__=='__main__':
    # Example usage
    print(search_notes('new note'))

