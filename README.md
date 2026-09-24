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

_Add a couple of screenshots here (dashboard + add-expense form) before
posting to LinkedIn/GitHub — recruiters skim visuals first._

---

Built as a personal portfolio project to practice Python, data manipulation,
and building interactive data apps.
