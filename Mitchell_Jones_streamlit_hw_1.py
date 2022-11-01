import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(100)

# Create a random array of data that we will use for our y values
y_data = np.random.randn(x_limit)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(100)

# Create a random array of data that we will use for our y values
y_data = np.random.randn(x_limit)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart(df).mark_point().encode(
    x='x',
    y='y')

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_point().encode(
    x='x',
    y='y')

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("""
The 5 changes I made were:
- Change 1: Colored by X
- Change 2: Changed mark type
- Change 3: Changed mark size
- Change 4: Turned off grid
- Change 5: Made the plot interactive.
""")

scatter = alt.Chart(df).mark_square(size = 150).encode(
    x='x',
    y='y',
    color = 'x').configure_axis(grid = False).interactive()


st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.write('Original viz:')
# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

plot = alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q')

st.altair_chart(plot, use_container_width = True)

st.write('My changed viz:')

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

plot = alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color=alt.Color('z', scale=alt.Scale(scheme='oranges')),
    tooltip=['x', 'y'])

st.altair_chart(plot, use_container_width = True)
st.markdown("""
The 2 changes I made were:
- Change 1: Added tooltip.
- Change 2: Changed heatmap color to orange.
"""
)


