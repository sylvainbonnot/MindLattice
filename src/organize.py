import os

DFLT_PROJECT_ROOT = 'PKM'


def create_or_edit_note(
    project, note_name, project_root=DFLT_PROJECT_ROOT, content=None
):
    project_path = os.path.join(project_root, project)
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    note_path = os.path.join(project_path, note_name + '.md')
    if content:
        with open(note_path, 'w') as file:
            file.write(content)
    else:
        os.system(f'open {note_path}')


if __name__ == '__main__':

    # Example usage
    create_or_edit_note('Project1', 'note3', 'This is a new note.')
