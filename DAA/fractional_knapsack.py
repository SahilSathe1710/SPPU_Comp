import time

def fractional_knapsack(items, weight_limit):
    for item in items:
        item['value_per_weight'] = item['value'] / item['weight']

    items.sort(key=lambda x: x['value_per_weight'], reverse=True)
    print(items)
    total_value = 0.0
    remaining_weight = weight_limit

    for item in items:
        if remaining_weight >= item['weight']:
            total_value += item['value']
            remaining_weight -= item['weight']
            print(f'remaining_weight: {remaining_weight},total_value: {total_value}')
        else:
            fraction = remaining_weight / item['weight']
            total_value += item['value'] * fraction
            print(f'remaining_weight: {fraction},total_value: {total_value}')
            break

    return total_value

if __name__ == "__main__":
    n_items = int(input("Enter number of items: "))
    items = []
    for i in range(n_items):
        item = {}
        item_weight = int(input(f"Enter weight of item: "))
        item_value = int(input("Enter value of item: "))
        item.update({'weight':item_weight,'value':item_value})
        items.append(item)
    weight_limit = 50
    
    start = time.time()
    max_value = fractional_knapsack(items, weight_limit)
    end = time.time()
    print("Maximum value that can be obtained:", max_value)
    print("Time Complexity: ",end - start)

