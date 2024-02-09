# Run Jupyter Notebook

Create new Python virtual environment and activate it

```
virtualenv datathonenv
. datathonenv/activate
```

Install necessary dependencies

```
pip install geopandas shapely folium jupyter
```

Run a local JupyterLab where the content of your current working directory will automatically be loaded

```
jupyter-lab
```