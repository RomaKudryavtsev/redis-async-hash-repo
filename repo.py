import redis.asyncio as r
from config import config, Config
from model import ReferrorLeaderboardInfo
from utils import map_hash_to_leaderboard, map_leaderboard_to_hash


class RedisRepo:
    def __init__(self):
        self._config: Config = config
        self._pool = r.ConnectionPool(
            decode_responses=True,
            username=self._config.redis_user,
            password=self._config.redis_pwd,
            retry_on_timeout=True,
            socket_keepalive=True,
            health_check_interval=1,
        )
        self.r_client = r.Redis(connection_pool=self._pool)
        self.leaderboard_key = "leaderboard-referrals"

    async def put_leaderboard(self, leaderboard: list[ReferrorLeaderboardInfo]) -> None:
        leaderboard_hash = map_leaderboard_to_hash(leaderboard)
        await self.r_client.hset(self.leaderboard_key, mapping=leaderboard_hash)

    async def get_leaderboard(self) -> list[ReferrorLeaderboardInfo]:
        leaderboard_hash = await self.r_client.hgetall(self.leaderboard_key)
        return map_hash_to_leaderboard(leaderboard_hash)
