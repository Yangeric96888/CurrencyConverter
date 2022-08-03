import requests

isRun = True  # Runs the code
initialCur = input("What currency do you want to convert from? ").lower()  # The currency from which we convert
curData = requests.get("http://www.floatrates.com/daily/{}.json".format(initialCur)).json()  # Data for initial currency

# Initial cache
cache = {}
if initialCur != "eur":
    cache["eur"] = curData["eur"]["rate"]
if initialCur != "usd":
    cache["usd"] = curData["usd"]["rate"]

while isRun:

    finalCur = input("What currency to convert to? ").lower()
    # Breaks if blank input
    if finalCur.strip() == "":
        isRun = False

    if isRun:
        initialAmt = int(input("How much money do you want to conver to? "))  # Requests amount of money to be converted

        # Currency Exchange
        print("Checking the cache...")
        if finalCur in cache:
            print("Oh! It is in the cache!")
            finalAmt = round(cache[finalCur] * initialAmt, 2)
            print("You received {amt} {cur}.".format(amt=finalAmt, cur=finalCur.upper()))
        else:
            print("Sorry, but it is not in the cache!")
            finalAmt = round(curData[finalCur.lower()]["rate"] * initialAmt, 2)
            print("You received {amt} {cur}.".format(amt=finalAmt, cur=finalCur.upper()))

            cache[finalCur] = curData[finalCur]["rate"]  # Adds new currency to cache
