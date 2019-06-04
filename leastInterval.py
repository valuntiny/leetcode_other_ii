'''
Quest:
    Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
    However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
    You need to return the least number of intervals the CPU will take to finish all the given tasks.

    Example:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8

    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

    Note:
    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].

Solution:
    the total intervals depend on: n, the most frequent tasks occur M times, and there are Mct of them.
    let's say the most frequent jobs are A,B,C,...,K and each of them have M times
        - if n < Mct, then this constraint n doesnt necessarily do anything, we can make it more strict by setting n = Mct
        - if n >= Mct, then the sequence will be like A,B,C,...,K,_,A,B,C,...,K,_,A,B,C,...,K,_,A,B,C,...,K
          which the length is L = (M - 1) * (n + 1) + Mct.
          now there is two situation:
            * the rest non-most frequent jobs can fit in all the "_" idle time, then the time will just be L
            * the idle time is not enough for non-most frequent jobs, then we add them orderly to the end of each A,B,C,...,K,_ section
                  and the time will just be len(tasks)
'''


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = list(dict([l,tasks.count(l)] for l in set(tasks)).values())
        M = max(table)
        Mct = table.count(M)

        return max((M - 1) * (n + 1) + Mct, len(tasks))
