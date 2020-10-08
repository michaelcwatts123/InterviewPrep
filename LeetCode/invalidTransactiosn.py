# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

# Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        personalTransactions = {}
        invalidTransactions = set()
        for i in transactions:
            name, time, amount, city = i.split(',')
            if(int(amount) > 1000):
                invalidTransactions.add(i)
            if(name not in personalTransactions.keys()):
                personalTransactions[name] = [(int(time), city, amount)]
                continue
            else:
                personalTransactions[name].append((int(time), city, amount))
                for j in personalTransactions[name]:
                    if(city == j[1]):
                        continue
                    else:
                        if(abs(j[0]-int(time)) <= 60):
                            invalidTransactions.add(i)
                            invalidTransactions.add(name+','+str(j[0])+','+j[2]+','+j[1])
        return list(invalidTransactions)