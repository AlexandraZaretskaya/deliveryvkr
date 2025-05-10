from app import create_app, db  # Импортируем Flask-приложение и объект базы данных
from models import Product  # Импортируем модель Product

# Создаем приложение и контекст приложения
app = create_app()
with app.app_context():  # Открываем контекст приложения для работы с базой данных
    # Пример данных для продуктов
    pizza1 = Product(name="Margherita", description="Classic pizza with tomato and cheese", price=350, image_filename="margherita.jpg")
    pizza2 = Product(name="Pepperoni", description="Pizza with spicy pepperoni", price=400, image_filename="pepperoni.jpg")

    # Добавляем продукты в сессию
    db.session.add(pizza1)
    db.session.add(pizza2)
    
    # Применяем изменения и сохраняем в базе данных
    db.session.commit()

    print("Продукты успешно добавлены в базу данных!")
