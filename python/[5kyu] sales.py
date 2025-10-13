class Sales:
    def __init__(self, _salesperson_name, sales_amount = 0.0, commission_rate=0.0):
        self._salesperson_name = _salesperson_name
        self._sales_amount = sales_amount
        self._commission_rate = commission_rate
        self._commission = 0.0
        self._calculate_commission()

    def _calculate_commission(self):
        self.commission = self._sales_amount * self._commission_rate

    def getSalesPersonName(self):
        return self._salesperson_name

    def getSalesAmount(self):
        return self._sales_amount

    def getCommissionRate(self):
        return self._commission_rate

    def getCommission(self):
        return self._commission

    def setSalesPersonName(self, value):
        self._name = value

    def setSalesPersonName(self, name):
        self._salesperson_name = name

    def setSalesAmount(self, amount):
        if amount < 0:
            self._sales_amount = 0.0
        else:
            self._sales_amount = amount

        self._calculate_commission()

    def __str__(self):
        return(
            f"Sales person: {self.getSalesPersonName()}\n"
            f"Sales Amount: {self.getSalesAmount()}\n"
            f"Commission Rate: {self.getCommissionRate()}\n"
            f"Commission: {self.getCommission()}\n"
        )

def main():
    """
    Creates three SalesTransaction objects demonstrating the three required
    initialization scenarios and verifies their attributes.
    """
    print("--- Testing SalesTransaction Scenarios ---\n")

    # Scenario a: All three parameters specified
    # Sales: $1000.00, Rate: 10% (0.10) -> Commission: $100.00
    print("--- Scenario A: All Parameters Specified ---")
    txn_a = Sales("Alice Johnson", 1000.00, 0.10)
    print(txn_a)
    print(f"Verification: Commission calculated correctly? {txn_a.getCommission() == 100.00}")
    print("\n" + "=" * 40 + "\n")

    # Scenario b: Only name and sales amount specified (Rate defaults to 0.0)
    # Sales: $500.00, Rate: 0% (0.00) -> Commission: $0.00
    print("--- Scenario B: Rate Defaults to 0.0 ---")
    txn_b = Sales("Bob Smith", 500.00)
    print(txn_b)
    print(f"Verification: Rate defaulted correctly? {txn_b.getCommissionRate() == 0.0}")
    print(f"Verification: Commission calculated correctly? {txn_b.getCommission() == 0.0}")
    print("\n" + "=" * 40 + "\n")

    # Scenario c: Only name specified (Amount and Rate default to 0.0)
    # Sales: $0.00, Rate: 0% (0.00) -> Commission: $0.00
    print("--- Scenario C: Amount and Rate Default to 0.0 ---")
    txn_c = Sales("Charlie Brown")
    print(txn_c)
    print(f"Verification: Amount defaulted correctly? {txn_c.getSalesAmount() == 0.0}")
    print(f"Verification: Commission calculated correctly? {txn_c.getCommission() == 0.0}")
    print("\n" + "=" * 40 + "\n")

    # Test Setter to ensure recalculation (using txn_c)
    print("--- Testing Setter Recalculation (on txn_c) ---")
    txn_c.setSalesPersonName("Charlie Brown Jr.")
    # Set Sales Amount (rate is still 0.0)
    txn_c.setSalesAmount(250.00)
    print(txn_c)
    print(f"Verification: Commission still 0.0 (Rate is 0.0)? {txn_c.getCommission() == 0.0}")


if __name__ == "__main__":
    main()
    