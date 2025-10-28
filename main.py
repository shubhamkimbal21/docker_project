# test_seaborn_app.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    print("🎨 Yoo Generating a sample Seaborn plot inside Docker...\n")

    # Create a small dataset
    data = pd.DataFrame({
        "Fruits": ["Apple", "Banana", "Cherry", "Mango", "Orange"],
        "Quantity": [50, 30, 40, 35, 25]
    })

    # Create a bar plot
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x="Fruits", y="Quantity", data=data, palette="coolwarm")
    ax.set_title("Fruit Quantity Chart")

    # Save the figure
    plt.savefig("fruit_chart.png")
    print("✅ Chart saved successfully as 'fruit_chart.png'")

if __name__ == "__main__":
    main()
