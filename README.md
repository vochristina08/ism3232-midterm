
# ISM3232 Midterm: Copper Kettle Coffee Roasters

- **Name:** Christina Vo
- **Version:** ZETA
- **Date:** October 25, 2026

## What This Program Does

This program helps Copper Kettle Coffee Roasters calculate coffee shipment costs and organize customer orders. It applies discounts, calculates shipping fees and determines whether orders need prepayment or a freight pallet. It also prints a shipment report with individual orders and overall totals.

## Business Rules

1. **Bean Cost:** Multiply the price per bag by the number of bags ordered.
2. **Bulk Discounts:** Orders of 20–79 bags receive a 9% discount, while orders of 80 or more bags receive 14%. Partners ordering at least 20 bags receive an additional 4% discount.
3. **Shipment Total:** Subtract the discount from the bean cost and add a $35 shipping fee if the discounted cost is below $250.
4. **Prepayment:** Orders totaling $1,500 or more require prepayment.
5. **Freight Pallets:** Orders with more than 60 bags and a total above $700 require a pallet.
6. **Shipment Reporting:** Calculate the combined shipment total, identify the largest shipment and format each shipment's details.

## How to Run

Open the terminal in the project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

Run the following commands:

```bash
ruff format .
ruff check .
pytest -v
```

I wrote 24 pytest tests to check the business rules and their boundary conditions.

## Files in This Repository

- `business_rules.py` — Contains the eight business-rule functions.
- `main.py` — Stores shipment data and prints the shipment report.
- `tests/test_business_rules.py` — Contains 24 pytest tests.
- `tests/__init__.py` — Makes the tests folder a Python package.
- `.gitignore` — Excludes virtual environment and cache files from Git.
- `requirements.txt` — Lists the project dependencies.
- `commands.md` — Records terminal commands, outputs and commit history.
- `README.md` — Explains the project and how to run and test it.

## AI Use Statement
I did not use AI for this exam.