import matplotlib.pyplot as plt
import seaborn as sns

import bokeh as bk
from bokeh.io import show, output_notebook
from bokeh.plotting import figure

from plotnine import *
import plotnine.options as pno

import altair as alt

import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np

dataset = pd.read_csv("data.csv")
