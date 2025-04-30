import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(
    page_title="Streamlit Tests",
    page_icon="☠️",
)

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column] = pd.to_datetime(data[date_column])
    return data

st.title("☠️ Streamlit Tests")

# st.write("Loading data...")

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
# bar.progress(i + 1)
# time.sleep(0.1)

# Basic Components in a side bar
st.sidebar.title("Streamlit Tests")
st.sidebar.markdown("Welcome to my first ever Streamlit App! This is a collection of me learning how to use different Streamlit components following the Streamlit documentation")
st.sidebar.divider()
st.sidebar.subheader("Basic Components")
st.sidebar.write('Hello World! This is a test of st.write()!')
if st.sidebar.button("Button Test"):
    st.sidebar.write('Button was pushed!')
    x = st.sidebar.slider("Slider Test")
    st.sidebar.write(x, "squared is", x * x)
if st.sidebar.checkbox("Checkbox Test"):
    st.sidebar.write('Checkbox checked!')
else:
    st.sidebar.write('Checkbox unchecked!')
    st.sidebar.text_input("Text input test", key="Test")
    st.sidebar.write('Selectbox')
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    option = st.sidebar.selectbox(
        'Which number do you like best?',
        df['first column']
    )
    st.sidebar.write('You selected: ', option)

st.sidebar.camera_input("Your Webcam")
st.sidebar.audio_input("Microphone input")

# Advanced elements in main page
# st.subheader("Advanced components with the help of Numpy and Pandas")
# left_column, right_column = st.columns(2)

# left_column.write("Left Column")

# left_column.write('Table')
# dataframe = pd.DataFrame(
# np.random.randn(12, 4),
# columns=('col %d' % i for i in range(4))
# )
# left_column.dataframe(dataframe.style.highlight_max(axis=0))

# right_column.write("Right Column")

# right_column.write('Map - This one is REALLY cool')
# map_data = pd.DataFrame(
# np.random.randn(1000, 2) / [50,50] + [43.139752, -80.761428],
# columns=['lat', 'lon']
# )
# right_column.map(map_data)

# st.write('Line Graph')
# chart_data = pd.DataFrame(
# np.random.randn(20, 3),
# columns=['a','b','c']
# )
# st.line_chart(chart_data)

date_column = 'date/time'
data_url = ('https://s3-us-west-2.amazonaws.com/'
        'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Done! (using st.cache_data)')

if st.checkbox("Show raw data"):
    st.subheader("Raw Uber Data")
    st.write(data)

st.divider()
st.subheader("Number of pickups by hour")
hist_values = np.histogram(
    data[date_column].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.divider()
st.subheader("Map of pickups by hour")
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[date_column].dt.hour == hour_to_filter]
st.subheader(f'Map of pickups at {hour_to_filter}:00')
st.map(filtered_data)

st.divider()