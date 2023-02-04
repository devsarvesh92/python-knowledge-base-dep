from collections import Counter


def tournament_winner(competitions: list[str], results: list[int]) -> str:
    return sorted(
        Counter(
            [competitions[id][::-1][res] for id, res in enumerate(results)]
        ).items(),
        key=lambda x: x[1],
        reverse=True,
    )[0][0]


print(
    tournament_winner(
        [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]], [0, 1, 1]
    )
)
