import heapq


def min_connection_cost(cables, show_steps=False):
    if any(length < 0 for length in cables):
        raise ValueError("Довжина кабелю не може бути від'ємною")

    heap = cables.copy()
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        combined_length = first + second
        total_cost += combined_length

        if show_steps:
            print(f"З'єднуємо {first} + {second} = {combined_length}")

        heapq.heappush(heap, combined_length)

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]

    print("Довжини кабелів:", cables)

    result = min_connection_cost(cables, show_steps=True)

    print("Мінімальні загальні витрати:", result)
