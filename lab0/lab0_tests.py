import unittest

class Lab0(unittest.TestCase):
    def lab01(self):
        import lab01
        self.assertEqual(lab01.kaffe(), "Jag har druckit 2 koppar kaffe idag.", "Tyvärr fel utskrift.")
        
    def lab02(self):
        import lab02
        self.assertEqual(lab02.kaffe(), "Jag har druckit 3 koppar kaffe idag.", "Tyvärr fel utskrift.")
        
        