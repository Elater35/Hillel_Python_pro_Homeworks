"""Створення класів для магазину"""

import pandas as pd


class Product:
    """Створення класу Product (Товар) з атрибутами - ідентифікаційний номер,
    назва товару, ціна, кількість,- та методами зміни ціни та кількості.
    """
    def __init__(self, prod_id: int, name: str, price: float, quantity: int):
        self.prod_id = prod_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Перевизначаємо метод __str__:
        отримуємо відформатований рядок про товар та його атрибути.
        """
        return (f"Товар: {self.name}. Ціна: {self.price} грн. "
                f"Кількість: {self.quantity} шт.")

    def change_price(self, new_price: float) -> "Product":
        """Заведення нової ціни через аргумент методу."""
        self.price = new_price
        return self

    def change_quantity(self, new_quantity: int) -> "Product":
        """Заведення нової кількості товару через аргумент методу."""
        self.quantity = new_quantity
        return self


class Customer:
    """Створення класу Customer (Покупець) з атрибутами - ідентифікаційний
    номер, прізвище-ім'я, e-mail, історія (список списків з двоелементних
    кортежів (товар, кількість),- та методом додавання чергового замовлення
    до історії замовлень.
    """
    def __init__(self, cust_id: int, cust_name: str, email: str,
                 orders: list["Order"] | None = None):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.email = email
        self.orders = orders if isinstance(orders, list) else []

    def __str__(self):
        """Перевизначаємо метод __str__:
        отримуємо інформацію про покупця та історію його закупівель.
        """
        orders_str = ("\n".join([str(order) for order in self.orders])
                      if self.orders else "Немає замовлень.")
        return (f"Користувач: {self.cust_name}. e-mail: {self.email}.\n"
                f"Ваші покупки:\n{orders_str}")

    def add_to_orders(self, order: "Order") -> "Customer":
        """Додає замовлення до історії клієнта."""
        self.orders.append(order)
        return self


class Order:
    """Створення класу Order (Замовлення) з одним атрибутом - закупівля
    (список з двоелементних кортежів (товар, кількість),- та методами
    додавання товару до кошика покупок і розрахунку загальної вартості
    куплених товарів.
    """
    def __init__(self, purchases: list[tuple[Product, int]] | None = None):
        self.purchases = purchases if purchases is not None else []

    def __str__(self):
        """Перевизначаємо метод __str__:
        отримуємо інформацію про вміст замовлення та його вартість.
        """
        items = ", ".join([f"{prod.name} ({quant} шт.)"
                           for prod, quant in self.purchases])
        return (f"Замовлення: Товари: {items}. "
                f"Сумарна вартість: {self.calculate_total()} грн.")

    def add_to_cart(self, product: Product, quantity) -> "Order":
        """Додаємо товар до замовлення, якщо його кількість достатня."""
        if product.quantity >= quantity:
            self.purchases.append((product, quantity))
            product.change_quantity(product.quantity - quantity)
        else:
            print(f"Недостатньо товару '{product.name}'. "
                  f"(Доступно {product.quantity} шт).")
        return self

    def calculate_total(self) -> float:
        """Рахує загальну вартість всього замовлення."""
        return sum(product.price * quant for product, quant in self.purchases)


class Shop:
    """Клас магазину, який ініціалізується з файлу Excel за допомогою
     бібліотеки 'pandas'.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.products = {}
        self.customers = {}
        self.load_data()

    def load_data(self):
        """Зчитуємо дані з Excel-файлу та заповнюємо словники магазину."""
        try:
            df_products = pd.read_excel(self.file_path, sheet_name="Товари")
            for _, row in df_products.iterrows():
                prod = Product(row["ID"], row["Назва"], row["Ціна"],
                               row["Кількість"])
                self.products[prod.prod_id] = prod

            df_customers = pd.read_excel(self.file_path, sheet_name="Клієнти")
            for _, row in df_customers.iterrows():
                cust = Customer(row["ID"], row["Ім'я"], row["e-mail"],
                                row["Покупки"])
                self.customers[cust.cust_id] = cust

            print(f" Дані успішно завантажено з файлу: {self.file_path}\n")
        except FileNotFoundError:
            print(f"Помилка: Файл не знайдено за шляхом {self.file_path}")
        except ValueError as e:
            print(f"Помилка в структурі Excel (можливо, "
                  f"відсутній потрібний лист): {e}")
        except KeyError as e:
            print(f"Помилка: У таблиці не знайдено стовпчик {e}")

    def show_state(self):
        """Виводить поточний стан магазину."""
        print("--- АСОРТИМЕНТ МАГАЗИНУ ---")
        for prod in self.products.values():
            print(prod)

        print("\n--- БАЗА КЛІЄНТІВ ---")
        for client in self.customers.values():
            print(client)
