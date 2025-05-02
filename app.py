import pandas as pd
import plotly.express as px
import streamlit as st

# Application header
st.header("Interactive Analysis of Vehicle Data in the U.S.")

# Load the data
car_data = pd.read_csv('vehicles_us.csv')  # Ensure the file is in the same directory

# Button to build a histogram
hist_button = st.button('Build Histogram')

if hist_button:  # If the button is clicked
    st.write('Creating a histogram for the "odometer" column')
    fig_hist = px.histogram(car_data, x="odometer", title="Odometer Histogram")
    st.plotly_chart(fig_hist, use_container_width=True)

# Button to build a scatter plot
scatter_button = st.button('Build Scatter Plot')

if scatter_button:  # If the button is clicked
    st.write('Creating a scatter plot for the "price" and "odometer" columns')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Scatter Plot: Price vs Odometer")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Optional challenge: Use checkboxes instead of buttons
st.write("### Optional: Use checkboxes to generate charts")

# Checkbox for the histogram
build_histogram = st.checkbox('Build a Histogram')

if build_histogram:  # If the checkbox is selected
    st.write('Creating a histogram for the "odometer" column')
    fig_hist = px.histogram(car_data, x="odometer", title="Odometer Histogram")
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox for the scatter plot
build_scatter = st.checkbox('Build a Scatter Plot')

if build_scatter:  # If the checkbox is selected
    st.write('Creating a scatter plot for the "price" and "odometer" columns')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Scatter Plot: Price vs Odometer")
    st.plotly_chart(fig_scatter, use_container_width=True)