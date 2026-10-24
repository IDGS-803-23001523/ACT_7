from main import main

def test_main(monkeypatch, capsys):
    inputs = iter(["200", "25"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    main()
    
    output = capsys.readouterr().out
    assert "Precio con descuento: 150.00" in output
    assert "Precio final con IVA: 174.00" in output