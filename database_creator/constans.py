INTERVAL_1MIN = '1m'
INTERVAL_3MIN = '3m'
INTERVAL_5MIN = '5m'
INTERVAL_15MIN = '15m'
INTERVAL_30MIN = '30m'
INTERVAL_1H = '1h'
INTERVAL_2H = '2h'
INTERVAL_4H = '4h'
INTERVAL_6H = '6h'
INTERVAL_8H = '8h'
INTERVAL_12H = '12h'
INTERVAL_1D = '1d'
INTERVAL_3D = '3d'
INTERVAL_1W = '1w'
INTERVAL_1M = '1M'

INTERVALS_MILLISECONDS = {
    INTERVAL_1MIN: 60 * 1000,
    INTERVAL_3MIN: 3 * 60 * 1000,
    INTERVAL_5MIN: 5 * 60 * 1000,
    INTERVAL_15MIN: 15 * 60 * 1000,
    INTERVAL_30MIN: 30 * 60 * 1000,
    INTERVAL_1H: 60 * 60 * 1000,
    INTERVAL_2H: 2 * 60 * 60 * 1000,
    INTERVAL_4H: 4 * 60 * 60 * 1000,
    INTERVAL_6H: 6 * 60 * 60 * 1000,
    INTERVAL_8H: 8 * 60 * 60 * 1000,
    INTERVAL_12H: 12 * 60 * 60 * 1000,
    INTERVAL_1D: 24 * 60 * 60 * 1000,
    INTERVAL_3D: 3 * 24 * 60 * 60 * 1000,
    INTERVAL_1W: 7 * 24 * 60 * 60 * 1000,
    INTERVAL_1M: 30 * 24 * 60 * 60 * 1000,
}

INTERVALS = list(INTERVALS_MILLISECONDS.keys())
INTERVALS_UNIQUE = INTERVALS[:-1]
INTERVALS_UNIQUE.append('1Mouth')

MAX_CANDLES_CONNECTIONS = 20
CANDLES_DELAY = 1