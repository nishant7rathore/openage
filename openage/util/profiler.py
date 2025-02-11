# Copyright 2017-2022 the openage authors. See copying.md for legal info.

"""
Profiling utilities
"""

import cProfile
import io
import pstats
import tracemalloc


class Profiler:
    """
    A class for quick and easy profiling.
    Usage:
        p = Profiler()
        with p:
            # call methods that need to be profiled here
        print(p.report())

    The 'with' statement can be replaced with calls to
    p.enable() and p.disable().
    """

    profile: cProfile.Profile = None
    profile_stats: pstats.Stats = None
    profile_stream = None

    def __init__(self, oStream=None):
        # oStream can be a file if the profile results want to be saved.
        self.profile = cProfile.Profile()
        self.profile_stream = oStream

    def __enter__(self):
        """
        Activate data collection.
        """
        self.enable()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stop profiling.
        """
        self.disable()

    def write_report(self, sortby: str = 'calls') -> None:
        """
        Write the profile stats to profile_stream's file.
        """
        self.profile_stats = pstats.Stats(self.profile, stream=self.profile_stream)
        self.profile_stats.sort_stats(sortby)
        self.profile_stats.print_stats()

    def report(self, sortby: str = 'calls'):
        """
        Return the profile_stats to the console.
        """
        self.profile_stats = pstats.Stats(self.profile, stream=io.StringIO())
        self.profile_stats.sort_stats(sortby)
        self.profile_stats.print_stats()
        return self.profile_stats.stream.getvalue()

    def enable(self):
        """
        Begins profiling calls.
        """
        self.profile.enable()

    def disable(self):
        """
        Stop profiling calls.
        """
        self.profile.disable()


class Tracemalloc:
    """
    A class for memory profiling.
    Usage:
        p = Tracemalloc()
        with p:
            # call methods that need to be profiled here
        print(p.report())

    The 'with' statement can be replaced with calls to
    p.enable() and p.disable().
    """

    snapshot = None

    def __init__(self, oStream=None):
        # oStream can be a file if the profile results want to be saved.
        self.tracemalloc_stream = oStream

    def __enter__(self):
        """
        Activate data collection.
        """
        self.enable()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stop profiling.
        """
        self.disable()

    def report(
        self,
        sortby: str = 'lineno',
        cumulative: bool = True,
        limit: int = 100
    ) -> None:
        """
        Return the snapshot statistics to the console.
        """
        for stat in self.snapshot.statistics(sortby, cumulative)[:limit]:
            print(stat)

    @staticmethod
    def enable() -> None:
        """
        Begins profiling calls.
        """
        tracemalloc.start()

    def disable(self) -> None:
        """
        Stop profiling calls.
        """
        self.snapshot = tracemalloc.take_snapshot()
