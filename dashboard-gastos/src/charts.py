import plotly.express as px

def monthly_expenses_chart(df):
    gastos = (
        df[df["tipo"] == "Despesa"]
        .groupby("mes")["valor"]
        .sum()
        .abs()
        .reset_index()
    )

    return px.line(
        gastos,
        x="mes",
        y="valor",
        title="Gastos Mensais",
    )
def category_chart(df):
    categoria = (
        df[df["tipo"] == "Despesa"]
        .groupby("categoria")["valor"]
        .sum()
        .abs()
        .reset_index()
    )

    return px.pie(
    categoria,
    names="categoria",
    values="valor",
    title="Gastos por Categoria",
    )
