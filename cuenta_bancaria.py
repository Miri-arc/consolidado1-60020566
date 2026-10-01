class SaldoInsuficienteError(Exception):
    """Excepción personalizada cuando no hay saldo suficiente."""
    pass

class MontoInvalidoError(Exception):
    """Excepción personalizada cuando se ingresa un monto negativo o cero."""
    pass

class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise MontoInvalidoError("El monto a depositar debe ser mayor a cero.")
        self._saldo += monto

    def retirar(self, monto: float) -> None:
        if monto <= 0:
            raise MontoInvalidoError("El monto a retirar debe ser mayor a cero.")
        if monto > self._saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente. Saldo actual: S/{self._saldo:.2f}")
        self._saldo -= monto

    def transferir(self, cuenta_destino: "CuentaBancaria", monto: float) -> None:
        self.retirar(monto)
        cuenta_destino.depositar(monto)

    def __str__(self) -> str:
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: S/{self._saldo:.2f}"

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("001-123", "Miri", 500.0)
    cuenta2 = CuentaBancaria("001-456", "Juan", 200.0)

    print(cuenta1)
    print(cuenta2)

    print("\n--- Probando transferencia ---")
    cuenta1.transferir(cuenta2, 150.0)
    print(f"Saldo Miri tras transferencia: S/{cuenta1.saldo:.2f}")
    print(f"Saldo Juan tras transferencia: S/{cuenta2.saldo:.2f}")

    print("\n--- Probando manejo de excepciones ---")
    try:
        cuenta1.retirar(1000.0)
    except SaldoInsuficienteError as e:
        print(f"Error capturado: {e}")

    try:
        cuenta2.depositar(-50.0)
    except MontoInvalidoError as e:
        print(f"Error capturado: {e}")
        