import timeit
from tabulate import tabulate
from constants import coins
from handlers.find_coins_greedy import find_coins_greedy
from handlers.find_min_coins import find_min_coins


def main():
    while True:
        try:
            target = int(input("Input target amount: "))
            if target < 0:
                print("Amount must be non-negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer amount.")

    number = input("Choose algorithm (1 - Greedy, 2 - Dynamic, 3 - Both): ")

    results = []

    match number:
        case "1":
            t = timeit.timeit(lambda: find_coins_greedy(coins, target), number=1)
            results.append(["Greedy", find_coins_greedy(coins, target), f"{t:.6f} c"])
        case "2":
            t = timeit.timeit(lambda: find_min_coins(coins, target), number=1)
            results.append(["Dynamic", find_min_coins(coins, target), f"{t:.6f} c"])
        case "3":
            t1 = timeit.timeit(lambda: find_coins_greedy(coins, target), number=1)
            t2 = timeit.timeit(lambda: find_min_coins(coins, target), number=1)
            results.append(["Greedy", find_coins_greedy(coins, target), f"{t1:.6f} c"])
            results.append(["Dynamic", find_min_coins(coins, target), f"{t2:.6f} c"])
        case _:
            print("Invalid input! Please choose 1, 2, or 3")
            return

    print("\nResults:")
    print(tabulate(
        results,
        headers=["Algorithm", "Coins", "Time"],
        tablefmt="github"
    ))


if __name__ == "__main__":
    main()
