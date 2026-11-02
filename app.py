from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html, Input, Output


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "clean_data"


def load_data():
    orders = pd.read_csv(DATA_DIR / "orders.csv", parse_dates=["order_date"])
    details = pd.read_csv(DATA_DIR / "order_details.csv")
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    targets = pd.read_csv(DATA_DIR / "sales_targets.csv")

    sales = details.merge(orders, on="order_id", validate="many_to_one")
    sales = sales.merge(customers, on="customer_id", validate="many_to_one")
    sales = sales.merge(products, on="product_id", validate="many_to_one")
    sales["month"] = sales["order_date"].dt.strftime("%Y-%m")

    return sales, targets


sales, targets = load_data()

ALL = "__all__"


def dropdown_options(values):
    return [{"label": "Semua", "value": ALL}] + [
        {"label": str(value), "value": str(value)}
        for value in sorted(values.dropna().unique())
    ]


def filter_frame(selected_region, selected_category, selected_channel, selected_status, selected_month):
    dff = sales.copy()
    if selected_region != ALL:
        dff = dff[dff["region"] == selected_region]
    if selected_category != ALL:
        dff = dff[dff["category"] == selected_category]
    if selected_channel != ALL:
        dff = dff[dff["sales_channel"] == selected_channel]
    if selected_status != ALL:
        dff = dff[dff["order_status"] == selected_status]
    if selected_month != ALL:
        dff = dff[dff["month"] == selected_month]
    return dff


def fmt_currency(value):
    if abs(value) >= 1_000_000_000:
        return f"Rp {value / 1_000_000_000:.2f}B"
    if abs(value) >= 1_000_000:
        return f"Rp {value / 1_000_000:.1f}M"
    return f"Rp {value:,.0f}"


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Sales Analytics Dashboard"

region_values = sales["region"].dropna().unique()
category_values = sales["category"].dropna().unique()
channel_values = sales["sales_channel"].dropna().unique()
status_values = ["Completed", "Cancelled"]
month_values = sorted(sales["month"].unique())
region_coordinates = {
    "Bandung": {"lat": -6.9175, "lon": 107.6191},
    "Denpasar": {"lat": -8.6500, "lon": 115.2167},
    "Jakarta": {"lat": -6.2088, "lon": 106.8456},
    "Makassar": {"lat": -5.1477, "lon": 119.4327},
    "Medan": {"lat": 3.5952, "lon": 98.6722},
    "Semarang": {"lat": -6.9667, "lon": 110.4167},
    "Surabaya": {"lat": -7.2575, "lon": 112.7521},
}

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Sales Analytics Dashboard", className="mb-0 fw-bold dashboard-title"),
                        html.P(
                            "Executive overview • January–December 2025",
                            className="text-secondary mb-0 dashboard-subtitle",
                        ),
                    ],
                    md=3,
                    className="d-flex flex-column justify-content-center",
                ),
                dbc.Col(
                    [
                        html.Label("Region", className="filter-label"),
                        dcc.Dropdown(
                            id="filter-region",
                            options=dropdown_options(sales["region"]),
                            value=ALL,
                            clearable=False,
                        ),
                    ],
                    md=1,
                ),
                dbc.Col(
                    [
                        html.Label("Category", className="filter-label"),
                        dcc.Dropdown(
                            id="filter-category",
                            options=dropdown_options(sales["category"]),
                            value=ALL,
                            clearable=False,
                        ),
                    ],
                    md=2,
                ),
                dbc.Col(
                    [
                        html.Label("Channel", className="filter-label"),
                        dcc.Dropdown(
                            id="filter-channel",
                            options=dropdown_options(sales["sales_channel"]),
                            value=ALL,
                            clearable=False,
                        ),
                    ],
                    md=2,
                ),
                dbc.Col(
                    [
                        html.Label("Status", className="filter-label"),
                        dcc.Dropdown(
                            id="filter-status",
                            options=dropdown_options(pd.Series(status_values)),
                            value="Completed",
                            clearable=False,
                        ),
                    ],
                    md=2,
                ),
                dbc.Col(
                    [
                        html.Label("Month", className="filter-label"),
                        dcc.Dropdown(
                            id="filter-month",
                            options=dropdown_options(sales["month"]),
                            value=ALL,
                            clearable=False,
                        ),
                    ],
                    md=2,
                ),
            ],
            className="g-2 mb-2 align-items-end header-row",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(id="kpi-revenue", className="kpi-card"), md=2),
                dbc.Col(html.Div(id="kpi-profit", className="kpi-card"), md=2),
                dbc.Col(html.Div(id="kpi-margin", className="kpi-card"), md=2),
                dbc.Col(html.Div(id="kpi-orders", className="kpi-card"), md=2),
                dbc.Col(html.Div(id="kpi-target", className="kpi-card"), md=4),
            ],
            className="g-2 mb-2",
        ),
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Span("KEY INSIGHTS  ", className="insight-heading"),
                                html.Span(id="insights", className="insight-inline"),
                            ],
                            md=8,
                        ),
                        dbc.Col(
                            [
                                html.Span("ACTION  ", className="action-heading"),
                                html.Span(id="recommendations", className="action-inline"),
                            ],
                            md=4,
                        ),
                    ],
                    className="align-items-center g-2",
                ),
                className="py-2",
            ),
            className="insight-banner mb-2",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card([dbc.CardHeader("Revenue Trend vs Target"), dbc.CardBody(dcc.Graph(id="graph-trend", config={"displayModeBar": False}, style={"height": "180px"}))], className="chart-card"), md=4),
                dbc.Col(dbc.Card([dbc.CardHeader("Revenue Distribution Map"), dbc.CardBody(dcc.Graph(id="graph-region", config={"displayModeBar": False}, style={"height": "180px"}))], className="chart-card"), md=4),
                dbc.Col(dbc.Card([dbc.CardHeader("Regional Target Achievement"), dbc.CardBody(dcc.Graph(id="graph-target", config={"displayModeBar": False}, style={"height": "180px"}))], className="chart-card"), md=4),
            ],
            className="g-2 mb-2",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card([dbc.CardHeader("Top 10 Product Revenue Tree"), dbc.CardBody(dcc.Graph(id="graph-products", config={"displayModeBar": False}, style={"height": "180px"}))], className="chart-card"), md=6),
                dbc.Col(dbc.Card([dbc.CardHeader("Channel Revenue & Margin"), dbc.CardBody(dcc.Graph(id="graph-channel", config={"displayModeBar": False}, style={"height": "180px"}))], className="chart-card"), md=6),
            ],
            className="g-3",
        ),
    ],
    fluid=True,
)


@app.callback(
    [
        Output("kpi-revenue", "children"),
        Output("kpi-profit", "children"),
        Output("kpi-margin", "children"),
        Output("kpi-orders", "children"),
        Output("kpi-target", "children"),
        Output("graph-trend", "figure"),
        Output("graph-region", "figure"),
        Output("graph-products", "figure"),
        Output("graph-channel", "figure"),
        Output("graph-target", "figure"),
        Output("insights", "children"),
        Output("recommendations", "children"),
    ],
    [
        Input("filter-region", "value"),
        Input("filter-category", "value"),
        Input("filter-channel", "value"),
        Input("filter-status", "value"),
        Input("filter-month", "value"),
    ],
)
def update_dashboard(region_filter, category_filter, channel_filter, status_filter, month_filter):
    region_filter = region_filter or ALL
    category_filter = category_filter or ALL
    channel_filter = channel_filter or ALL
    status_filter = status_filter or ALL
    month_filter = month_filter or ALL

    dff = filter_frame(region_filter, category_filter, channel_filter, status_filter, month_filter)

    revenue = float(dff["revenue"].sum()) if not dff.empty else 0.0
    profit = float(dff["profit"].sum()) if not dff.empty else 0.0
    margin = profit / revenue if revenue else 0.0
    unique_orders = dff["order_id"].nunique()

    target_region = list(region_values) if region_filter == ALL else [region_filter]
    target_month = list(month_values) if month_filter == ALL else [month_filter]
    target_frame = targets[
        targets["region"].isin(target_region)
        & targets["month"].isin(target_month)
    ]
    target_revenue = float(target_frame["target_revenue"].sum())
    achievement = revenue / target_revenue if target_revenue else 0.0

    kpi_card = lambda label, value, accent="#6558d9": html.Div(
        [
            html.Div(label, className="label"),
            html.Div(value, className="value"),
        ],
        style={"borderLeftColor": accent},
    )

    def empty_fig(title):
        return {
            "layout": {
                "title": title,
                "annotations": [{"text": "Tidak ada data untuk filter ini", "showarrow": False}],
                "height": 180,
            }
        }

    trend_fig = empty_fig("Monthly Revenue vs Target")
    region_fig = empty_fig("Revenue by Region")
    product_fig = empty_fig("Top 10 Products")
    channel_fig = empty_fig("Sales Channel Performance")
    target_fig = empty_fig("Sales vs Target Matrix")

    insights = []
    recommendations = []

    if not dff.empty:
        monthly = dff.groupby("month", as_index=False)["revenue"].sum().sort_values("month")
        monthly_target = target_frame.groupby("month", as_index=False)["target_revenue"].sum()
        monthly = monthly.merge(monthly_target, on="month", how="left")
        monthly["target_revenue"] = monthly["target_revenue"].fillna(0)

        trend_fig = go.Figure()
        trend_fig.add_scatter(x=monthly["month"], y=monthly["target_revenue"], name="Target",
                              mode="lines+markers", line=dict(color="#ff8a65", width=3))
        trend_fig.add_scatter(
            x=monthly["month"],
            y=monthly["revenue"],
            name="Revenue",
            mode="lines+markers",
            line=dict(color="#6558d9", width=2.5),
            fill="tozeroy",
            fillcolor="rgba(101, 88, 217, 0.14)",
            marker=dict(size=6),
        )
        trend_fig.update_layout(height=180, margin=dict(l=10, r=10, t=8, b=5),
                                legend=dict(orientation="h", y=1.08), paper_bgcolor="white",
                                plot_bgcolor="white")
        trend_fig.update_yaxes(tickprefix="Rp ", tickformat=".3s", gridcolor="#edf1f7")

        region_frame = dff.groupby("region", as_index=False)["revenue"].sum()
        region_frame["lat"] = region_frame["region"].map(
            lambda region: region_coordinates.get(region, {}).get("lat")
        )
        region_frame["lon"] = region_frame["region"].map(
            lambda region: region_coordinates.get(region, {}).get("lon")
        )
        region_frame = region_frame.dropna(subset=["lat", "lon"])

        region_fig = go.Figure(go.Scattergeo(
            lat=region_frame["lat"],
            lon=region_frame["lon"],
            mode="markers+text",
            text=region_frame["region"],
            textposition="top center",
            marker=dict(
                size=(region_frame["revenue"] / region_frame["revenue"].max() * 26).clip(lower=8),
                color=region_frame["revenue"],
                colorscale=[[0, "#b9c2ff"], [1, "#6558d9"]],
                cmin=region_frame["revenue"].min(),
                cmax=region_frame["revenue"].max(),
                line=dict(width=1, color="white"),
                showscale=False,
            ),
            customdata=region_frame[["revenue"]],
            hovertemplate="<b>%{text}</b><br>Revenue: Rp %{customdata[0]:,.0f}<extra></extra>",
        ))
        region_fig.update_geos(
            scope="asia",
            showland=True,
            landcolor="#f2f4f8",
            showocean=True,
            oceancolor="#eef4fa",
            showcountries=True,
            countrycolor="#d8dee8",
            lataxis_range=[-11, 7],
            lonaxis_range=[94, 141],
            projection_type="natural earth",
        )
        region_fig.update_layout(
            height=180,
            margin=dict(l=5, r=5, t=5, b=5),
            paper_bgcolor="white",
            plot_bgcolor="white",
            geo=dict(bgcolor="white"),
        )

        product_frame = dff.groupby("product_name", as_index=False)["revenue"].sum()
        product_frame = product_frame.sort_values("revenue", ascending=False).head(10)
        product_fig = go.Figure(go.Treemap(
            labels=product_frame["product_name"],
            parents=["Top 10"] * len(product_frame),
            values=product_frame["revenue"],
            texttemplate="<b>%{label}</b><br>%{value:,.0f}",
            textfont=dict(size=10),
            marker=dict(
                colors=product_frame["revenue"],
                colorscale=["#dfe7ff", "#6558d9"],
                showscale=False,
            ),
            hovertemplate="<b>%{label}</b><br>Revenue: Rp %{value:,.0f}<extra></extra>",
        ))
        product_fig.update_layout(height=180, margin=dict(l=10, r=10, t=8, b=5),
                                  paper_bgcolor="white", plot_bgcolor="white")
        product_fig.update_traces(root_color="#f8f9fb")

        channel_frame = dff.groupby("sales_channel", as_index=False).agg(
            revenue=("revenue", "sum"), profit=("profit", "sum")
        )
        channel_frame["margin"] = channel_frame["profit"] / channel_frame["revenue"]
        channel_fig = go.Figure(go.Scatter(
            x=channel_frame["revenue"],
            y=channel_frame["margin"],
            mode="markers+text",
            text=channel_frame["sales_channel"],
            textposition="top center",
            marker=dict(
                size=channel_frame["profit"].clip(lower=0).pow(0.38) / 1.6,
                sizemode="diameter",
                sizemin=10,
                color=channel_frame["margin"],
                colorscale=["#ffb4a2", "#6558d9"],
                showscale=False,
            ),
            hovertemplate="<b>%{text}</b><br>Revenue: Rp %{x:,.0f}<br>Margin: %{y:.1%}<extra></extra>",
        ))
        channel_fig.update_layout(height=180, margin=dict(l=10, r=10, t=8, b=5),
                                  paper_bgcolor="white", plot_bgcolor="white")
        channel_fig.update_xaxes(tickprefix="Rp ", tickformat=".3s", gridcolor="#edf1f7")
        channel_fig.update_yaxes(tickformat=".0%", gridcolor="#edf1f7",
                                 range=[0, max(0.4, channel_frame["margin"].max() * 1.25)])

        actual_region = dff.groupby("region", as_index=False)["revenue"].sum()
        region_target = target_frame.groupby("region", as_index=False)["target_revenue"].sum()
        target_matrix = actual_region.merge(region_target, on="region", how="left")
        target_matrix["target_revenue"] = target_matrix["target_revenue"].fillna(0)
        target_matrix["achievement"] = target_matrix["revenue"] / target_matrix["target_revenue"].replace(0, pd.NA)
        target_matrix["achievement"] = target_matrix["achievement"].fillna(0).sort_values()
        target_matrix = target_matrix.sort_values("achievement", ascending=False)
        target_fig = go.Figure(go.Heatmap(
            z=[target_matrix["achievement"].tolist()],
            x=target_matrix["region"].tolist(),
            zmin=0,
            zmax=max(1, target_matrix["achievement"].max()),
            colorscale=[
                [0, "#ffd6cc"],
                [0.5, "#ffb4a2"],
                [0.799, "#cfc9ff"],
                [1, "#6558d9"],
            ],
            text=[[f"{value:.1%}" for value in target_matrix["achievement"].tolist()]],
            texttemplate="%{text}",
            textfont=dict(size=9, color="#344054"),
            hovertemplate="<b>%{x}</b><br>Achievement: %{z:.1%}<extra></extra>",
            showscale=False,
        ))
        target_fig.update_layout(height=180, margin=dict(l=10, r=10, t=8, b=5),
                                 paper_bgcolor="white", plot_bgcolor="white",
                                 yaxis=dict(visible=False))
        target_fig.update_xaxes(side="bottom", tickfont=dict(size=9), showgrid=False)

        best_month = monthly.loc[monthly["revenue"].idxmax()]
        best_region = region_frame.sort_values("revenue", ascending=False).iloc[0]
        best_product = product_frame.sort_values("revenue", ascending=False).iloc[0]
        best_channel = channel_frame.sort_values("margin", ascending=False).iloc[0]

        insights = [
            f"{best_month['month']} mencatat revenue tertinggi: {fmt_currency(best_month['revenue'])}.",
            f"{best_region['region']} adalah region teratas.",
            f"{best_product['product_name']} adalah produk teratas.",
            f"{best_channel['sales_channel']} memiliki margin tertinggi ({best_channel['margin']:.1%}).",
        ]

        recommendations = [
            "Perkuat campaign region dan channel yang memiliki margin tinggi, bukan hanya revenue terbesar.",
            "Tinjau produk dengan diskon tinggi untuk memastikan kontribusinya tetap menghasilkan profit.",
            "Gunakan tren bulanan untuk mengalokasikan stok dan promosi menjelang periode puncak.",
        ]

    insight_text = " • ".join(insights[:4]) if insights else "Tidak ada insight untuk filter ini."
    recommendation_text = " • ".join(recommendations[:2]) if recommendations else "Tidak ada rekomendasi untuk filter ini."

    return (
        kpi_card("Total Revenue", fmt_currency(revenue)),
        kpi_card("Total Profit", fmt_currency(profit)),
        kpi_card("Profit Margin", f"{margin:.1%}", "#26a69a"),
        kpi_card("Unique Orders", f"{unique_orders:,}", "#42a5f5"),
        kpi_card("Target Achievement", f"{achievement:.1%} • {fmt_currency(revenue)} / {fmt_currency(target_revenue)}", "#ff8a65"),
        trend_fig,
        region_fig,
        product_fig,
        channel_fig,
        target_fig,
        insight_text,
        recommendation_text,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8050, host="127.0.0.1")
