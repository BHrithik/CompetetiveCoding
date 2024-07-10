class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current_count = 0
        # logs = [i for i in logs if i!= "./"]
        for i in logs:
            if i == "./":
                continue
            if i == "../":
                current_count -= 1
                current_count = max(0,current_count)
            else:
                current_count += 1
        return current_count if current_count > 0 else 0