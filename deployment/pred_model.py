import streamlit as st
import pandas as pd
import pickle

def run_model_prediction():
    st.title("Prediksi Harga Laptop")

    # Load Model dan Preprocessing Pipeline
    with open('best_random_forest_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    
    with open('preproc_pipeline.pkl', 'rb') as file_2:
        preproc_pipeline = pickle.load(file_2)

    # Input pengguna
    os = st.selectbox('What OS are you using?', ['Windows 10', 'No OS', 'Linux', 'Windows 7', 'Chrome OS', 'macOS', 'Windows 10 S', 'Mac OS X', 'Android'])
    screen = st.selectbox('What Screen are you using?', ['Full HD', 'Standard', '4K Ultra HD', 'Quad HD+'])
    cpu_model = st.text_input('What type of CPU are you using?')
    primary_storage = st.selectbox('What type of Primary Storage are you using?', ['SSD', 'HDD', 'Flash Storage', 'Hybrid'])
    secondary_storage = st.selectbox('What type of Secondary Storage are you using?', ['No', 'HDD', 'SSD', 'Hybrid'])
    ram = st.select_slider('How much Ram?', options=list(range(2, 65, 2)), value=2)
    screen_w = st.select_slider('Width screen (px):', options=[1366, 1440, 1600, 1920, 2160, 2256, 2304, 2400, 2560, 2736, 2880, 3200, 3840], value=1920)
    screen_h = st.select_slider('Height screen (px):', options=[768, 900, 1080, 1200, 1440, 1504, 1600, 1800, 1824, 2160], value=1080)
    cpu_freq = st.select_slider('What\'s the CPU frequency (GHz)?', options=[round(i * 0.1, 1) for i in range(9, 37)], value=1.0)

    if st.button("Prediksi"):
        input_data = pd.DataFrame({
            'OS': [os],
            'Screen': [screen],
            'CPU_model': [cpu_model],
            'PrimaryStorageType': [primary_storage],
            'SecondaryStorageType': [secondary_storage],
            'Ram': [ram],
            'ScreenW': [screen_w],
            'ScreenH': [screen_h],
            'CPU_freq': [cpu_freq]
        })

        st.subheader("Data yang dimasukkan:")
        st.write(input_data)

        processed_data = preproc_pipeline.transform(input_data)
        prediction = loaded_model.predict(processed_data)

        st.write('Prediksi harga laptop: ')
        st.write(prediction)

if __name__ == '__main__':
    run_model_prediction()