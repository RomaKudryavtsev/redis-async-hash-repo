import asyncio
from dataclasses import asdict
from repo import RedisRepo
from model import ReferrorLeaderboardInfo

leaderboard = [
    ReferrorLeaderboardInfo(
        referror_id=1,
        referror_name="test1",
        referral_points_earnings=1000,
        referees_num=10,
        avatar_url=None,
    ),
    ReferrorLeaderboardInfo(
        referror_id=2,
        referror_name="test2",
        referral_points_earnings=2000,
        referees_num=9,
        avatar_url=None,
    ),
]
redis_repo = RedisRepo()


async def save_leaderboard():
    await redis_repo.put_leaderboard(leaderboard)


async def read_leaderboard():
    return await redis_repo.get_leaderboard()


async def main():
    await save_leaderboard()
    res = await read_leaderboard()
    print([asdict(leaderboard_data) for leaderboard_data in res])


if __name__ == "__main__":
    asyncio.run(main())
