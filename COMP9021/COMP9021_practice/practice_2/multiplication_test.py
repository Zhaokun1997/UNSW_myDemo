for num_x in range(100, 1_000):
    for num_y in range(10, 100):
        product0 = num_x * (num_y % 10)
        if product0 < 1_000:
            continue
        product1 = num_x * (num_y // 10)
        if product1 >= 1_000:
            continue
        total_sum = product0 + product1 * 10
        if total_sum >= 10_000:
            continue
        column_sum = num_x % 10 + num_y % 10 + product0 % 10 + total_sum % 10
        if num_x // 10 % 10 + num_y // 10 + product0 // 10 % 10 + product1 % 10 + total_sum // 10 % 10 != column_sum:
            continue
        if num_x // 100 + product0 // 100 % 10 + product1 // 10 % 10 + total_sum // 100 % 10 != column_sum:
            continue
        if product0 // 1000 + product1 // 100 + total_sum // 1000 != column_sum:
            continue
        print(f'{num_x} * {num_y} = {total_sum}, all columns adding up to {column_sum}.')
