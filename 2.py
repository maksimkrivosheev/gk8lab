import asyncio
import json

async def process_transactions(filename="transactions.json"):
    transactions_by_category = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                  chunk = json.loads(line)
                  for transaction in chunk:
                      category = transaction["category"]
                      amount = transaction["amount"]
                      transactions_by_category[category] = transactions_by_category.get(category, 0) + amount
                except json.JSONDecodeError as e:
                  print(f"Ошибка JSON: {e}")

        for category, total_amount in transactions_by_category.items():
            print(f"Категория: {category}, Общая сумма: {total_amount}")
            if total_amount > 3000: 
                print(f"Вы превысили расход по {category}!")

    except FileNotFoundError:
        print(f" {filename} не найден.")


async def main():
    await process_transactions()

if __name__ == "__main__":
    asyncio.run(main())
