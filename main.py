from random import shuffle

HEAP_N = 3
CARD_N = 4
# correct sequence of cards
PAFF = list(range(CARD_N-1, -1, -1))
path = []


class State:

    def __init__(self, cards):
        self.cards = cards
        self.empty = True
        for i in range(HEAP_N):
            max_j = len(self.cards[i]) - CARD_N + 1
            for j in range(max_j):
                if self.cards[i][j:j+CARD_N] == PAFF:
                    self.cards[i] = self.cards[i][:j] + self.cards[i][j+CARD_N:]
            if len(self.cards[i]) > 0:
                self.empty = False

    def __str__(self):
        return str(self.cards)

    def __eq__(self, other):
        return self.cards == other.cards


def step(state: State):
    if state.empty:
        print("hoorray")
        return len(path)
    for i in range(HEAP_N):
        for j in range(HEAP_N):
            if i != j and len(state.cards[j]) > 0 and\
                    (len(state.cards[i]) == 0 or (state.cards[i][-1] > state.cards[j][-1])):

                new_cards = [state.cards[i].copy() for i in range(HEAP_N)]
                new_cards[i].append(new_cards[j][-1])
                new_cards[j].pop()
                new_state = State(new_cards)
                if new_state not in path:
                    path.append(new_state)
                    ret = step(new_state)
                    path.pop()
                    return ret
    return -1


def check_nominal(state: State):
    # TODO
    return True


def check(state: State):
    if state.empty:
        print("Already solved")
        return True

    top_card = state.cards[0][-1]
    all_equal = True
    for heap in state.cards:
        if heap[-1] != top_card:
            all_equal = False
    if all_equal:
        print("No possible steps")
        return False

    if not check_nominal(state):
        print("Cannot be solved")
        return False

    path_len = step(state)
    if path_len == -1 :
        print("No path found")
        return False
    else:
        print("Found path with length", path_len)
        return True


if __name__ == '__main__':
    cards = list(range(CARD_N)) * HEAP_N
    path = []
    shuffle(cards)
    # cards = [3, 2, 1, 0]*3
    cards = [cards[i * CARD_N: i * CARD_N + CARD_N] for i in range(HEAP_N)]
    # print(cards)
    state = State(cards)
    # print(state)
    print(check(state))
