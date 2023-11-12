# mac-ai
Sample scripts running AI on Apple Silicon

## Prerequisits
Ensure you have Python 3.9 or higher, and run the following in mac-ai root directory to setup.
```
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Scripts

Check setup
```
python is_available.py
```

Run LLaMA 2, and view resource utilization
```
/usr/bin/time -lhp python llama2.py
```

Run Mistral, and view resource utilization
```
/usr/bin/time -lhp python mistral.py
```
