import numpy as np
import pandas as pd

np.random.seed(777)
n_bookings = 1000

data = {
    'booking_id': range(1, n_bookings + 1),
    # Статус программы лояльности пользователя Т-Банка
    'user_status': np.random.choice(['Regular', 'Pro', 'Premium'], size=n_bookings, p=[0.5, 0.3, 0.2]),
    # Длительность проживания в отелях 
    'nights': np.random.randint(1, 11, size=n_bookings),
    # Стоимость одной ночи в отеле
    'price_per_night': np.random.choice([3000, 4500, 6000, 9000, 12000], size=n_bookings, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
    # Месяц бронирования 
    'season': np.random.choice(['Низкий сезон', 'Высокий сезон (Лето)'], size=n_bookings, p=[0.4, 0.6])
}

df = pd.DataFrame(data)

df['total_booking_cost'] = df['nights'] * df['price_per_night']

df['bank_gross_revenue'] = df['total_booking_cost'] * 0.10

def calculate_cashback(row):
    base_cashback_rate = 0.03 # 3% базовый для Regular
    
    if row['user_status'] == 'Pro':
        base_cashback_rate = 0.06 # 6% для пользователей с подпиской Pro
    elif row['user_status'] == 'Premium':
        base_cashback_rate = 0.10 # 10% кэшбэка для Premium-клиентов
        
    # Корректировка на сезонность (не уверен что т-банк так делает на самом деле)
    if row['season'] == 'Выгодый сезон (Лето)':
        base_cashback_rate -= 0.01
        
    cashback_sum = row['total_booking_cost'] * base_cashback_rate
    return round(cashback_sum, 2)

df['cashback_paid'] = df.apply(calculate_cashback, axis=1)

df['bank_net_profit'] = df['bank_gross_revenue'] - df['cashback_paid']

total_turnover = df['total_booking_cost'].sum()
total_gross = df['bank_gross_revenue'].sum()
total_cashback = df['cashback_paid'].sum()
net_profit = df['bank_net_profit'].sum()
profit_margin = (net_profit / total_gross) * 100

print("====================================================")
print("🏨 СИСТЕМА МОНИТОРИНГА МАРЖИНАЛЬНОСТИ: Т-ОТЕЛИ")
print("====================================================")
print(f"🌍 Общий оборот бронирований (GMV): {total_turnover:,.0f} руб.")
print(f"💰 Валовый доход банка (Комиссия): {total_gross:,.0f} руб.")
print(f"🎫 Всего выплачено кэшбэка клиентам: {total_cashback:,.0f} руб.")
print("----------------------------------------------------")
print(f"🫐 ЧИСТАЯ ПРИБЫЛЬ СЕРВИСА Т-ОТЕЛИ: {net_profit:,.0f} руб.")
print(f"📊 Эффективная маржинальность программы: {profit_margin:.1f}%")
print("====================================================")
