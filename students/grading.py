# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3.7 (XPython)
#     language: python
#     name: xpython
# ---

# %% [markdown]
# # For Grading Assignments

# %% [markdown]
# - See https://nbgrader.readthedocs.io/en/stable/command_line_tools/index.html for details of the `nbgrader` commands.

# %%
# %reset -f
from students import *

# %% [markdown]
# ## Collect and autograde assignments

# %% [markdown]
# Specify the assignment to be graded.

# %%
assignment = 'TutorialA'

# %% [markdown]
# Collect assignments as soon as possible after the deadlines. Otherwise, assignments submitted after the deadline may be collected.

# %%
# !nbgrader collect --assignment={assignment}

# %% [markdown]
# Backup `~/nbgrader` to `~/old`.

# %%
# !bash backup.sh

# %% [markdown]
# Autograde assignments. Autograde can fail if students renamed their notebook or duplicated/removed any answer/test cells. Fix the students' submission by going to the `~/nbgrader/submitted/`, and run the autograde again.

# %%
# !nbgrader autograde --assignment={assignment}

# %% [markdown]
# If autograding completes succesfully, backup again before manual grading.

# %%
# !bash backup.sh

# %% [markdown]
# ## Manual Grading

# %% [markdown]
# The following show the assignment status and links for manual grading.

# %%
df = load_students(assignment, 'students.csv', include_test_student = True)

# %%

# %% [markdown]
# - If there is no link for the student, that means the student has not submitted.  
# - If the status is 'submitted', you need to autograde the assignment first.
# - Grade exercises that require manual grading, and 
# - Give feedback to both autograded and manually graded assignments.
# - ~~Enter the student grades in the Canvas gradebook.~~

# %% [markdown]
# After manual grading: 
# 1. backup and generate the feedback by running the cells below, and 
# 1. rerun the above `load_students` function to see updated status and generated feedback link.

# %%
# !./backup

# %%
# !nbgrader generate_feedback --assignment={assignment}

# %% [markdown]
# If feedback needs to be changed for a student, use the assignment links above and rerun generate_feedback with the flags `--force` and `--student=<eid>`.

# %% [markdown]
# ## Release feedback

# %% [markdown]
# Generated feedback needs to be released to students.

# %%
# !nbgrader release_feedback --assignment={assignment}

# %% [markdown]
# After you have released the feedback, notify the students to fetch the feedback. 
