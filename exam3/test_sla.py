import sys
import time
import os

from sla import show_sla
print(show_sla(float(sys.argv[1])))



"""from sla import show_sla
 

class TestFonctionGet(unittest.TestCase):
 
    # Chaque méthode dont le nom commence par 'test_'
    # est un test.
    def test_get_element(self):
 
        simple_comme_bonjour = ("8h 45.0m 57.0s")
        element = get(simple_comme_bonjour, 0)
 
        # Le test le plus simple est un test d'égalité. On se
        # sert de la méthode assertEqual pour dire que l'on
        # s'attend à ce que les deux éléments soient égaux. Sinon
        # le test échoue.
        self.assertEqual(element, "8h 45.0m 57.0s")
 
# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()"""
