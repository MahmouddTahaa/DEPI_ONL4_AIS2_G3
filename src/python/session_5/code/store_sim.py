from typing import Dict, List, Optional
from prettytable import PrettyTable


class Product:
    def __init__(self, name: str = "", price: float = 0.0, quantity: int = 0) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def accept_product_info(self) -> None:
        while True:
            name = input("Enter product name:>> ").strip()
            if name:
                self.name = name
                break

        while True:
            try:
                price = float(input("Enter product price:>> ").strip())
                if price < 0:
                    continue
                self.price = price
                break
            except ValueError:
                continue

        while True:
            try:
                qty = int(input("Enter product quantity:>> ").strip())
                if qty < 0:
                    continue
                self.quantity = qty
                break
            except ValueError:
                continue

    def to_dict(self) -> Dict:
        return {"name": self.name, "price": self.price, "quantity": self.quantity}


class InventoryHandler:
    def __init__(self) -> None:
        self.products: List[Dict] = []

    def add_product(self, product: Optional[Product] = None) -> None:
        if product is None:
            product = Product()
            product.accept_product_info()
        self.products.append(product.to_dict())

    def view_inventory(self) -> None:
        table = PrettyTable()
        table.field_names = ["Product Name", "Price ($)", "Quantity"]
        for p in self.products:
            table.add_row([p["name"], f"{p['price']:.2f}", p["quantity"]])
        print(table)

    def find_product(self, name: str) -> Optional[Dict]:
        key = name.strip().lower()
        for p in self.products:
            if p["name"].strip().lower() == key:
                return p
        return None


class DiscountHandler:
    def __init__(
        self, original_price: float, discount_code: Optional[str] = None
    ) -> None:
        self.discount_codes = {"AG225": 0.20, "MB213": 0.30}
        self.original_price = original_price
        self.discount_code = discount_code.strip().upper() if discount_code else ""
        self.discount_amount = 0.0

    def calculate_discount(self) -> float:
        if self.discount_code and self.discount_code in self.discount_codes:
            percentage = self.discount_codes[self.discount_code]
            self.discount_amount = percentage * self.original_price
            return self.discount_amount
        self.discount_amount = 0.0
        return 0.0

    def apply_discount(self) -> float:
        return max(self.original_price - self.discount_amount, 0.0)


class StoreFront:
    def __init__(self, inventory: InventoryHandler) -> None:
        self.inventory = inventory

    def place_order(self) -> None:
        name = input("Enter product name to buy:>> ").strip()
        product = self.inventory.find_product(name)
        if product is None:
            print("Product not found.")
            return

        try:
            quantity = int(input("Enter quantity:>> ").strip())
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return
            if quantity > product["quantity"]:
                print(f"Insufficient quantity, only {product['quantity']} available.")
                return
        except ValueError:
            print("Invalid quantity.")
            return

        unit_price = float(product["price"])
        subtotal = unit_price * quantity

        code = input("Enter discount code (or press Enter to skip):>> ").strip()
        dh = DiscountHandler(subtotal, code if code else None)
        dh.calculate_discount()
        total = dh.apply_discount()

        product["quantity"] -= quantity

        print(f"Subtotal: ${subtotal:.2f}")
        if dh.discount_amount > 0:
            print(f"Discount: -${dh.discount_amount:.2f} (code: {dh.discount_code})")
        print(f"Total to pay: ${total:.2f}")


def main() -> None:
    inv = InventoryHandler()
    store = StoreFront(inv)

    menu = (
        "Choose an action:\n"
        "1 - Add product\n"
        "2 - View inventory\n"
        "3 - Place order\n"
        "x - Exit\n"
        "Enter choice:>> "
    )

    while True:
        choice = input(menu).strip().lower()
        if choice == "1":
            inv.add_product()
            print("-" * 40)
        elif choice == "2":
            inv.view_inventory()
            print("-" * 40)
        elif choice == "3":
            store.place_order()
            print("-" * 40)
        elif choice == "x":
            break
        else:
            continue


if __name__ == "__main__":
    main()
