import subprocess
import sys

def test_compra():
    result = subprocess.run([sys.executable, 'main.py'], input='200\n25\n', text=True, capture_output=True)
    
    assert result.returncode == 0
    
    assert "Precio con descuento: 150.00" in result.stdout
    assert "Precio final con IVA: 174.00" in result.stdout

def test_compra_excepcion():
    # Caso de error: simula ingresar un descuento inválido > 100 (activa el bloque except)
    result = subprocess.run([sys.executable, 'main.py'], input='100\n150\n', text=True, capture_output=True)
    assert result.returncode == 0
    assert "Error:" in result.stdout