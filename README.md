# E-learning Project

INSTRUCTION: Create a elearning website using django rest framework.

## Project Setup
1. Clone Project
```bash
git clone https://github.com/Isagani-lapira/e-learning.git
```

2. Navigate to project folder and open it on VS code
```bash
cd cd e-learning
code .
```

3. Create python visual environment
```bash
py -m venv env
source env/scripts/activate
```
or
```bash
py -m venv env
source env/scripts/activate
```
4. Download all requirements
```bash
pip install -r requirements.txt
```
if error occurs you may refer to this
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Run tailwind (This is for first time running the project)
```bash
cd elearning
cd theme
cd static_src
```
6. Install necessary requirements to run tailwind
```bash
npm install
```

7. Go to the root folder (elearning folder)
8. Make migrations and migrate to update models (if any changes)
```bash
py manage.py makemigrations
py manage.py migrate
```
5. Run project
```bash
py manage.py runserver
```
