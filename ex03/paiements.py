from abc import ABC, abstractmethod

class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass

    @property
    def montant(self):
        return self._montant

class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        if len(cvv) != 3 or not cvv.isdigit():
            raise ValueError("Le CVV doit contenir 3 chiffres")
        if len(numero) != 16 or not numero.isdigit():
            raise ValueError("Le numéro de carte doit contenir 16 chiffres")
        self._numero = numero
        self._cvv = cvv

    def payer(self):
        numero_masque = "*" * 12 + self._numero[-4:]
        return f"Paiement de {self._montant:.2f}€ effectué par Carte Bancaire {numero_masque}"

class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        if "@" not in email:
            raise ValueError("Email invalide")
        self._email = email
        self._token = token

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ effectué via PayPal ({self._email})"

class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        if reseau not in ["BTC", "ETH", "USDT", "XRP"]:
            raise ValueError("Réseau crypto non supporté")
        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self):
        wallet_masque = self._wallet_id[:6] + "..." + self._wallet_id[-4:]
        return f"Paiement de {self._montant:.2f}€ effectué en {self._reseau} (wallet: {wallet_masque})"

def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())

if __name__ == "__main__":
    paiements = [
        CarteBancaire(150.00, "1234567812345678", "123"),
        CarteBancaire(89.99, "9876543210987654", "456"),
        PayPal(250.50, "user@example.com", "tok_abc123def456"),
        PayPal(45.00, "client@test.fr", "tok_xyz789ghi012"),
        Crypto(500.00, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "BTC"),
        Crypto(1200.00, "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb", "ETH")
    ]

    traiter_paiements(paiements)