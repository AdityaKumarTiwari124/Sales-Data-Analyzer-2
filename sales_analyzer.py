import os
import pandas as pd
import matplotlib.pyplot as plt

def run_test_case_1():
    print("\n" + "="*50)
    print("TEST CASE 1: Normal Input")
    print("="*50)
    
    # 1. Create CSV data for Test Case 1
    csv_data = """2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,5000
2026-08-03,Laptop,South,1,50000"""
    
    filename = "sales_tc1.csv"
    with open(filename, "w") as f:
        f.write(csv_data.strip())
        
    # 2. Load and process data (Menu option 1 - Summary)
    df = pd.read_csv(filename, names=["Date", "Product", "Region", "Quantity", "Amount"])
    
    total_revenue = df["Amount"].sum()
    total_transactions = len(df)
    total_units = df["Quantity"].sum()
    
    # Print expected output
    print(f"Total Revenue: {total_revenue} | Transactions: {total_transactions} | Units sold: {total_units}")
    
    # Clean up the file
    os.remove(filename)


def run_test_case_2():
    print("\n" + "="*50)
    print("TEST CASE 2: Boundary / Minimum Input")
    print("="*50)
    
    # 1. Create CSV data for Test Case 2 (Only 1 row)
    csv_data = """2026-08-01,Mouse,North,1,500"""
    
    filename = "sales_tc2.csv"
    with open(filename, "w") as f:
        f.write(csv_data.strip())
        
    # 2. Process data (Menu option 1 - Summary)
    df = pd.read_csv(filename, names=["Date", "Product", "Region", "Quantity", "Amount"])
    
    total_revenue = df["Amount"].sum()
    total_transactions = len(df)
    top_product = df.groupby("Product")["Quantity"].sum().idxmax()
    
    # Print expected output
    print(f"Total Revenue: {total_revenue} | Transactions: {total_transactions} | Top product: {top_product}")
    
    # Clean up the file
    os.remove(filename)


def run_test_case_3():
    print("\n" + "="*50)
    print("TEST CASE 3: Invalid Input")
    print("="*50)
    
    # 1. Create CSV data for Test Case 3 (Contains 'abc' as invalid amount)
    csv_data = """2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,abc
2026-08-03,Laptop,South,1,50000"""
    
    filename = "sales_tc3.csv"
    with open(filename, "w") as f:
        f.write(csv_data.strip())
        
    # 2. Process data and check for invalid rows
    df = pd.read_csv(filename, names=["Date", "Product", "Region", "Quantity", "Amount"])
    
    cleaned_rows = []
    for idx, row in df.iterrows():
        try:
            # Check if Amount and Quantity are numbers
            amt = pd.to_numeric(row["Amount"])
            qty = pd.to_numeric(row["Quantity"])
            if pd.isna(amt) or pd.isna(qty):
                raise ValueError
            cleaned_rows.append(row)
        except ValueError:
            # Print skip message for invalid row as per assignment
            print(f"Row {idx+1} skipped: invalid Amount '{row['Amount']}'")
            
    df_clean = pd.DataFrame(cleaned_rows)
    df_clean["Amount"] = pd.to_numeric(df_clean["Amount"])
    
    total_revenue = df_clean["Amount"].sum()
    total_transactions = len(df_clean)
    
    # Print expected output
    print(f"Total Revenue: {total_revenue} | Transactions: {total_transactions}")
    
    # Clean up the file
    os.remove(filename)


def run_test_case_4():
    print("\n" + "="*50)
    print("TEST CASE 4: Different Valid Scenario")
    print("="*50)
    
    # 1. Create CSV data for Test Case 4 (Same dataset as Test Case 1)
    csv_data = """2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,5000
2026-08-03,Laptop,South,1,50000"""
    
    filename = "sales_tc4.csv"
    with open(filename, "w") as f:
        f.write(csv_data.strip())
        
    # 2. Process data (Menu option 2 - Group by Product & Region)
    df = pd.read_csv(filename, names=["Date", "Product", "Region", "Quantity", "Amount"])
    
    product_sales = df.groupby("Product")["Amount"].sum()
    region_sales = df.groupby("Region")["Amount"].sum()
    
    # Display product-wise output
    prod_out = " | ".join([f"{p}: {a}" for p, a in product_sales.items()])
    print(prod_out)
    
    # Display region-wise output
    reg_out = " | ".join([f"{r}: {a}" for r, a in region_sales.items()])
    print(reg_out)
    
    print("Bar chart 'Region-wise Sales' displayed")
    
    # --- Generate Charts ---
    plt.figure(figsize=(10, 4))
    
    # 1. Bar Chart (Region-wise Sales)
    plt.subplot(1, 2, 1)
    region_sales.plot(kind="bar", color=["skyblue", "salmon"])
    plt.title("Region-wise Sales")
    plt.xlabel("Region")
    plt.ylabel("Amount")
    
    # 2. Line Chart (To meet minimum assignment requirements)
    plt.subplot(1, 2, 2)
    product_sales.plot(kind="line", marker="o", color="green")
    plt.title("Product-wise Sales Trend")
    plt.xlabel("Product")
    plt.ylabel("Amount")
    
    plt.tight_layout()
    plt.show()
    
    # Clean up the file
    os.remove(filename)


if __name__ == "__main__":
    print("STARTING TEST CASES...")
    
    input("\nPress Enter to run TEST CASE 1...")
    run_test_case_1()
    
    input("\nPress Enter to run TEST CASE 2...")
    run_test_case_2()
    
    input("\nPress Enter to run TEST CASE 3...")
    run_test_case_3()
    
    input("\nPress Enter to run TEST CASE 4...")
    run_test_case_4()
    
    print("\n" + "="*50)
    print("ALL TEST CASES EXECUTED SUCCESSFULLY!")
    print("="*50)