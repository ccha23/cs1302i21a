---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.9.1
kernelspec:
  display_name: Python 3.7 (XPython)
  language: python
  name: xpython
---

+++ {"slideshow": {"slide_type": "slide"}}

# Pandas

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

+++ {"slideshow": {"slide_type": "subslide"}}

In this lab, we will analyze COVID19 data using a powerful package called [`pandas`](https://pandas.pydata.org/docs/user_guide/index.html).  
The package name comes from *panel data* and *Python for data analysis*.

+++ {"slideshow": {"slide_type": "slide"}}

## Loading CSV Files with Pandas 

+++ {"slideshow": {"slide_type": "fragment"}}

[DATA.GOV.HK](https://data.gov.hk/en-data/dataset/hk-dh-chpsebcddr-novel-infectious-agent) provides an [API](https://data.gov.hk/en/help/api-spec#historicalAPI) to retrieve historical data on COVID-19 cases in Hong Kong.

+++ {"slideshow": {"slide_type": "fragment"}}

The following uses the `urlencode` function to create the url that links to a csv file containing probable and confirmed cases of COVID-19 by Aug 1st, 2020.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
from urllib.parse import urlencode

url_data_gov_hk_get = 'https://api.data.gov.hk/v1/historical-archive/get-file'
url_covid_csv = 'http://www.chp.gov.hk/files/misc/enhanced_sur_covid_19_eng.csv'
time = '20200801-1204'
url_covid = url_data_gov_hk_get + '?' + urlencode({
    'url': url_covid_csv,
    'time': time
})

print(url_covid)
```

+++ {"slideshow": {"slide_type": "fragment"}}

`urlencode` creates a string `'url=<...>&time=<...>'` with some [special symbols encoded](https://www.w3schools.com/tags/ref_urlencode.ASP), e.g.:
- `:` is replaced by `%3A`, and
- `/` is replaced by `%2F`.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Write a function `simple_encode` that takes in a string and return a string with `:` and `/` encoded as described above.  
*Hint:* Use the `replace` method of `str`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: simple_encode
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def simple_encode(string):
    '''Returns the string with : and / encoded to %3A and %2F respectively.'''
    ### BEGIN SOLUTION
    return string.replace(':', '%3A').replace('/', '%2F')
    ### END SOLUTION
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-simple_encode
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
assert simple_encode(
    'http://www.chp.gov.hk/files/misc/enhanced_sur_covid_19_eng.csv'
) == 'http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Fenhanced_sur_covid_19_eng.csv'
### BEGIN HIDDEN TESTS
assert simple_encode(
    'https://api.data.gov.hk/v1/historical-archive/get-file'
) == 'https%3A%2F%2Fapi.data.gov.hk%2Fv1%2Fhistorical-archive%2Fget-file'
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "subslide"}}

Like the function `open` that loads a file into memory, `pandas` has a function `read_csv` that loads a csv file.   
The csv file can even reside on the web.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
import pandas as pd
df_covid = pd.read_csv(url_covid)

print(type(df_covid))
df_covid
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above creates a [`DataFrame` object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame). The content of the csv file is displayed as an HTML table conveniently.   
(We can control how much information to show by setting the [display options](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html).)

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Using the function `pd.read_csv`, load `building_list_eng.csv` as `df_building` from the url `url_building`.  

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: df_building
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
url_building_csv = 'http://www.chp.gov.hk/files/misc/building_list_eng.csv'
time = '20200801-1203'
url_building = url_data_gov_hk_get + '?' + urlencode({
    'url': url_building_csv,
    'time': time
})

### BEGIN SOLUTION
df_building = pd.read_csv(url_building)
### END SOLUTION
df_building
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-df_building
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
assert all(df_building.columns == ['District', 'Building name', 'Last date of residence of the case(s)',
       'Related probable/confirmed cases'])  # check column names
### BEGIN HIDDEN TESTS
assert df_building.shape == (2165, 4)
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "subslide"}}

## Selecting and Removing columns

+++ {"slideshow": {"slide_type": "fragment"}}

We can obtain the column labels of a `Dataframe` using its `columns` attribute.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
df_covid.columns
```

+++ {"slideshow": {"slide_type": "fragment"}}

Using the indexing operator `[]`, a column of a `DataFrame` can be returned as a [`Series` object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html), which is essentially a named array.   
We can further use the method `value_counts` to return the counts of different values in another `Series` object.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
series_gender_counts = df_covid['Gender'].value_counts()  # return the number of male and female cases

print(type(series_gender_counts))
series_gender_counts
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** For `df_building`, use the operator `[]` and method `value_counts` to assign `series_district_counts` to a `Series` object that stores the counts of buildings in different district.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: series_district_counts
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN SOLUTION
series_district_counts = df_building['District'].value_counts()
### END SOLUTION
series_district_counts
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-series_district_counts
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
assert all(series_district_counts[['Wong Tai Sin', 'Kwun Tong']] == [313, 212])
### BEGIN HIDDEN TESTS
assert all(series_district_counts[[
    'Wong Tai Sin', 'Kwun Tong', 'Yau Tsim Mong', 'Tuen Mun', 'Sha Tin',
    'Kowloon City', 'Sham Shui Po', 'Kwai Tsing', 'Eastern', 'Sai Kung',
    'Yuen Long', 'North', 'Wan Chai', 'Tsuen Wan', 'Tai Po',
    'Central & Western', 'Southern', 'Islands'
]] == [
    313, 212, 205, 192, 157, 149, 142, 112, 103, 98, 91, 88, 83, 62, 50, 50,
    33, 25
])
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "subslide"}}

In `df_covid`, it appears that the column `Name of hospital admitted` contains no information. We can confirm this by:
1. Returning the column as a `Series` with `df_covid_cases['Name of hospital admitted']`, and
1. printing an array of unique column values using the method `unique`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
df_covid['Name of hospital admitted'].unique()
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Drop the column `Name of hospital admitted` using the `drop` method of the DataFrame. 

Use the keyword argument `inplace=True`, so that the method will 
- mutate the original DataFrame in place instead of 
- creating a copy of the DataFrame with the column dropped.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: drop
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN SOLUTION
### END SOLUTION
df_covid
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-drop
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# tests
assert all(df_covid.columns == ['Case no.', 'Report date', 'Date of onset', 'Gender', 'Age',
       'Hospitalised/Discharged/Deceased', 'HK/Non-HK resident',
       'Case classification*', 'Confirmed/probable'])
```

+++ {"slideshow": {"slide_type": "slide"}}

## Selecting Rows of DataFrame

+++ {"slideshow": {"slide_type": "fragment"}}

We can select the confirmed male cases using the attribute [`.loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) and the indexing operator `[]`.  
`.loc` implements an advanced indexing method `__getitem__` that can take a boolean vector.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
df_confirmed_male = df_covid.loc[(df_covid['Confirmed/probable']=='Confirmed') & (df_covid['Gender']=='M')]
df_confirmed_male
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Assign `df_confirmed_local` to a `DataFrame` of confirmed cases that are local or epidemiologically linked with a local case.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: df_confirmed_local
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN SOLUTION
df_confirmed_local = df_covid.loc[
    (df_covid['Confirmed/probable'] == 'Confirmed')
    & ((df_covid['Case classification*'] == 'Local case')
       | (df_covid['Case classification*'] ==
          'Epidemiologically linked with local case'))]
### END SOLUTION

df_confirmed_local
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-df_confirmed_local
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
# tests
assert set(df_confirmed_local['Case classification*'].unique()) == {
    'Epidemiologically linked with local case', 'Local case'
}
### BEGIN HIDDEN TESTS
assert len(df_confirmed_local) == 2034
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "subslide"}}

## Challenge

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Write a function `case_counts` that 
- takes an argument `district`, and
- returns the number of cases in `district`. 

*Hint:* Be careful that there can be more than one case for each building and there may be multiple buildings associated with one case.  
You may want to use the `split` and `strip` methods of `str` to obtain a list of cases from the `Dataframe`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: case_counts
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def case_counts(district):
    ### BEGIN SOLUTION
    all_cases = []
    for cases in df_building.loc[df_building['District'] ==
                         district,'Related probable/confirmed cases']:
        all_cases.extend([case.strip() for case in cases.split(',')])
    return len(set(all_cases))
    ### END SOLUTION
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-case_counts
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
assert case_counts('Kwai Tsing') == 109
### BEGIN HIDDEN TESTS
assert [
    counts for counts in map(case_counts, [
        'Yau Tsim Mong', 'Wong Tai Sin', 'North', 'Sham Shui Po', 'Tuen Mun',
        'Central & Western', 'Sha Tin', 'Kwun Tong', 'Kwai Tsing', 'Southern',
        'Tai Po', 'Kowloon City', 'Wan Chai', 'Eastern', 'Yuen Long',
        'Sai Kung', 'Tsuen Wan', 'Islands'
    ])
] == [
    204, 368, 70, 126, 153, 44, 124, 201, 109, 27, 39, 151, 74, 87, 79, 88, 52,
    24
]
### END HIDDEN TESTS
```
