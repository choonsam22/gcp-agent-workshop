import pandas as pd

def get_sales_by_region(region: str) -> str:
    df = pd.read_csv("sales.csv")
    row = df[df["region"] == region.lower()]
    if row.empty:
        return f"{region} 지역 데이터가 없습니다."
    value = int(row.iloc[0]["amount"])
    return f"{region} 지역 매출은 {value:,}원 입니다."
