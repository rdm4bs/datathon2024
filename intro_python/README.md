# Run Jupyter Notebook

Create new Python virtual environment and activate it

<table>
<tr>
<td> Linux </td> <td> Windows </td>
</tr>
<tr>
<td>

```bash
virtualenv datathonenv
. datathonenv/activate
```

</td>
<td>
    
```bash
virtualenv datathonenv
.\datathonenv\Scripts\activate
```
</td>
</tr>
</table>

With Python3, `virtualenv` is not nececssary: `python3 -m venv datathonenv` also creates the virtual environment. 

Install necessary dependencies

```
pip install geopandas shapely folium jupyter matplotlib mapclassify requests
```

Run a local JupyterLab where the content of your current working directory will automatically be loaded

```
jupyter-lab
```

## Credit

Many thanks to [Michael Roth](https://github.com/MichaelRothDLR) for his inspirations on using Jupyter Notebooks with GeoPandas and Folium.
