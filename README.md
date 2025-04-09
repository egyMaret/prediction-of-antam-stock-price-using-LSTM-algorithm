# 📈 Prediction of Antam Stock Price Using LSTM Algorithm

## 📌 **Brief Description**
Stocks are an important factor in a country's economy, especially in the financial sector. However, volatile stock movements are often a challenge for investors to make the right investment decisions.

This research aims to predict **the closing price of PT Aneka Tambang Tbk (ANTM)** shares using **Long Short-Term Memory (LSTM)** which has the ability to remember long-term patterns in *time series* data.

---

## 🔍 **Background**
- Based on data from the **Indonesia Stock Exchange (IDX)** as of September 25, 2024, there are **more than 6 million investors** in Indonesia.
- Accurate stock price prediction can help investors in making investment decisions.
- The **LSTM** model was chosen because it has proven to be effective in handling **time series data** and studying stock movement patterns.

---

## 📊 **Dataset**
- **Data Source**: Share price of PT Aneka Tambang Tbk (ANTM)
- **Time Range**: September 1, 2019 - September 1, 2024  
- **Data used**: Closing price (*Close Price*)

---

## 🛠️ **Research Methods**
Models were built using **LSTM** with several architectural configurations to find the best performance:
1. **Number of Hidden Layers**: 2, 3, 4, and 5
2. **Optimizer**: Adam, Adagrad, and Adadelta  
3. **Number of Epochs**: 50, 100, 150, and 200  

**Processing:**
1. **Data preprocessing**: Normalization, division of training and testing data.  
2. **Training Model**: Using the configured LSTM architecture.  
3. **Model Evaluation**: Using **Root Mean Squared Error (RMSE)**.  

---

## 📘 LSTM
LSTM was first introduced by Hochreiter and Schmidhuber in 1997, many studies have used LSTM for various cases of sequential data such as, speech recognition and predicting machine errors. LSTM is a type of RNN that has the ability to remember long term and short term for time series data. The LSTM architecture is specifically designed to avoid the vanishing gradient problem, which most often occurs when we use RNNs.

LSTM has 3 gates, namely, forget gate which functions to decide which information needs to be discarded or remembered from the cell state, continue to the input gate which functions to regulate what new information will be added to the cell state, finally the output gate with a function to determine which part of the cell state will be issued as output.

<p align="center">
  <img src="https://github.com/user-attachments/assets/f365bdeb-588a-4329-9dc1-414f0b205608" alt="Deskripsi Gambar" width="500">
</p>

## 📙 ANTAM
Aneka Tambang or commonly abbreviated to Antam, is part of MIND ID that is primarily engaged in nickel, bauxite and gold mining. To support its business activities, by the end of 2021, the company also has 15 gold boutiques located in 11 cities in Indonesia.

The company began its history in 1968 as a state company (PN) under the name PN Aneka Tambang established by the Indonesian government as a result of the merger of PN Tambang Bauksit Indonesia, PN Tambang Emas Tjikotok, PN Logam Mulia, PT Nikel Indonesia, South Kalimantan Diamond Mine Project, and ex-Bappetamb projects. In 1974, the company's status was changed to a state-owned company. In 1976, the company began commercial operation of the FeNi I Plant in Pomalaa, and three years later, the company also began operating a nickel mine on Gebe Island. In 1994, the company started operating a gold mine in Pongkor, and a year later, it also started operating the FeNi II Plant in Pomalaa commercially. On November 27, 1997, the company was officially listed on the Jakarta Stock Exchange and Surabaya Stock Exchange. A year later, the company also began operating a nickel mine on Gee Island.

---

## 🎯 **Research Results**
From all the experiments conducted, the best model was obtained with the following configuration:
- **Architecture**: 2 Hidden Layers  
- **Optimizer**: Adam  
- **Epoch**: 100  
- **RMSE Value (Testing)**: **37.133**  

<p align="center">
  <img src="https://github.com/user-attachments/assets/8754bb4a-488c-4887-bc3f-dd6ab4e71155" alt="Grafik Prediksi Saham" width="500">
</p>

This model successfully learns the movement pattern of ANTM stock and provides optimal prediction results.

---

## 🧑‍💻 **model utilization**
how to use the best model to predict the next few days with python language, can use the file **main.py**.

Here are the results when running the **main.py** code in predicting the next few days, starting from 02-09-2024 to 06-09-2024

```
WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 366ms/step
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 33ms/step
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 33ms/step
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 28ms/step
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 31ms/step
Prediksi Harga Saham dari 2024-09-02 hingga 2024-09-06:
Ticker          ANTM.JK
2024-09-02  1405.019902
2024-09-03  1406.166716
2024-09-04  1406.398620
2024-09-05  1406.636537
2024-09-06  1406.802461
```

**comparison with actual data**
```
Price	Adj Close	Close	High	Low	Open	Volume
Ticker	ANTM.JK	ANTM.JK	ANTM.JK	ANTM.JK	ANTM.JK	ANTM.JK
Date						
2024-09-02	1395.0	1395.0	1415.0	1385.0	1400.0	116937200
2024-09-03	1370.0	1370.0	1405.0	1365.0	1400.0	87618500
2024-09-04	1345.0	1345.0	1370.0	1340.0	1350.0	98870900
2024-09-05	1345.0	1345.0	1370.0	1330.0	1350.0	106245300
2024-09-06	1335.0	1335.0	1360.0	1330.0	1345.0	77347000
```

all code and experiments can be seen on [my Colab](https://colab.research.google.com/drive/1M92XWuuRHfnMYtsSSzXroECyxSi1uJ1m?usp=sharing)

---

## 📞 **Contact**
- **Name**: Egy Maretiano
- **LinkedIn**: [Egy Maret](http://www.linkedin.com/in/egy-maretiano-9488b7337?authuser=0)  
- **Email**: emaretiano@gmail.com

---

**⭐ Don't forget to star this repository if you find it interesting and useful! ⭐**
