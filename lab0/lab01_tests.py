import unittest
import lab01

class Lab01(unittest.TestCase):
    def lab01(self):
        self.assertEqual(lab01.kaffe(), "Jag har druckit 2 koppar kaffe idag.", "Tyvärr fel utskrift.")
        
    def lab02(self):
        self.assertEqual(lab01.kaffe(), "Jag har druckit 2 koppar kaffe idag.\nJag har druckit 3 koppar kaffe idag.", "Fel utskrift.")
        
        