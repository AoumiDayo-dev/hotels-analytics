# hotels-analytics
# 🏨 T-Hotels Analytics — Room Utilization & Cashback Optimization Engine 
###  🫐 Аналитическая платформа для сервиса Т-Отели: оптимизация кэшбэка и загрузки

[EN] An analytical data-modeling project customized for the **T-Hotels (T-Bank Travel)** vertical. It includes database DDL architectures for reservation tracking and a Python engine simulating seasonal room utilization rates and predictive cashback efficiency metrics to maximize bank ecosystem net profit.

[RU] Проект аналитического моделирования, разработанный специально под бизнес-логику вертикали **Т-Отели (Т-Путешествия)**. Включает архитектуру базы данных для трекинга бронирований и скрипт на Python, рассчитывающий коэффициенты загрузки отелей (Utilization) и чистую маржинальность кэшбэк-программ.

---

### 🛠️ Tech Stack / Стек:
* Python 3, Pandas, NumPy, Relational SQL (SQLite/PostgreSQL DDL).

---

### 🗄️ Database Architecture (Star Schema) / Архитектура DWH:
```sql
CREATE TABLE dim_hotels (hotel_id INT PRIMARY KEY, hotel_name TEXT, city TEXT, stars INT);
CREATE TABLE dim_users (user_id INT PRIMARY KEY, loyalty_status TEXT); -- Regular, Pro, Premium

CREATE TABLE fact_bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_id INT, user_id INT,
    check_in DATE, duration_nights INT,
    room_price_per_night REAL,
    cashback_paid REAL, -- Выплаченный кэшбэк
    FOREIGN KEY (hotel_id) REFERENCES dim_hotels(hotel_id),
    FOREIGN KEY (user_id) REFERENCES dim_users(user_id)
);
```
