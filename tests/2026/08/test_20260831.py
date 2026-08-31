class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def build_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def test_nodes_between_critical_points_examples(solution):
    # Example 1: no critical points
    assert solution.nodesBetweenCriticalPoints(build_list([3, 1])) == [-1, -1]

    # Example 2: three critical points at indices 3, 5, 6
    assert solution.nodesBetweenCriticalPoints(build_list([5, 3, 1, 2, 5, 1, 2])) == [
        1,
        3,
    ]

    # Example 3: two critical points at indices 2 and 5
    assert solution.nodesBetweenCriticalPoints(
        build_list([1, 3, 2, 2, 3, 2, 2, 2, 7])
    ) == [3, 3]
