from itertools import combinations


def getBasket():  # for testing: this is the initial basket, aka 'raw data'
    basket = [
        ('beer', 'wine', 'cheese'),
        ('beer', 'potato chips'),
        ('beer', 'potato chips', 'cheese'),
        ('eggs', 'flour', 'butter', 'cheese'),
        ('wine', 'cheese', 'beer'),
        ('wine', 'cheese'),
        ('potato chips',)
    ]

    return basket


def getSupport(basket):
    items = {}

    for transaction in basket:
        for item in transaction:
            items[(item,)] = items.setdefault((item,), 0) + 1
    return items


def filter(items, ignored, supportThreshold):
    i = {}

    for item in items:
        if items[item] >= supportThreshold:
            i[item] = items[item]
        else:
            ignored.append(item)

    return i, ignored  # returns a dict with key: value item :count and an array of tuples to be ignored when combining


def getCombinedSupport(basket, ignored, noToCombine=2, ):  # combines items in basket and create a new basket
    combinedItems = {}

    for transaction in basket:
        ignore = False
        for item in ignored:
            if set(item).intersection(transaction):
                ignore = True
        if not ignore:
            for combination in combinations(sorted(transaction), noToCombine):
                combinedItems[combination] = combinedItems.setdefault(combination, 0) + 1

    return combinedItems


def getAssociation(basket, items):
    def computeConfidence(basket, combination):
        count = 0
        for transaction in basket:
            if combination.issubset(transaction):
                count += 1

        return count / len(basket)

    def computeLift(basket, item1, item2):
        pass

    for item in items:
        print(item[0], end=' ')
        for x in range(1, len(item)):
            print('=> ' + item[x])


def main():
    frequentItemsetSize = 2
    supportThreshold = 2
    basket = getBasket()
    items = getSupport(basket)
    ignored = []
    items, ignored = filter(items, ignored, supportThreshold)

    for i in range(2, frequentItemsetSize + 1):
        items = getCombinedSupport(basket, ignored, 2)
        items, ignored = filter(items, ignored, supportThreshold)

    getAssociation(basket, items)


main()
