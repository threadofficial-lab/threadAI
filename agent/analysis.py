def summarize_dataframe(df):
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict()
    }
