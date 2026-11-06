import math


def parse_plan(text):
    if not isinstance(text, str):
        return None

    if text.count(':') != 1:
        return None

    plan, gb = text.split(':')

    plan = plan.strip()

    if not plan or not gb.strip():
        return None

    try:
        data = float(gb)
    except ValueError:
        return None

    if not math.isfinite(data) or data < 0:
        return None

    return plan.title(), data


def usage_average(usage_csv):
    if not isinstance(usage_csv, str):
        return None

    if not usage_csv.strip():
        return None

    parts = usage_csv.split(',')
    values = []

    for part in parts:
        part = part.strip()

        if not part:
            return None

        try:
            value = int(part)
        except ValueError:
            return None

        if value < 0:
            return None

        values.append(value)

    if not values:
        return None

    return sum(values) // len(values)


def payable_bill(text):
    if not isinstance(text, str):
        return None

    if text.count('|') != 1:
        return None

    bill, discount = text.split('|')

    try:
        bill = float(bill)
        discount = float(discount)
    except ValueError:
        return None

    if not math.isfinite(bill) or not math.isfinite(discount):
        return None

    if bill < 0 or discount < 0:
        return None

    total = bill * 1.18 - discount

    if not math.isfinite(total):
        return None

    return max(total, 0)


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter plan:data in GB (e.g. standard:5): ")
    result = parse_plan(user_input)
    print("Plan and Data:", result)

    print("\n==== Running usage_average ====")
    user_input = input("Enter daily usage in MB as CSV (e.g. 300,450,800): ")
    result = usage_average(user_input)
    print("Average Usage:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 399|50): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)


if __name__ == "__main__":
    main()
