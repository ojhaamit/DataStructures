'''
Distribute Bonuses:

You are the manager of a number of employees who all sit in a row.
The CEO would like to give bonuses to all of your employees,
but since the company did not perform so well this year the CEO would
like to keep the bonuses to a minimum.

The rule of giving bonuses is as below:
- Each employee willl begin with a bonus factor of 1X.
- For each employee, if they perform better than the person sitting next to them,
  the employee is given +1 higher bonus (and upto +2 if they perform better than
  both people to their sides).

Given a list of employee's performance, find the bonus that each employee should get.

Example:
Input: [1, 2, 3, 2, 3, 5, 1]
Output: [1, 2, 3, 1, 2, 3, 1]
'''

def getBonuses(performance):
    count = len(performance)
    bonus = [1] * count

    for i in range(1, count):
        if performance[i -1] < performance[i]:
            bonus[i] = bonus[i - 1] + 1

    for i in range(count - 2, -1, -1):
        if performance[i + 1] < performance[i]:
            bonus[i] = max(bonus[i], bonus[i + 1] + 1)

    return bonus


print(getBonuses([4, 3, 2, 1]))

