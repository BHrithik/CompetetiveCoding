class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # Why your current solution might not work + complexity drawbacks:
        # 1) Incorrect cooldown logic:
        #    - You store `last_processed` as a time, but your check `if time - last_processed >= 0`
        #      is basically always true once `last_processed` is <= time (which it will be after first run).
        #    - Cooldown needs `time >= last_processed + n + 1`, not just `time - last_processed >= 0`.
        #
        # 2) First-time processing detection is wrong:
        #    - You initialize last_processed to 0 for every task, so at time=0 they all look "available",
        #      but that doesn't represent "never processed". You need a sentinel like -inf or track next_valid_time.
        #
        # 3) Heap ordering is not aligned with what you need:
        #    - You heapify lists like [last_processed, remaining_count], which makes a min-heap by last_processed first.
        #    - The core greedy strategy is to always pick the task with the highest remaining count that is currently available.
        #      Your heap doesn't prioritize remaining counts.
        #
        # 4) You can get stuck idling even when a different task is available:
        #    - Because you only look at the top heap element and idle otherwise, but the next element might be runnable.
        #
        # Complexity drawback:
        # - The simulation can still be O(T log U), but due to incorrect ordering it can do excessive idles and is wrong anyway.
        # - There is also a well-known O(U) math solution (U = number of unique task types) that avoids simulation.

        # Follow-up Questions:
        # 1) Is `n` the cooldown between identical tasks (i.e., after doing 'A' you must wait n intervals before 'A' again)?
        #    (Yes.)
        # 2) Does each task take exactly 1 unit time and we can be idle?
        #    (Yes.)
        # 3) Do we only need the minimum total intervals, not the actual schedule?
        #    (Yes.)
        # 4) Are tasks represented by letters and there can be repeats?
        #    (Yes.)

        # Brute Force Approach:
        # - Try to construct a schedule interval by interval, always picking any allowed task.
        # - Backtracking / brute scheduling blows up exponentially in worst case.
        # - Time Complexity: exponential (not feasible).
        # - Space Complexity: exponential / large recursion state.

        # Optimized Approach (Math / Counting):
        # - Count frequencies of tasks.
        # - Let max_freq be the maximum frequency.
        # - Let num_max be how many tasks have that max frequency.
        # - Think of placing the most frequent tasks into (max_freq - 1) "gaps" that each need length (n + 1),
        #   then the last block contributes num_max.
        # - Minimum intervals:
        #     max( len(tasks), (max_freq - 1) * (n + 1) + num_max )
        # - Time Complexity: O(T) where T = len(tasks)
        # - Space Complexity: O(U) where U = number of unique tasks

        if n == 0:
            return len(tasks)
        if not tasks:
            return 0

        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        max_freq = max(freq.values())
        num_max = 0
        for v in freq.values():
            if v == max_freq:
                num_max += 1

        # core formula
        skeleton = (max_freq - 1) * (n + 1) + num_max
        return max(len(tasks), skeleton)
