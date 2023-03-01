from __future__ import annotations

from two.util.ints import uint32, uint64

# 1 Two coin = 1,000,000,000,000 = 1 trillion mojo.
_mojo_per_two = 1000000000000
_reward_per = [
    (100000, 10),
    (200000, 9.5),
    (300000, 9),
    (400000, 8.5),
    (500000, 8),
    (700000, 7.5),
    (900000, 7),
    (1100000, 6.5),
    (1300000, 6),
    (1600000, 5.5),
    (1900000, 5),
    (2200000, 4.5),
    (2500000, 4),
    (3000000, 3.5),
    (3500000, 3),
    (4000000, 2.5),
    (4500000, 2),
    (5000000, 1.5),
    (6000000, 1.25),
    (7000000, 1),
    (8000000, 0.9),
    (9000000, 0.8),
    (11000000, 0.7),
    (13000000, 0.6),
    (15000000, 0.5),
    (17000000, 0.4),
    (19000000, 0.3),
    (22000000, 0.2),
    (25000000, 0.15),
    (25000000, 0.1),
]


def calculate_reward(height: uint32, index: int = -1) -> int:
    _height, _reward = _reward_per[index]
    if height >= _height if index == -1 else height < _height:
        return _reward
    else:
        index += 1
        return calculate_reward(height, index)


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times,
    due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height > 1000:
        return uint64(int((7 / 8) * calculate_reward(height) * _mojo_per_two))
    if height == 0:
        return uint64(int((7 / 8) * 3000000 * _mojo_per_two))
    else:
        return uint64(int((1 / 8) * calculate_reward(height) * _mojo_per_two))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times,
    due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    if height == 0:
        return uint64(int((1 / 8) * 3000000 * _mojo_per_two))
    return uint64(int((1 / 8) * calculate_reward(height) * _mojo_per_two))


def calculate_base_community_reward(height: uint32) -> uint64:
    """
    Community Rewards: 6% every block
    """
    return uint64(int((6 / 100) * calculate_reward(height) * _mojo_per_two))


def calculate_base_timelord_fee(height: uint32) -> uint64:
    """
    Timelord Fee: 2% every block
    """
    return uint64(int((2 / 100) * calculate_reward(height) * _mojo_per_two))
