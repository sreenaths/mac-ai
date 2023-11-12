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

## Resource utilization

#### M1 Pro - 16 GPU Cores | Metal 3
<table>
  <tr>
    <th>Model</th>
    <th>Time (Sec)</th>
    <th>Peak memory footprint (Bytes)</th>
  </tr>
  <tr>
    <td>LLaMA 2</td>
    <td>70.50</td>
    <td>28763153984</td>
  </tr>
  <tr>
    <td>Mistral</td>
    <td>79.25</td>
    <td>21783790848</td>
  </tr>
</table>
