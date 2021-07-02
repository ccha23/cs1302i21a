import pandas as pd
import os
from IPython import display

def get_status(eid, assignment):
    stages = ['submitted', 'autograded', 'feedback']
    for status in reversed(stages):
        if os.path.isdir(f'../nbgrader/{status}/{eid}/{assignment}'):
            return status
    else:
        return ''


def get_link(eid, assignment):
    status = get_status(eid, assignment)
    output = status and f'<a href="../../formgrader/manage_students/{eid}/{assignment}" target=_blank>{status}</a>'
    if status == 'feedback':
        output += f'<br><a href="../../tree/nbgrader/feedback/{eid}/{assignment}" target=_blank>(generated)</a>'
    return output 

def load_students(assignment, csv, sections = None, include_test_student = False):
    df = pd.read_csv('cs5483.csv')
    if sections:
        df = df.loc[df['section'].isin(sections)]
    if include_test_student:
        df = df.append({'eid': 'test-student'}, ignore_index = True)
    df[assignment] = [get_link(row["eid"],assignment) for (index, row) in df.iterrows()]
    display.display(display.HTML(f'<a href="../../formgrader/manage_submissions/{assignment}" target=_blank>See all submissions</a>'))
    display.display(display.HTML(df.to_html(escape=False)))
    # display.display(display.HTML('test-student:<br>'+get_link('test-student',assignment)))
    return df





