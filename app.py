import streamlit as st
import pandas as pd
import joblib

# ====================================
# LOAD MODEL
# ====================================
@st.cache_resource
def load_model():
    model = joblib.load("model_exam_score.pkl")
    return model

model = load_model()

# ====================================
# UI
# ====================================
st.title("🎓 Prediksi Nilai Ujian Siswa")
st.write("Masukkan data siswa untuk memprediksi nilai ujian.")

# ====================================
# INPUT USER
# ====================================
sleep_hours = st.slider(
    "Jam Tidur per Hari",
    min_value=0.0,
    max_value=12.0,
    value=7.0,
    step=0.5
)

class_attendance = st.slider(
    "Kehadiran Kelas (%)",
    min_value=0,
    max_value=100,
    value=90
)

study_hours = st.slider(
    "Jam Belajar per Hari",
    min_value=0.0,
    max_value=12.0,
    value=5.0,
    step=0.5
)

sleep_quality = st.selectbox(
    "Kualitas Tidur (1 = Buruk, 5 = Sangat Baik)",
    [1, 2, 3, 4, 5],
    index=3
)

study_method = st.selectbox(
    "Metode Belajar (1 = Membaca, 2 = Video, 3 = Latihan Soal)",
    options={
        1: "Membaca",
        2: "Video",
        3: "Latihan Soal"
    }
)

# ====================================
# DATAFRAME INPUT
# ====================================
input_data = pd.DataFrame({
    "sleep_hours": [sleep_hours],
    "class_attendance": [class_attendance],
    "study_hours": [study_hours],
    "sleep_quality": [sleep_quality],
    "study_method": [study_method]
})

st.subheader("📋 Data Input")
st.write(input_data)

# ====================================
# PREDIKSI
# ====================================
if st.button("🔮 Prediksi Nilai Ujian"):

    prediction = model.predict(input_data)

    st.success(f"🎯 Prediksi Nilai Ujian: **{prediction[0]:.2f}**")

    st.info(
        "Catatan: Hasil prediksi merupakan estimasi berdasarkan pola data historis."
    )
