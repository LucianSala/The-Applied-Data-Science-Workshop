#!/usr/bin/env python
# coding: utf-8

# <img src="../assets/packt-banner.png" alt="">

# # Chapter 1: Introduction to Jupyter Notebooks
# 
# We look at core Jupyter features to use in your Notebooks, along with additional functionality that you may find useful and Python libraries we'll be using in this book.
# 
# ---

# ## Basic functionality and features
# 
# Examples of useful notebook features such as getting help, using tab, and Jupyter's magic functions.
# 
# ---

# ### Jupyter Features    
# 
# ---

# #### Basic Keyboard Shortcuts
# - `Shift + Enter` to run cell
# - `Escape` to leave cell
# - `a` to add a cell above
# - `b` to add a cell below
# - `dd` to delete a cell
# - `m` to change cell to Markdown (after pressing escape)
# - `y` to change cell to Code (after pressing escape)
# - Arrow keys move cells (after pressing escape)
# - `Enter` to enter cell   
# 
# 
# ---

# #### Getting Help
# - add question mark to end of object

# In[1]:


# Get the numpy arange docstring
import numpy as np
get_ipython().run_line_magic('pinfo', 'np.arange')


# In[2]:


# Get the python sort function docstring
get_ipython().run_line_magic('pinfo', 'sorted')


# In[3]:


# See what functions are available for an object
a = np.array([1, 2, 3])
get_ipython().run_line_magic('psearch', 'a.*')


# In[ ]:





# In[ ]:





# ---

# #### Tab Completion
# 
# Example of Jupyter tab completion include:
# - listing available modules on import   
# `import <tab>`   
# `from numpy import <tab>`
# - listing available modules after import         
# `np.<tab>`   
# - function completion    
# `np.ar<tab>`   
# `sor<tab>([2, 3, 1])`   
# - variable completion    
# `myvar_1 = 5`   
# `myvar_2 = 6`   
# `my<tab>`   
# - listing relative path directory contents   
# `../<tab>`   
# (then press enter on a folder and tab again to show its contents)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ---

# #### Jupyter Magic Functions
# List of the available magic commands:

# In[4]:


get_ipython().run_line_magic('lsmagic', '')


# ---

# In[5]:


# Display plots inline
get_ipython().run_line_magic('matplotlib', 'inline')


# ---
# **Timers**

# In[6]:


a = [1, 2, 3, 4, 5] * int(1e5)


# In[7]:


get_ipython().run_cell_magic('time', '', '# Get runtime for the entire cell\n\nfor i in range(len(a)):\n    a[i] += 5\n')


# In[8]:


# Get runtime for one line
get_ipython().run_line_magic('time', 'a = [_a + 5 for _a in a]')


# In[9]:


# Average results of many runs
get_ipython().run_line_magic('timeit', 'set(a)')


# ---

# **Using bash in the notebook**
# 
# *Note*: this section may not work on Windows machines unless you have configured your shell environment in Jupyter. You need not worry, as there's rarely any need to use bash in the Notebook. Feel free to skip over this section.
# 
# Alternatively, you can try to fix the issue using one of the following methods:
# 
#  - Open up [Anaconda Prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt), then navigate to the source code and start `jupyter notebook`
#  - Open up [git bash](https://github.com/jupyter/help/issues/181#issuecomment-341059517), then navigate to the source code and start `jupyter notebook`
#  - Try to point Jupyter towards the git shell by [adding the following code](https://medium.com/@konpat/using-git-bash-in-jupyter-noteobok-on-windows-c88d2c3c7b07) (or similar for your system) to `~/.jupyter/jupyter_notebook_config.py`:
# 
# ```
# c.NotebookApp.terminado_settings = {
#     'shell_command': ['C:\\Program Files\\Git\\bin\\bash.exe']
# }
# 
# ```

# In[10]:


get_ipython().run_cell_magic('bash', '', '\necho "using bash from inside Jupyter!" > test-file.txt\nls\necho ""\ncat test-file.txt\nrm test-file.txt\n')


# In[11]:


get_ipython().run_line_magic('ls', '')


# In[12]:


get_ipython().run_cell_magic('bash', '', 'pwd\n')


# ---
# **External magic functions**   
# Note: these can be installed with pip by doing "pip install package_name"

# - *ipython-sql* enables SQL code cells
# 
# Source: https://github.com/catherinedevlin/ipython-sql
# 
# Install with:
# ```
# pip install ipython-sql
# ```

# In[13]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[14]:


get_ipython().run_cell_magic('sql', 'sqlite://', "\nSELECT *\nFROM (\n    SELECT 'Hello' as msg1, 'World!' as msg2\n);\n")


# ---
# - *watermark* helps document python library versions for reproducability
# 
# Source: https://github.com/rasbt/watermark
# 
# Install with:
# ```
# pip install watermark
# ```

# In[15]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('pinfo', '%watermark')


# In[16]:


get_ipython().run_line_magic('watermark', '-d -v -m -p requests,numpy,pandas,matplotlib,seaborn,sklearn')


# ---

# ### Activity: Using Jupyter to learn about Pandas DataFrames
# 
# _Note: If desired, the following code can be removed from the student version of the notebook and replaced with empty cells._
# 
# ---

# In[17]:


# Load the pandas library

import pandas as pd


# In[18]:


# Pull up the help docstring for a pandas DataFrame

get_ipython().run_line_magic('pinfo', 'pd.DataFrame')


# In[19]:


# Use a dictionary to create a DataFrame with "fruit" and "score" columns

fruit_scores = {
    'fruit': ['apple', 'orange', 'banana', 'blueberry'],
    'score': [4, 2, 9, 8],
}
df = pd.DataFrame(data=fruit_scores)


# In[20]:


# Display the DataFrame

df


# In[ ]:


# Use tab completion to pull up a list of functions for df
# df.<tab>

df.


# In[22]:


# Pull up the docstring for the sort_values DataFrame function

get_ipython().run_line_magic('pinfo', 'df.sort_values')


# In[23]:


# Sort the DataFrame by score in descending order

df.sort_values(by='score', ascending=False)


# In[24]:


# Use the timeit magic function to test how long sorting takes

get_ipython().run_line_magic('timeit', "df.sort_values(by='score', ascending=False)")


# ---

# In[ ]:




