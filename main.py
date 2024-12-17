import pandas as pd
from keras.models import load_model
import pickle
import numpy as np

# Memuat model dan scaler yang telah disimpan
loaded_model = load_model('model_lstm.h5')

with open('scaler.pkl', 'rb') as f:
    loaded_scaler = pickle.load(f)

data = pd.read_pickle('dataframe.pkl')

time_step = 30

# Fungsi untuk membuat dataset baru berdasarkan tanggal input
def prepare_input_data(start_date, end_date, dataframe, time_step):
    """
    Menyiapkan data untuk prediksi masa depan berdasarkan rentang tanggal.
    """
    # Tambahkan tanggal masa depan ke dataframe
    future_dates = pd.date_range(start=start_date, end=end_date)
    new_data = dataframe.reindex(dataframe.index.union(future_dates))

    # Ambil nilai terakhir yang telah ada untuk proyeksi data selanjutnya
    last_data_scaled = loaded_scaler.transform(new_data[['Close']].dropna())

    # Memproyeksikan nilai jika ada missing di masa depan
    for date in future_dates:
        input_sequence = last_data_scaled[-time_step:]
        input_sequence = input_sequence.reshape(1, time_step, 1)

        # Prediksi nilai berikutnya
        predicted_value = loaded_model.predict(input_sequence)[0][0]
        scaled_value = [[predicted_value]]

        # Tambahkan nilai hasil prediksi ke dataset
        last_data_scaled = np.vstack((last_data_scaled, scaled_value))

    # Invers data prediksi kembali ke skala asli
    predicted_close_values = loaded_scaler.inverse_transform(last_data_scaled[-len(future_dates):])
    new_data.loc[future_dates, 'Close'] = predicted_close_values.ravel()

    return new_data

# Fungsi untuk memprediksi harga masa depan
def predict_future_prices(start_date, end_date):
    """
    Memprediksi harga saham penutupan di masa depan berdasarkan input tanggal.
    """
    new_data = prepare_input_data(start_date, end_date, data, time_step)

    # Hanya menampilkan rentang data yang diprediksi
    return new_data.loc[start_date:end_date, 'Close']

# Contoh penggunaan
future_start_date = '2024-09-02'
future_end_date = '2024-09-06'

predicted_prices = predict_future_prices(future_start_date, future_end_date)
print(f"Prediksi Harga Saham dari {future_start_date} hingga {future_end_date}:")
print(predicted_prices)