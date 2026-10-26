# Terminal Record: Copper Kettle Coffee Roasters

## 1. Building the project

'''bash
mkdir ism3232-midterm
cd ~/ism3232-midterm
git init
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
printf '.venv/\n__pycache__/\n' > .gitignore
mkdir tests
touch business_rules.py main.py tests/__init__.py tests/test_business_rules.py
touch commands.md README.md
tree -L 2
git remote add origin https://github.com/vochristina08/ism3232-midterm.git
git add .
git commit -m "Part 1: Set up project structure and dependencies"
git push -u origin main
'''

## 2. The virtual environment

```bash
which python3
```

```text
/Users/christinavo/ism3232-midterm/.venv/bin/python3
```

The output shows that the virtual environment is active because Python is running from the `.venv/bin/` folder inside my project.

## 3. The project structure

```bash
tree -L 2
```

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The `__pycache__` folder is on my computer but not in my GitHub repository because it contains automatically generated Python cache files that are excluded by `.gitignore`.

## 4. Every function and test

```bash
rg 'def '
```

```text
business_rules.py
12:def calculate_bean_cost(bag_price: float, bags: int) -> float:
16:def get_bulk_discount(bags: int, partner: bool = False) -> float:
31:def calculate_shipment_total(
44:def requires_prepayment(total: float) -> bool:
48:def needs_pallet(bags: int, total: float) -> bool:
52:def total_shipped(shipments: list) -> float:
65:def largest_shipment(shipments: list) -> str:
83:def format_shipment_line(

tests/test_business_rules.py
13:def test_bean_cost():
16:def test_bulk_discount_below_20():
19:def test_bulk_discount_at_20():
22:def test_large_discount_below_80():
25:def test_large_discount_at_80():
28:def test_partner_discount_changes_result():
32:def test_shipment_total_with_shipping_fee():
35:def test_shipping_fee_below_250():
38:def test_no_shipping_fee_at_250():
41:def test_shipment_total_with_bulk_discount():
44:def test_prepayment_below_1500():
47:def test_prepayment_at_1500():
51:def test_pallet_at_60_bags():
54:def test_pallet_above_60_bags():
57:def test_pallet_at_700_total():
60:def test_pallet_above_700_total():
64:def test_total_shipped_with_two_shipments():
71:def test_total_shipped_empty_list():
74:def test_largest_shipment_with_two_buyers():
81:def test_largest_shipment_tie():
88:def test_largest_shipment_empty_list():
91:def test_format_shipment_line_no_flags():
96:def test_format_shipment_line_both_flags():
101:def test_format_shipment_line_one_flag():
```

The `business_rules.py` file defines 8 functions, and `tests/test_business_rules.py` defines 24 tests.

## 5. Which files print

```bash
rg -l 'print'
```

```text
commands.md
main.py
```

The Python file `main.py` prints the shipment report, while `business_rules.py` does not appear because its functions return values instead of printing them.


## 6. The commit history

```bash
git log --oneline
```

```text
70f53d4 (HEAD -> main, origin/main) Part 4: Add 24 pytest tests for business rules
c8b4f4c Part 3: Complete shipment report and summary calculations
eb57099 Part 2: Add total_shipped, largest_shipment, format_shipment_line, and tests
071d428 Part 2: Add freight pallet requirement and tests
6791306 Part 2: Add prepayment requirement and tests
4201c8d Part 2: Add shipment total function and tests
631fba8 Part 2: Add bulk discount function and tests
f5ff618 Part 2: Add bean cost function and first test
ab7c92d Part 1: Set up project structure and dependencies
```

There were 9 commits at the time I ran `git log --oneline`.