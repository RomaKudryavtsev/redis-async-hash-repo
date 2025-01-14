from dataclasses import dataclass


@dataclass
class ReferrorLeaderboardInfo:
    referror_id: int
    referror_name: str
    referral_points_earnings: int
    referees_num: int
    avatar_url: str | None
