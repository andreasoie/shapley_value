import math
from itertools import combinations
from typing import Any, List, Tuple, Union


def create_combinations(n_players: int) -> Tuple[List[str], List[List[str]]]:
    """Creates all the possible coalition combinations for a given number of players.

    Args:
        n_players (int): the number of players in the game

    Returns:
        Tuple[List[str], List[List[str]]]: a tuple containing a list of all players and a list of all possible coalition combinations
    """
    players = [str(i) for i in range(n_players)]
    combos = [list(j) for i in range(len(players)) for j in combinations(players, i+1)]
    return players, combos


def generate_coalitions(actors: List[Any]) -> List[Any]:
    """Generates all the coalition combinations of actors.

    Args:
        actors (List[Any]): the elements to be combined

    Returns:
        List[Any]: the combinations of actors
    """
    actor_combos = []
    for i in range(1, len(actors) + 1):
        actor_combos += combinations(actors, i)
    return actor_combos


def calculate_shapley_values(n_players: int, characteristic_values: List[Union[float, int]]) -> List[float]:
    """Calculate the Shapley value for each player in a cooperative game.

    Args:
        n_players (int): The number of players in the game.
        characteristic_values (List[int]): A list of the characteristic values for all possible coalitions.
        (Example:
            n_players = 3
            coalition values = [418000000, 74200000, 28800000, 500090000, 499395020, 0, 576585020]:
            where list indices 0, 1, 2, 3, 4, 5, 6 refer to the following coalitions:
                {1} = 418000000,
                {2} = 74200000,
                {3} = 28800000,
                {1, 2} = 500090000,
                {1, 3} = 499395020,
                {2, 3} = 0,
                {1, 2, 3} = 576585020
            
            output: [480942510.0, 59345000.0, 36297510.0]
    Returns:
        List[Union[float, int]]: A list of the Shapley value for each player in the given game.
    """
    all_players, all_combinations = create_combinations(n_players)
    shapley_values: List[Union[float, int]] = []
    for player in all_players:
        shapley_value: Union[float, int] = 0
        for i in range(len(all_combinations)):
            if player in all_combinations[i]:
                continue
            Cui = sorted(all_combinations[i] + [player])
            k = all_combinations.index(Cui)
            l = i
            numerator = (characteristic_values[k] - characteristic_values[l]) * math.factorial(len(all_combinations[i])) * math.factorial(len(all_players) - len(all_combinations[i]) - 1)
            denominator = math.factorial(len(all_players))
            shapley_value += numerator / denominator
        temp_numerator = characteristic_values[all_players.index(player)] * math.factorial(0) * math.factorial(len(all_players) - 1)
        temp_denominator = math.factorial(len(all_players))
        shapley_value += temp_numerator / temp_denominator
        shapley_values.append(shapley_value)
    return shapley_values

if __name__ == "__main__":
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
    coalition_values = [sum([player["revenue"] for player in combination]) for combination in coalition_combinations]
    
    shapley_values = calculate_shapley_values(N_PLAYERS, coalition_values)
    print(f" Input: {coalition_values}")
    print(f"Output: {shapley_values}")
