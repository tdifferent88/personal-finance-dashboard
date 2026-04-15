from dash import Dash, dcc, html
from data_loader import load_data
from charts import monthly_expenses_chart, category_chart

df = load_data()

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Financeiro Pessoal"),

    dcc.Graph(
        figure=monthly_expenses_chart(df)
    ),

    dcc.Graph(
        figure=category_chart(df)
    )
])

if __name__ == "__main__":
    app.run(debug=True)
