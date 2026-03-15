# https://leetcode.com/problems/fancy-sequence/description

class Fancy:
    """1622. Fancy Sequence

    Write an API that generates fancy sequences using the append, addAll,
    and multAll operations. Implement the Fancy class:
    Fancy() Initializes the object with an empty sequence.
    void append(val) Appends an integer val to the end of the sequence.
    void addAll(inc) Increments all existing values in the sequence by an
    integer inc.
    void multAll(m) Multiplies all existing values in the sequence by an
    integer m.
    int getIndex(idx) Gets the current value at index idx (0-indexed) of the
    sequence modulo 10^9 + 7. If the index is greater or equal than the
    length of the sequence, return -1.
    """
    def __init__(self):
        # base stored values (transformed so current = mult * base + add)
        self.seq = []
        self.mult = 1
        self.add = 0
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        # store inverse-adjusted value to preserve invariant:
        # (self.seq[-1] * self.mult + self.add) % MOD == val at append time
        inv_mult = pow(self.mult, self.MOD - 2, self.MOD)
        stored = ((val - self.add) % self.MOD * inv_mult) % self.MOD
        self.seq.append(stored)

    def add_all(self, inc: int) -> None:
        # lazy add: only update additive (applies to all existing)
        self.add = (self.add + inc) % self.MOD

    def mult_all(self, m: int) -> None:
        # lazy mult: scale both mult and add (new_val = m * old_val)
        self.add = (self.add * m) % self.MOD
        self.mult = (self.mult * m) % self.MOD

    def get_index(self, idx: int) -> int:
        # O(1) retrieval with current lazy transformation
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.MOD

    addAll = add_all
    multAll = mult_all
    getIndex = get_index