import matplotlib.pyplot as plt

def plot_numeric(df):
    df.select_dtypes("number").hist(figsize=(10, 6))
    plt.tight_layout()
    plt.show()
