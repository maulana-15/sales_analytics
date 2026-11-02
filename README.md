# Sales Analytics Dashboard

Interactive web dashboard built from the Sales Analytics portfolio dataset.

## Run

```powershell
cd "D:\portfolio DA\pack 1\01_sales_analytics"
python -m pip install -r requirements.txt
python app.py
```

Buka dashboard di `http://127.0.0.1:8050`.

The dashboard provides filters for order status, region, sales channel, product category, and month. All KPI cards, charts, and insights update based on the active selection.

## Data

- `clean_data/customers.csv`
- `clean_data/products.csv`
- `clean_data/orders.csv`
- `clean_data/order_details.csv`
- `clean_data/sales_targets.csv`

## Analysis

The application calculates:

- Total revenue and profit
- Profit margin
- Unique completed or selected orders
- Monthly revenue versus target
- Revenue by region
- Top 10 products
- Profitability by sales channel
- Sales-versus-target achievement by region
