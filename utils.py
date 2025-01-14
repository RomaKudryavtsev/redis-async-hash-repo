import ast
from dataclasses import asdict
from model import ReferrorLeaderboardInfo


def map_leaderboard_to_hash(
    leaderboard: list[ReferrorLeaderboardInfo],
) -> dict[str, str]:
    res = {
        str(leaderboard_entry.referror_id): str(asdict(leaderboard_entry))
        for leaderboard_entry in leaderboard
    }
    return res


def map_hash_to_leaderboard(
    leaderboard_hash: dict[str, str]
) -> list[ReferrorLeaderboardInfo]:
    res = [
        ReferrorLeaderboardInfo(
            referror_id=leaderboard_data["referror_id"],
            referror_name=leaderboard_data["referror_name"],
            referral_points_earnings=leaderboard_data["referral_points_earnings"],
            referees_num=leaderboard_data["referees_num"],
            avatar_url=leaderboard_data["avatar_url"],
        )
        for leaderboard_data in (
            ast.literal_eval(data) for data in leaderboard_hash.values()
        )
    ]
    return res
