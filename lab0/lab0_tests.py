import unittest
import subprocess
from contextlib import contextmanager
import contextlib

from io import StringIO
from unittest.mock import patch

class Lab0(unittest.TestCase):
        
    def lab01(self): 
        output = subprocess.run(["python3", "lab01.py"], stdout=subprocess.PIPE).stdout.decode('utf-8')
        # print(output)        
        data = output.splitlines();
        self.assertEqual(len(data), 3, "Fel antal rader.")
        self.assertEqual(data[2], "Jag har druckit 2 koppar kaffe idag.", "Fel utskrift.")
        
    def lab02(self): 
        output = subprocess.run(["python3", "lab02.py"], stdout=subprocess.PIPE).stdout.decode('utf-8')
        # print(output)        
        data = output.splitlines();
        self.assertEqual(len(data), 3, "Fel antal rader.")
        self.assertEqual(data[2], "Jag har druckit 3 koppar kaffe idag.", "Fel utskrift.")


l = Lab0()
l.lab02()
