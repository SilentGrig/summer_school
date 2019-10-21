import poker_score


def test_should_return_higher_of_two_cards():
    card_one = "SA"
    card_two = "CK"
    higher_card = poker_score.get_higher_card(card_one, card_two)
    assert(higher_card == card_one)


def test_should_return_first_card_if_same_value():
    card_one = "C7"
    card_two = "S7"
    higher_card = poker_score.get_higher_card(card_one, card_two)
    assert(higher_card == card_one)


def test_should_return_highest_card_from_hand():
    hand = ["SJ", "H8", "HA", "D2", "C9"]
    highest_card = poker_score.get_highest_card_from_hand(hand)
    assert(highest_card == "HA")


def test_should_return_highest_card_when_tied_highest_value_in_hand():
    hand = ["SJ", "H8", "HJ", "D2", "C9"]
    highest_card = poker_score.get_highest_card_from_hand(hand)
    assert(highest_card == "SJ" or highest_card == "HJ")


def test_should_return_highest_card_from_single_hand():
    hands = [["SJ", "H8", "HK", "D2", "C9"]]
    hands_highest_cards = poker_score.get_highest_card_for_each_player(hands)
    assert(hands_highest_cards[0] == "HK")


def test_should_return_highest_card_for_multiple_hands():
    hands = [
        ["SJ", "H8", "HK", "D2", "C9"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SQ", "H5", "H9", "D8", "C2"],
    ]
    hands_highest_cards = poker_score.get_highest_card_for_each_player(hands)
    assert(hands_highest_cards == ["HK", "DA", "SQ"])


def test_should_return_only_player_with_highest_card():
    hands = [
        ["SJ", "H8", "HK", "D2", "C9"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SQ", "H5", "H9", "D8", "C2"],
    ]
    highest_cards = poker_score.score_high_card(hands)
    assert(highest_cards == [(2, "DA")])


def test_should_return_two_players_with_same_high_card():
    hands = [
        ["SJ", "H8", "HK", "D2", "C9"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SQ", "HA", "H9", "D8", "C2"],
    ]
    highest_cards = poker_score.score_high_card(hands)
    assert(highest_cards == [(2, "DA"), (3, "HA")])


def test_should_return_hand_grouped_by_value():
    hand = ["SJ", "H8", "HA", "D8", "C9"]
    grouped_hand = poker_score.get_cards_grouped_by_value(hand)
    assert(grouped_hand == {11: ["SJ"], 14: ["HA"], 8: ["H8", "D8"], 9: ["C9"]})


def test_should_return_pair_from_hand():
    hand = ["SJ", "H8", "HA", "D8", "C9"]
    highest_pair = poker_score.get_highest_pair_from_hand(hand)
    assert(highest_pair == ("H8", "D8"))


def test_should_return_empty_tuple_when_no_pair_in_hand():
    hand = ["SJ", "H3", "HA", "D8", "C9"]
    highest_pair = poker_score.get_highest_pair_from_hand(hand)
    assert(highest_pair == ())


def test_should_return_highest_pair_for_each_hand():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.get_highest_pair_per_player(hands)
    assert(highest_pairs == [("H8", "C8"), ("H2", "C2"), ("SA", "HA")])


def test_should_return_highest_pair_for_each_hand_and_empty_when_no_pair():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "C3", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.get_highest_pair_per_player(hands)
    assert(highest_pairs == [("H8", "C8"), (), ("SA", "HA")])


def test_should_return_winning_pairs():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "C3", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.score_pair_cards(hands)
    assert(highest_pairs == [(3, ("SA", "HA"))])


def test_should_return_two_tied_winning_pairs():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "CA", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.score_pair_cards(hands)
    assert(highest_pairs == [(2, ("DA", "CA")), (3, ("SA", "HA"))])


test_should_return_higher_of_two_cards()
test_should_return_first_card_if_same_value()
test_should_return_highest_card_from_hand()
test_should_return_highest_card_when_tied_highest_value_in_hand()
test_should_return_highest_card_from_single_hand()
test_should_return_highest_card_for_multiple_hands()
test_should_return_only_player_with_highest_card()
test_should_return_two_players_with_same_high_card()
test_should_return_hand_grouped_by_value()
test_should_return_pair_from_hand()
test_should_return_empty_tuple_when_no_pair_in_hand()
test_should_return_highest_pair_for_each_hand()
test_should_return_highest_pair_for_each_hand_and_empty_when_no_pair()
test_should_return_winning_pairs()
test_should_return_two_tied_winning_pairs()
print("All passed!")
