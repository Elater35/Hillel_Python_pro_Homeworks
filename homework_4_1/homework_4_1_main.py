import homework_4_1_classes

# --- ТЕСТУВАННЯ РОБОТИ ---
if __name__ == "__main__":
    FILE_PATH = "shop_data_for_hw4.xlsx"

    # Створюємо магазин та завантажуємо початковий стан
    my_shop = homework_4_1_classes.Shop(FILE_PATH)
    my_shop.show_state()  # друкуємо поточний стан магазину
