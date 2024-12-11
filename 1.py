import asyncio
import json
import random
import datetime

async def generate_transaction():
    timestamp = datetime.datetime.now().isoformat()
    categories = ["Еда", "Авто", "Развлечения", "Одежда", "Квартира", "Связь", "Здоровье"]
    category = random.choice(categories)
    amount = round(random.uniform(10, 1000), 2)
    return {"timestamp": timestamp, "category": category, "amount": amount}

async def generate_transactions(num_transactions):
    transactions = await asyncio.gather(*[generate_transaction() for _ in range(num_transactions)])
    return transactions

async def save_transactions(transactions, filename="transactions.json"):
    for i in range(0, len(transactions), 10):
        chunk = transactions[i:i+10]
        with open(filename, "a") as f:
            json.dump(chunk, f)
            f.write("\n")
        print(f"Сохранено {len(chunk)} транзакций в файл {filename}")


async def main():
    num_transactions = int(input("Введите количество транзакций: "))
    transactions = await generate_transactions(num_transactions)
    await save_transactions(transactions)

if __name__ == "__main__":
    asyncio.run(main())
