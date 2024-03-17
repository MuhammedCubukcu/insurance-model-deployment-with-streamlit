# Setup Virtual Environment

```python
conda create -n insurance-env python=3.10
conda activate insurance-env
pip install -r requirements.txt
```

# Start Streamlit

```python
streamlit run your_scrip.py
```



**TARGET = 'charges'**

**FEATURES = ['age', 'sex', 'bmi', 'children', 'smoker', 'southwest', 'southeast',
    'northwest', 'northeast', 'charges']**