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
# # Student Registration

# %% [markdown]
# Run the following and check that the fields `eid`, `e_name`, and `email` are available. If not, rename the field title appropriately in the excel file.

# %%
import pandas as pd
import os
import re

# df_add = pd.read_excel('cs1302.xlsx', engine='openpyxl')
# df_add.to_csv('cs1302.csv', index=False)
# df_add = pd.read_csv('cs1302.csv')
df_add = pd.read_csv('cs5483.csv')
df_add

# %% [markdown]
# ## Add students

# %% [markdown]
# **Prequisites that needs to be done by server admin:**
# - Student accounts must be created and added to jupyterhub first before they can be added to the course.  
#   - [How to add users to Jupyterhub][addtojupyterhub]
# - The following environment variables needs to be set properly according to the values in the course service in `/etc/jupyterhub/jupyterhub_config.py`, e.g., in `~/.bash_profile`:
#   ```bash
#   export JUPYTERHUB_USER=...
#   export JUPYTERHUB_API_TOKEN=...
#   ```
#
# [addtojupyterhub]: https://tljh.jupyter.org/en/latest/howto/admin/admin-users.html#:~:text=Type%20the%20names%20of%20users,the%20JupyterHub%20with%20administrator%20privileges!

# %%
import subprocess
def run(cmd):
    print(subprocess.check_output(cmd, text=True, shell=True, stderr=subprocess.STDOUT))


# %% [markdown]
# Print the current list of students.

# %%
run('nbgrader db student list')

# %%
execute = input('Execute?') == 'y'
for index, row in df_add.iterrows():
    m = re.match(r"^(?P<last_name>[A-Z \-]+), (?P<first_name>(?:[A-Z\-][a-z \-]*)+)$", row['e-name'])
    command = f"nbgrader db student add {row['EID'].strip()} --last-name='{m.group('last_name').strip()}' --first-name='{m.group('first_name').strip()}' --email={row['Email'].strip()} --lms-user-id=s{row['Stud ID']}"
    print(command)
    if execute:
        run(command)

# %% [markdown]
# ## Remove students

# %% [markdown]
# Use the following to remove specific students.

# %%
to_remove = ['test123']
execute = input('Execute?') == 'y'
for eid in to_remove:
    command = f"nbgrader db student remove {eid.strip()}"
    print(command)
    if execute:
        run(command)

# %% [markdown]
# To remove all students, delete `~/nbgrader/gradebook.db`.
