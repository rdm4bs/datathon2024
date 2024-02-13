# Run Jupyter Notebook

Create a new virtual environment for Python 3 and activate it

<table>
<tr>
<td> Linux </td> <td> Windows </td>
</tr>
<tr>
<td>

```bash
python3 -m venv datathonenv
. datathonenv/activate
```

</td>
<td>
    
```bash
python3 -m venv datathonenv
.\datathonenv\Scripts\activate
```
</td>
</tr>
</table>

Install necessary dependencies

```
pip install geopandas shapely folium jupyter matplotlib mapclassify requests
```

Run a local JupyterLab where the content of your current working directory will automatically be loaded

```
jupyter-lab
```

## Supplementary tutorials

- Jupyter Notebook examples for [spatial data processing](https://github.com/jupyter/jupyter/wiki#earth-science-and-geo-spatial-data)
- Python for Geographic Data Analysis: [Retrieving data from Web Feature Service (WFS)](https://python-gis-book.readthedocs.io/en/latest/part2/chapter-09/nb/01-retrieving-data-from-wfs.html)


## Credit

Many thanks to [Michael Roth](https://github.com/MichaelRothDLR) for his inspirations on using Jupyter Notebooks with GeoPandas and Folium.
