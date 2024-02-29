import streamlit as st
import os
import py3Dmol

# Function to list all .xyz files in a directory
def list_xyz_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.xyz')]

# Function to read and return the content of an XYZ file
def read_xyz_file(xyz_file_path):
    with open(xyz_file_path, 'r') as file:
        return file.read()

# Streamlit app starts here
st.title('SI Visualizer for Ladder molecules paper')
st.markdown('[Click here to read the manuscript](https://doi.org/10.26434/chemrxiv-2023-29v0h)')


# Directory containing the .xyz files
xyz_files_directory = 'xyz_files'

# List all .xyz files in the directory
xyz_files = list_xyz_files(xyz_files_directory)

# Dropdown to select an XYZ file
selected_file = st.selectbox('Select an XYZ file', xyz_files)

# Button to visualize the selected XYZ file
if st.button('Visualize'):
    # Full path to the selected file
    full_path_to_file = os.path.join(xyz_files_directory, selected_file)

    # Read the selected XYZ file
    xyz_content = read_xyz_file(full_path_to_file)

    # Visualize the molecule using py3Dmol
    xyzview = py3Dmol.view(width=640, height=480)
    xyzview.addModel(xyz_content, 'xyz')
    xyzview.setStyle({'stick': {}})
    xyzview.zoomTo()
    
    # Display the visualization in Streamlit
    xyzview.show()
    st.components.v1.html(xyzview._make_html(), width=640, height=480, scrolling=False)

