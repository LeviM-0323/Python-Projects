# Streamlit Tests

This project is a playground for learning and experimenting with [Streamlit](https://streamlit.io/), a fast way to build and share data apps in Python. It demonstrates a variety of Streamlit components, including interactive widgets, data visualization, and media input, using both built-in and external data.

---

## Features

- **Streamlit Widgets:**  
  - Buttons, sliders, checkboxes, text input, selectbox, and more in the sidebar.
  - Camera and microphone input components.
- **Data Handling:**  
  - Loads and displays a sample Uber rides dataset.
  - Uses caching for efficient data loading.
- **Visualization:**  
  - Bar charts and maps of Uber pickups by hour.
  - Option to display raw data.
- **Layout:**  
  - Organized sidebar for controls and main area for data and charts.
- **Learning Focus:**  
  - Code is annotated and modular for easy experimentation and learning.

---

## Project Structure

```
PythonProjects/StreamlitTests/
│
├── Streamlit_Tests.py   # Main Streamlit app
├── Pages/
│   │
│   ├── 1_Mortgage_Calculator.py   # Mortgage calulcator page
│   ├── 2_Prompt_Playground.py     # Prompt Playground page
│   └── 3_Data_Explorer.py         # Data Explorer page
│
├── requirements.txt     # Project Requirements
└── README.md            # Project documentation
```

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/LeviM-0323/Python-Projects.git
   cd PythonProjects/StreamlitTests
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage

To run the app, use:
```sh
streamlit run Streamlit_Tests.py
```

- The app will open in your browser.
- Use the sidebar to interact with widgets and explore Streamlit features.
- View Uber pickup data, charts, and maps.

---

## Customization

- **Try new Streamlit components:**  
  Add or modify widgets in `Streamlit_Tests.py`.
- **Change data source:**  
  Replace the Uber dataset URL with your own CSV or data source.
- **Experiment with layouts:**  
  Use columns, expanders, and tabs for more advanced UI.

---

## License

This project is open source and available under the MIT License.