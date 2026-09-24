# 💰 Expense Tracker (Streamlit)

An interactive web app for logging personal expenses and visualizing spending
habits — built with **Python, Streamlit, Pandas, and Plotly**.

## Features

- **Add expenses** — date, category, amount, payment method, description
- **CSV-backed storage** — no database setup needed, data persists locally
- **Filters** — by date range, category, and payment method
- **Dashboard metrics** — total spend, this month's spend, average daily spend
- **Budget tracking** — set a monthly budget and see a live progress bar
- **Visual analytics**
  - Pie chart — spending by category
  - Line chart — spending over time
  - Bar chart — month-over-month comparison
- **Record management** — view, delete, and export filtered records as CSV

## Tech Stack

- [Streamlit](https://streamlit.io/) — web UI
- [Pandas](https://pandas.pydata.org/) — data handling
- [Plotly Express](https://plotly.com/python/plotly-express/) — charts

## Getting Started

1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Try it with sample data by renaming `sample_expenses.csv` to
   `expenses.csv` before launching, so the dashboard isn't empty.
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Open the local URL Streamlit prints (usually `http://localhost:8501`).

## Project Structure

```
expense_tracker/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── sample_expenses.csv    # Sample data for demo purposes (optional)
└── README.md
```

## Possible Extensions

- Multi-user login and per-user data
- Switch storage from CSV to SQLite/PostgreSQL
- Recurring expense tracking
- Export reports as PDF
- Currency conversion support

## Screenshots
<img width="1917" height="913" alt="image" src="https://github.com/user-attachments/assets/cf88ad64-50c9-45ae-983f-621f6764a9e6" />
<img width="1915" height="902" alt="image" src="https://github.com/user-attachments/assets/153e5afc-a513-40a3-a376-2a4e1612543c" />
<img width="1903" height="897" alt="image" src="https://github.com/user-attachments/assets/2e7204ec-d2de-4614-af16-4c181a1d4e74" />
<img width="1910" height="906" alt="image" src="https://github.com/user-attachments/assets/de619b13-6ea5-4346-aba4-ad12e64b9627" />
<img width="1911" height="907" alt="image" src="https://github.com/user-attachments/assets/51ad1f05-fddf-4280-bf92-79ad62c282b3" />





Built as a personal portfolio project to practice Python, data manipulation,
and building interactive data apps.
