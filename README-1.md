# Sales Data Analysis — Test Cases

## Overview
This Python script tests a sales-data analysis program using four test cases. Each test case creates a temporary CSV file, loads the data with **pandas**, performs calculations, prints the results, and removes the temporary file. The fourth test case also creates charts using **matplotlib**.

## Requirements
Install the required Python libraries:

```bash
pip install pandas matplotlib
```

Python 3 is required.

## How to Run
1. Save the test script as `test_sales.py`.
2. Open a terminal or command prompt in the same folder.
3. Run:

   ```bash
   python test_sales.py
   ```

4. Press **Enter** when prompted to execute each test case.
5. In Test Case 4, a chart window will open. Close it to allow the script to continue.

## Test Cases

### Test Case 1: Normal Input
**Purpose:** Verify that the program calculates summary totals for a valid dataset.

**Input data:**

| Date | Product | Region | Quantity | Amount |
|---|---|---|---:|---:|
| 2026-08-01 | Laptop | North | 2 | 100000 |
| 2026-08-02 | Mouse | South | 10 | 5000 |
| 2026-08-03 | Laptop | South | 1 | 50000 |

**Expected output:**
```text
Total Revenue: 155000 | Transactions: 3 | Units sold: 13
```

### Test Case 2: Boundary / Minimum Input
**Purpose:** Check that the calculations work with only one valid transaction.

**Input data:**

| Date | Product | Region | Quantity | Amount |
|---|---|---|---:|---:|
| 2026-08-01 | Mouse | North | 1 | 500 |

**Expected output:**
```text
Total Revenue: 500 | Transactions: 1 | Top product: Mouse
```

### Test Case 3: Invalid Input
**Purpose:** Verify that a row with a non-numeric amount is skipped.

**Input data:**

| Date | Product | Region | Quantity | Amount |
|---|---|---|---:|---|
| 2026-08-01 | Laptop | North | 2 | 100000 |
| 2026-08-02 | Mouse | South | 10 | abc |
| 2026-08-03 | Laptop | South | 1 | 50000 |

**Expected output:**
```text
Row 2 skipped: invalid Amount 'abc'
Total Revenue: 150000 | Transactions: 2
```

### Test Case 4: Product-wise and Region-wise Sales
**Purpose:** Calculate sales grouped by product and region, then display charts.

**Expected text output:**
```text
Laptop: 150000 | Mouse: 5000
North: 100000 | South: 55000
Bar chart 'Region-wise Sales' displayed
```

**Charts displayed:**
- **Region-wise Sales:** A bar chart comparing total sales in each region.
- **Product-wise Sales Trend:** A line chart comparing total sales by product. This chart shows grouped totals, not sales over time.

## Expected Results Summary

| Test case | Main check | Expected result |
|---|---|---|
| 1 | Normal summary | Revenue = 155000; 3 transactions; 13 units |
| 2 | Single-row dataset | Revenue = 500; 1 transaction; top product = Mouse |
| 3 | Invalid amount | Invalid row skipped; revenue = 150000; 2 valid transactions |
| 4 | Grouped sales and charts | Laptop = 150000; Mouse = 5000; North = 100000; South = 55000 |

## Notes
- CSV files are created in the current working directory and deleted after each test case.
- The script pauses for Enter before each test case.
- Test Case 3 validates numeric `Amount` and `Quantity` values and skips rows that raise a conversion error.
- The message saying the bar chart is displayed is printed before the charts are actually shown.
- The line chart is grouped by product, so it is a product comparison rather than a date-based trend.
