"""
Expense Tracker
A Streamlit web app for logging, browsing, and analyzing personal expenses.
Data is persisted to a local CSV file.
"""

import os
from datetime import date, datetime

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = "expenses.csv"
CATEGORIES = [
    "Food & Dining",
    "Groceries",
    "Transport",
    "Rent",
    "Utilities",
    "Shopping",
    "Entertainment",
    "Health",
    "Education",
    "Travel",
    "Other",
]
PAYMENT_METHODS = ["Cash", "Card", "UPI", "Net Banking", "Other"]
COLUMNS = ["Date", "Category", "Amount", "Payment Method", "Description"]

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------
def load_data() -> pd.DataFrame:
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    else:
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(DATA_FILE, index=False)
    return df


def save_data(df: pd.DataFrame) -> None:
    df.to_csv(DATA_FILE, index=False)


def add_expense(entry_date, category, amount, payment_method, description):
    df = load_data()
    new_row = pd.DataFrame(
        [[pd.to_datetime(entry_date), category, amount, payment_method, description]],
        columns=COLUMNS,
    )
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)


def delete_expenses(indices):
    df = load_data()
    df = df.drop(index=indices).reset_index(drop=True)
    save_data(df)


# ---------------------------------------------------------------------------
# Sidebar - Add expense + budget settings
# ---------------------------------------------------------------------------
st.sidebar.header("➕ Add New Expense")
with st.sidebar.form("add_expense_form", clear_on_submit=True):
    entry_date = st.date_input("Date", value=date.today())
    category = st.selectbox("Category", CATEGORIES)
    amount = st.number_input("Amount", min_value=0.0, step=10.0, format="%.2f")
    payment_method = st.selectbox("Payment Method", PAYMENT_METHODS)
    description = st.text_input("Description (optional)")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if amount <= 0:
            st.sidebar.error("Amount must be greater than 0.")
        else:
            add_expense(entry_date, category, amount, payment_method, description)
            st.sidebar.success("Expense added!")

st.sidebar.divider()
st.sidebar.header("🎯 Monthly Budget")
monthly_budget = st.sidebar.number_input(
    "Set a total monthly budget", min_value=0.0, step=500.0, value=0.0, format="%.2f"
)

# ---------------------------------------------------------------------------
# Main page
# ---------------------------------------------------------------------------
st.title("💰 Expense Tracker")
st.caption("Log your daily expenses and track spending patterns over time.")

data = load_data()

if data.empty:
    st.info("No expenses logged yet. Add your first expense from the sidebar!")
    st.stop()

data["Date"] = pd.to_datetime(data["Date"])

# ---- Filters -----------------------------------------------------------
with st.expander("🔍 Filters", expanded=False):
    col1, col2, col3 = st.columns(3)
    with col1:
        min_d, max_d = data["Date"].min().date(), data["Date"].max().date()
        date_range = st.date_input("Date range", value=(min_d, max_d))
    with col2:
        selected_categories = st.multiselect(
            "Category", options=sorted(data["Category"].unique()), default=None
        )
    with col3:
        selected_payment = st.multiselect(
            "Payment Method", options=sorted(data["Payment Method"].unique()), default=None
        )

filtered = data.copy()
if isinstance(date_range, tuple) and len(date_range) == 2:
    start, end = date_range
    filtered = filtered[
        (filtered["Date"] >= pd.to_datetime(start))
        & (filtered["Date"] <= pd.to_datetime(end))
    ]
if selected_categories:
    filtered = filtered[filtered["Category"].isin(selected_categories)]
if selected_payment:
    filtered = filtered[filtered["Payment Method"].isin(selected_payment)]

# ---- Key metrics ---------------------------------------------------------
total_spent = filtered["Amount"].sum()
this_month = datetime.now().strftime("%Y-%m")
month_spent = data[data["Date"].dt.strftime("%Y-%m") == this_month]["Amount"].sum()
avg_daily = (
    filtered.groupby(filtered["Date"].dt.date)["Amount"].sum().mean()
    if not filtered.empty
    else 0
)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total (filtered)", f"₹{total_spent:,.2f}")
m2.metric("This Month", f"₹{month_spent:,.2f}")
m3.metric("Avg / Active Day", f"₹{avg_daily:,.2f}")
m4.metric("Transactions", f"{len(filtered)}")

if monthly_budget > 0:
    pct = min(month_spent / monthly_budget, 1.0)
    st.progress(pct, text=f"Monthly budget used: ₹{month_spent:,.2f} / ₹{monthly_budget:,.2f}")
    if month_spent > monthly_budget:
        st.warning("You've exceeded your monthly budget!")

st.divider()

# ---- Charts ---------------------------------------------------------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("Spending by Category")
    cat_summary = filtered.groupby("Category")["Amount"].sum().reset_index()
    fig_pie = px.pie(cat_summary, names="Category", values="Amount", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with c2:
    st.subheader("Spending Over Time")
    time_summary = filtered.groupby(filtered["Date"].dt.date)["Amount"].sum().reset_index()
    fig_line = px.line(time_summary, x="Date", y="Amount", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

st.subheader("Monthly Comparison")
monthly = data.copy()
monthly["Month"] = monthly["Date"].dt.strftime("%Y-%m")
monthly_summary = monthly.groupby("Month")["Amount"].sum().reset_index()
fig_bar = px.bar(monthly_summary, x="Month", y="Amount", text_auto=".2s")
st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ---- Data table + delete ---------------------------------------------------
st.subheader("📋 Expense Records")
display_df = filtered.sort_values("Date", ascending=False).reset_index()
display_df.rename(columns={"index": "row_id"}, inplace=True)
st.dataframe(
    display_df.drop(columns=["row_id"]),
    use_container_width=True,
    hide_index=True,
)

with st.expander("🗑️ Delete a record"):
    if not display_df.empty:
        options = {
            row.row_id: f"{row.Date.date()} | {row.Category} | ₹{row.Amount:.2f} | {row.Description}"
            for row in display_df.itertuples()
        }
        to_delete = st.selectbox(
            "Select a record to delete", options=list(options.keys()), format_func=lambda x: options[x]
        )
        if st.button("Delete Selected Record"):
            delete_expenses([to_delete])
            st.success("Record deleted. Refresh to see updated data.")
            st.rerun()

st.divider()
st.download_button(
    "⬇️ Download filtered data as CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="filtered_expenses.csv",
    mime="text/csv",
)
