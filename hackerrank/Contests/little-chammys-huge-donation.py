def solve(total_candies):
    children_served = int ((3 * total_candies) ** (1 / 3.0))
    candies = children_served * (children_served + 1) * (2*children_served + 1) / 6

    while candies <= total_candies:
        children_served += 1
        candies = children_served * (children_served + 1) * (2*children_served + 1) / 6    

    return children_served - 1


testcases = int(raw_input())
candies_list = []

for i in range(testcases):
    candies = int(raw_input())
    candies_list.append(candies)

for candies in candies_list:
    print solve(candies)

