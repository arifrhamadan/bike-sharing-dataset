import streamlit as st

# Main function to run the Streamlit app
def main():
    # Title of the dashboard
    st.title("Dashboard Analisis Data Peminjaman Sepeda")

    # Business Questions
    st.header("Pertanyaan Bisnis")
    st.write("1. Berapa distribusi peminjaman sepeda berdasarkan musim?")
    st.write("2. Bagaimana hubungan antara temperatur dan jumlah peminjaman sepeda?")

    # Data Visualizations
    st.header("Visualisasi Data")

    # Visualisasi distribusi peminjaman sepeda berdasarkan musim
    st.subheader("Distribusi Peminjaman Sepeda Berdasarkan Musim")
    try:
        st.image('season_distribution.png')  # Gambar pertama
    except FileNotFoundError:
        st.error("Gambar 'season_distribution.png' tidak ditemukan.")

    # Visualisasi hubungan temperatur dan jumlah peminjaman sepeda
    st.subheader("Hubungan Temperatur dan Jumlah Peminjaman Sepeda")
    try:
        st.image('temp_vs_cnt.png')  # Gambar kedua
    except FileNotFoundError:
        st.error("Gambar 'temp_vs_cnt.png' tidak ditemukan.")


# Run the app
if __name__ == '__main__':
    main()
