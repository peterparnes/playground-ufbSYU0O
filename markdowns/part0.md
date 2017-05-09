# Lab 0 - En inledande övning 

Det här är den allra första labben i D0009E. Den är tänkt som en introduktion till själva utvecklingsmiljön och till att skriva program. Vi ska inte lösa några problem i denna introduktionslab, utan det kommer först i nästa lab. 

## Uppgift 1

Skriv in följande program i programrutan nedan:

```python
def kaffe():
  print("Detta är ett program som räknar hur mycket kaffe du dricker.")
  namn = "Anna Andersson"
  print("Jag heter " + namn)
  n = 2
  druckit = "Jag har druckit " + str(n) + " koppar kaffe idag."
  print(druckit)
  return druckit
```

Välj "Run my code" för att köra programmet. Programmet kör och text skrivs ut på skärmen.

@[Lab0 del 1]({"stubs":["lab01.py"], "command":"lab0_tests.Lab01.lab01"})

## Uppgift 2:

Kan du ändra programmet det står att du druckit 3 koppar kaffe? 

Välj "Run my code" för att köra programmet. Programmet kör och text skrivs ut på skärmen. Fundera på varför de två sista print-satserna skriver ut olika text fast det är samma sats. 

@[Lab0 del 2]({"stubs":["lab02.py"], "command":"lab0_tests.Lab0.lab02"})

@[Lab0 del 2]({"stubs":["lab03.py"], "command":"python check_lab02.py"})


Du har nu skrivit, kört och modifierat ett pythonprogram! 