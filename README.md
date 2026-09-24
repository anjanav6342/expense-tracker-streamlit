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
<img width="1903" height="912" alt="image" src="https://github.com/user-attachments/assets/ab970b5f-d877-485e-aa41-a50a21230cf3" />
<img width="1917" height="837" alt="image" src="https://github.com/user-attachments/assets/19b117e3-7259-4111-8018-e441fda44fdc" />
<img width="1917" height="837" alt="image" src="https://github.com/user-attachments/assets/c5fc9e8b-2e5a-40bb-b592-35115f99efe4" />
<img width="1905" height="912" alt="image" src="https://github.com/user-attachments/assets/0c896c83-6e90-4cd4-ac0f-e6f1f7e2320a" />






Built as a personal portfolio project to practice Python, data manipulation,
and building interactive data apps.
