import subprocess
import sys

def test_compra():
    result = subprocess.run([sys.executable, 'main.py'], input='200\n25\n', text=True, capture_output=True)
    
    assert result.returncode == 0
    
    assert "Precio con descuento: 150.00" in result.stdout
    assert "Precio final con IVA: 174.00" in result.stdout