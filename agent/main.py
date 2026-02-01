from loader import load_data
from analysis import summarize_dataframe
from visualize import plot_numeric
from llm import ask_llm

df = load_data("data.csv")

summary = summarize_dataframe(df)
print("DATA SUMMARY:", summary)

insight = ask_llm(f"Analyze this data summary: {summary}")
print("LLM INSIGHTS:", insight)

plot_numeric(df)
