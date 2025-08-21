"""
Task
You will receive the bookseller's stocklist and a list of categories. Your task is to find the total number of books in the bookseller's stocklist, with the category codes in the list of categories. Note: the codes are in the same order in both lists.

Return the result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog).

Example
# the bookseller's stocklist:
"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"

# list of categories:
"A", "B", "C", "W"

# result:
"(A : 20) - (B : 114) - (C : 50) - (W : 0)"
Explanation:

category A: 20 books (ABART)
category B: 114 books = 25 (BKWRK) + 89 (BTSQZ)
category C: 50 books (CDXEF)
category W: 0 books
"""

def stock_list(stocklist, categories):
    if len(stocklist) == 0 or len(categories) == 0:
        return ""

    category_dic = {category: 0 for category in categories}
    answer = []

    for stock_data in stocklist:
        data_list = stock_data.split(" ")
        name = data_list[0][0]
        quantity = int(data_list[1])

        if name in category_dic:
            category_dic[name] += quantity

    for name, quantity in category_dic.items():
        answer.append(f"({name} : {str(quantity)})")

    return " - ".join(answer)
