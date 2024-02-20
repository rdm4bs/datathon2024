# Using Python in a Jupyter Notebook

Create a new virtual environment for Python 3 and activate it

<table>
    <tr>
        <th>Linux</th>
        <th> Windows, having <a href="https://docs.python.org/3/using/windows.html#python-launcher-for-windows">Python launcher</a> installed</th>
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
py -3 -m venv datathonenv
.\datathonenv\Scripts\activate
```
</td>
</tr>
</table>

Install necessary dependencies (for additional information refer to [JupyterLab installation](https://jupyter.org/install))

```bash
pip install jupyter geopandas folium matplotlib mapclassify requests
```

Start a local JupyterLab in your current working directory from where you can interactively run any `.ipynb` file

```bash
jupyter-lab
```

### Optional: export to plain script

If you want to export the example notebook into a plain Python script for other use, run

```bash
jupyter nbconvert --to python .\intro_python.ipynb
```

## Resources

- Jupyter Notebook examples for [spatial data processing](https://github.com/jupyter/jupyter/wiki#earth-science-and-geo-spatial-data)
- Python for Geographic Data Analysis: [Retrieving data from Web Feature Service (WFS)](https://python-gis-book.readthedocs.io/en/latest/part2/chapter-09/nb/01-retrieving-data-from-wfs.html)


## Credit

Many thanks to [Michael Roth](https://www.researchgate.net/profile/Michael-Roth-5) for his inspirations on using Jupyter Notebooks with GeoPandas and Folium.
