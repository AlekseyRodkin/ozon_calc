import streamlit as st

st.title("📦 Калькулятор выгоды досрочного вывода средств с Ozon")

# Входные параметры
margin = st.number_input("Маржинальность за цикл (%)", value=20.0, min_value=0.0, step=0.5)
cycle_weeks = st.number_input("Длительность одного цикла (в неделях)", value=8, min_value=1)
capital_cost_month = st.number_input("Стоимость капитала (% в месяц)", value=3.0, min_value=0.0, step=0.1)
early_withdraw_fee = st.number_input("Комиссия за досрочный вывод (%)", value=2.5, min_value=0.0, step=0.1)
time_saved = st.number_input("Экономия времени на цикл (в неделях)", value=3, min_value=1)

# Расчёты
capital_cost_week = capital_cost_month / 4
capital_cost_period = capital_cost_week * time_saved
extra_fee = early_withdraw_fee - capital_cost_period

cycles_per_year_old = int(52 / cycle_weeks)
profit_old = cycles_per_year_old * margin

new_cycle_weeks = cycle_weeks - time_saved
if new_cycle_weeks <= 0:
    st.error("Новый цикл не может быть меньше или равен 0 неделям.")
else:
    cycles_per_year_new = int(52 / new_cycle_weeks)
    profit_per_cycle_new = margin - extra_fee
    profit_new = cycles_per_year_new * profit_per_cycle_new

    # Вывод
    st.markdown("---")
    st.subheader("📊 Результаты")
    st.write(f"Чистая переплата за досрочный вывод: **{extra_fee:.2f}%**")
    st.write(f"Годовая доходность без досрочности: **{profit_old:.2f}%**")
    st.write(f"Годовая доходность с досрочностью: **{profit_new:.2f}%**")
    if profit_new > profit_old:
        st.success("✅ Досрочный вывод выгоден!")
    else:
        st.warning("⚠️ Досрочный вывод не даёт выгоды в текущей конфигурации.")
