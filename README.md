# Shapley Value

Shapley values are a method used in cooperative game theory to assign a fair distribution of the total "payoff" of a game among its players.

The concept of Shapley values was introduced by [Lloyd Shapley](https://www.nobelprize.org/prizes/economic-sciences/2012/shapley/facts/) in the early 1950s. The Shapley value of a player in a game is defined as the average marginal contribution of that player over all possible coalitions. In other words, it calculates how much a player adds to the total payoff of the game on average when he or she joins a coalition compared to when he or she is not in the coalition.

Shapley values have numerous use cases in different fields, including economics, political science, and computer science. Some examples of their applications are:

- In economics, Shapley values are used to allocate the gains from cooperation among the players in a market or a supply chain. They can help determine the fair share of profits that each participant should receive.
- In political science, Shapley values are used to analyze the power and influence of different actors in a legislative body or a voting system. They can help determine the likelihood of a particular player's vote being decisive.
- In computer science, Shapley values are used in machine learning to explain the contribution of each feature to the prediction of a model. They can help identify the most important variables and improve the interpretability of the model.

### Example
using 'revenue' as the coalition feature
```python

N_PLAYERS = 3
REVENUE_A = 418_000_000 # Company A's revenue
REVENUE_B = 74_200_000  # Company B's revenue
REVENUE_C = 28_800_000  # Company C's revenue

companies = [
    {"id": "A", "revenue": REVENUE_A},
    {"id": "B", "revenue": REVENUE_B},
    {"id": "C", "revenue": REVENUE_C},
]
coalition_combinations = generate_coalitions(companies)
```
```bash
>> [
    ({'..A.'},),
    ({'..B.'},),
    ({'..C.'},),
    ({'..A.'}, {'..B.'}),
    ({'..A.'}, {'..C.'}),
    ({'..B.'}, {'..C.'}),
    ({'..A.'}, {'..B.'}, {'..C.'})
]
```
In practice, certain combinations results in changes in the average expected marginal contribution (costs, roles, etc.). This would make the Shapley values at the end more meaningful. For the sake of simplicity, they're not in this example.
```python

coalition_values = [sum([player["revenue"] for player in combination]) for combination in coalition_combinations]
```

```bash
>> [418000000, 74200000, 28800000, 492200000, 446800000, 103000000, 521000000]
```
```python
shapley_values = calculate_shapley_values(N_PLAYERS, coalition_values)
```

```bash
>> [418000000.0, 74200000.0, 28800000.0]
```
which totals to `521.000.000`

To put it into context, let `521.000.000` be the yearly revenue of a joint venture between 3 companies. The Shapley values can be interpreted as follows:

- Company 1 is responsible `418.000.000` ~ 80.2% of the revenue
- Company 2 is responsible `74.200.000`  ~ 14.2% of the revenue
- Company 3 is responsible `28.800.000`  ~ 5.5% of the revenue

#### Testing
```python
python test_shapley.py
```

#### See more
<https://www.researchgate.net/publication/316869719_Shapley_Value_its_algorithms_and_application_to_supply_chains>