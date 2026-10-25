# Midterm Terminal Commands

## Part 1: Project Setup

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

## Part 2: Business Rules

pytest -v
ruff format .
ruff check .
git add business_rules.py tests/test_business_rules.py
git commit -m "Part 2: Add bean cost function and first test"
git push

## Part 2: Bulk Discount Function

pytest -v
ruff check .