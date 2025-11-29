import unittest
from paiements import Paiement, CarteBancaire, PayPal, Crypto

class TestPaiements(unittest.TestCase):
    
    def test_montant_negatif(self):
        with self.assertRaises(ValueError):
            CarteBancaire(-50, "1234567812345678", "123")
    
    def test_montant_zero(self):
        with self.assertRaises(ValueError):
            PayPal(0, "test@example.com", "token123")
    
    def test_carte_bancaire_cvv_invalide(self):
        with self.assertRaises(ValueError):
            CarteBancaire(100, "1234567812345678", "12")
        with self.assertRaises(ValueError):
            CarteBancaire(100, "1234567812345678", "abcd")
    
    def test_carte_bancaire_numero_invalide(self):
        with self.assertRaises(ValueError):
            CarteBancaire(100, "123456781234567", "123")
        with self.assertRaises(ValueError):
            CarteBancaire(100, "abcd567812345678", "123")
    
    def test_paypal_email_invalide(self):
        with self.assertRaises(ValueError):
            PayPal(100, "invalidemail", "token123")
    
    def test_crypto_reseau_invalide(self):
        with self.assertRaises(ValueError):
            Crypto(100, "wallet123", "DOGE")
    
    def test_carte_bancaire_payer(self):
        carte = CarteBancaire(150.00, "1234567812345678", "123")
        resultat = carte.payer()
        self.assertIn("150.00", resultat)
        self.assertIn("Carte Bancaire", resultat)
        self.assertIn("5678", resultat)
    
    def test_paypal_payer(self):
        paypal = PayPal(250.50, "user@example.com", "token123")
        resultat = paypal.payer()
        self.assertIn("250.50", resultat)
        self.assertIn("PayPal", resultat)
        self.assertIn("user@example.com", resultat)
    
    def test_crypto_payer(self):
        crypto = Crypto(500.00, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "BTC")
        resultat = crypto.payer()
        self.assertIn("500.00", resultat)
        self.assertIn("BTC", resultat)
        self.assertIn("1A1zP1", resultat)
        self.assertIn("fNa", resultat)
    
    def test_montant_property(self):
        carte = CarteBancaire(100, "1234567812345678", "123")
        self.assertEqual(carte.montant, 100)

if __name__ == "__main__":
    unittest.main()