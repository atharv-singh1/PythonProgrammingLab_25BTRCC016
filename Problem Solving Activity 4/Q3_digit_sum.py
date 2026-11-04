def digit_sum(number):
    if number < 10:
        return number
    digit = number % 10
    return digit + digit_sum(number // 10)


print("Sum of digits:", digit_sum(5824))
print("Single digit:", digit_sum(7))
print("Zero:", digit_sum(0))
