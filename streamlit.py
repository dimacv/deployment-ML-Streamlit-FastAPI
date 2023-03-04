# импортируем библиотеку streamlit
import streamlit as st
# импортируем библиотекe для работы с изображениями
from PIL import Image
# импортируем библиотеки requests и json
import requests
import json

###  Функция запуска web интерфейса
def run():
    # Загрузим из файла изображение логотипа
    image = Image.open('logo.jpeg')
    # Отобразим его в web интерфейсе
    st.sidebar.image(image)
    # Выведем надпись на боковой панели
    st.sidebar.info('Прогнозирования просрочки с использованием метода логистической регрессии.')
    st.sidebar.info('В данной реализации были использованы FastAPI и Streamlit.')
    # Зададим заголовок
    st.title("Прогнозирования просрочки:")

    # Делаем запрос входных данных через метод streamlit.number_input()
    # и заполняем соответствующие переменные аналогичные полям датафрейма
    RevolvingUtilizationOfUnsecuredLines = \
        st.number_input('Утилизация [RevolvingUtilizationOfUnsecuredLines]')
    age = st.number_input('Возраст клиента [age]', step=1)
    NumberOfTime30_59DaysPastDueNotWorse = \
        st.number_input('Количество просрочек 30-59 дней по данным БКИ [NumberOfTime30-59DaysPastDueNotWorse]',
                        step=1)
    DebtRatio = \
        st.number_input('Соотношение долга к доходу [DebtRatio]')
    MonthlyIncome = \
        st.number_input('Ежемесячный заработок [MonthlyIncome]')
    NumberOfOpenCreditLinesAndLoans = \
        st.number_input('Количество кредитов [NumberOfOpenCreditLinesAndLoans]', step=1)
    NumberOfTimes90DaysLate = \
        st.number_input('Количество просрочек 90+ по данным БКИ [NumberOfTimes90DaysLate]', step=1)
    NumberRealEstateLoansOrLines = \
        st.number_input('Количество ипотечных кредитов [NumberRealEstateLoansOrLines]', step=1)
    NumberOfTime60_89DaysPastDueNotWorse = \
        st.number_input('Количество просрочек 60-89 дней по данным БКИ [NumberOfTime60-89DaysPastDueNotWorse]', step=1)
    NumberOfDependents = st.number_input('Количество иждивенцев [NumberOfDependents]', step=1)
    output = ""

    # Создаем словарь из полученных значений
    input_dict = {'RevolvingUtilizationOfUnsecuredLines': RevolvingUtilizationOfUnsecuredLines,
                  'age': age,
                  'NumberOfTime30_59DaysPastDueNotWorse': NumberOfTime30_59DaysPastDueNotWorse,
                  'DebtRatio': DebtRatio,
                  'MonthlyIncome': MonthlyIncome,
                  'NumberOfOpenCreditLinesAndLoans': NumberOfOpenCreditLinesAndLoans,
                  'NumberOfTimes90DaysLate': NumberOfTimes90DaysLate,
                  'NumberRealEstateLoansOrLines': NumberRealEstateLoansOrLines,
                    'NumberOfTime60_89DaysPastDueNotWorse': NumberOfTime60_89DaysPastDueNotWorse,
                    'NumberOfDependents': NumberOfDependents
                  }

    # Если нажата кнопка получения прогноза
    if st.button("Predict"):

        # Посылаем POST запрос FastAPI
        response = requests.post(url=f"http://localhost:8000/predict",
                                 headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                                 data=json.dumps(input_dict))

        # Преобразуем результат в строчный формат
        output = str(response.json())

    # Выводим результат в web интерфейсе
    st.success('Вероятность просрочки: {}'.format(output))


# Вызов функции запуска web интерфейса, если данный файл не спользуется как модуль
if __name__ == '__main__':
    run()

