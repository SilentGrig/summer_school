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
    highest_card = poker_score.get_highest_group_from_hand(hand, 1)
    assert(highest_card == ("HA",))


def test_should_return_next_highest_card_when_tied_highest_value_in_hand():
    hand = ["SJ", "H8", "HJ", "D2", "C9"]
    highest_card = poker_score.get_highest_group_from_hand(hand, 1)
    assert(highest_card == ("C9",))


def test_should_return_highest_card_from_single_hand():
    hands = [["SJ", "H8", "HK", "D2", "C9"]]
    hands_highest_cards = poker_score.get_highest_group_per_player(hands, 1)
    assert(hands_highest_cards[0] == ("HK",))


def test_should_return_highest_card_for_multiple_hands():
    hands = [
        ["SJ", "H8", "HK", "D2", "C9"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SQ", "H5", "H9", "D8", "C2"],
    ]
    hands_highest_cards = poker_score.get_highest_group_per_player(hands, 1)
    assert(hands_highest_cards == [("HK",), ("DA",), ("SQ",)])


def test_should_return_only_player_with_highest_card():
    hands = [
        ["SJ", "H8", "HK", "D2", "C9"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SQ", "H5", "H9", "D8", "C2"],
    ]
    highest_cards = poker_score.score_group_cards(hands, 1)
    assert(highest_cards == {1: ("DA",)})


def test_should_return_two_players_with_same_high_card():
    hands = [
        ["SJ", "H8", "HK", "D2", "C9"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SQ", "HA", "H9", "D8", "C2"],
    ]
    highest_cards = poker_score.score_group_cards(hands, 1)
    assert(highest_cards == {1: ("DA",), 2: ("HA",)})


def test_should_return_hand_grouped_by_value():
    hand = ["SJ", "H8", "HA", "D8", "C9"]
    grouped_hand = poker_score.get_cards_grouped_by_value(hand)
    assert(grouped_hand == {11: ["SJ"], 14: ["HA"], 8: ["H8", "D8"], 9: ["C9"]})


def test_should_return_pair_from_hand():
    hand = ["SJ", "H8", "HA", "D8", "C9"]
    highest_pair = poker_score.get_highest_group_from_hand(hand, 2)
    assert(highest_pair == ("H8", "D8"))


def test_should_return_empty_tuple_when_no_pair_in_hand():
    hand = ["SJ", "H3", "HA", "D8", "C9"]
    highest_pair = poker_score.get_highest_group_from_hand(hand, 2)
    assert(highest_pair == ())


def test_should_return_highest_pair_for_each_hand():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.get_highest_group_per_player(hands, 2)
    assert(highest_pairs == [("H8", "C8"), ("H2", "C2"), ("SA", "HA")])


def test_should_return_highest_pair_for_each_hand_and_empty_when_no_pair():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "C3", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.get_highest_group_per_player(hands, 2)
    assert(highest_pairs == [("H8", "C8"), (), ("SA", "HA")])


def test_should_return_winning_pairs():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "C3", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.score_group_cards(hands, 2)
    assert(highest_pairs == {2: ("SA", "HA")})


def test_should_return_two_tied_winning_pairs():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "CA", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_pairs = poker_score.score_group_cards(hands, 2)
    assert(highest_pairs == {1: ("DA", "CA"), 2: ("SA", "HA")})


def test_should_remove_used_cards():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "CA", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    usedCards = {1: ("DA", "CA"), 2: ("SA", "HA")}
    remainingCards = poker_score.handsRemovingUsedAndFoldedPlayers(hands, usedCards)
    assert(remainingCards == [[], ["C7", "H2", "S9"], ["H9", "D8", "C4"]])


def test_should_return_kicker_card_on_pair_tie():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "DA", "CA", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    winning_cards = poker_score.get_winning_hands(hands)
    assert(winning_cards == ({1: ("DA", "CA", "S9"), 2: ("SA", "HA", "H9")}, "one pair with kicker"))


def test_should_return_three_of_a_kind_from_hand():
    hand = ["SJ", "H8", "HA", "D8", "C8"]
    highest_triple = poker_score.get_highest_group_from_hand(hand, 3)
    assert(highest_triple == ("H8", "D8", "C8"))


def test_should_return_highest_three_of_a_kind_for_each_hand():
    hands = [
        ["SJ", "H8", "HK", "D8", "C8"],
        ["C7", "H2", "DA", "C2", "S9"],
        ["SA", "HA", "H9", "D8", "C4"],
    ]
    highest_triples = poker_score.get_highest_group_per_player(hands, 3)
    assert(highest_triples == [("H8", "D8", "C8"), (), ()])


def test_should_return_winning_three_of_a_kinds():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "H2", "D8", "C3", "S9"],
        ["SA", "HA", "H9", "DA", "C4"],
    ]
    highest_triples = poker_score.score_group_cards(hands, 3)
    assert(highest_triples == {2: ("SA", "HA", "DA")})


def test_should_return_kicker_card_on_three_of_a_kind_tie():
    hands = [
        ["SJ", "H8", "HK", "D2", "C8"],
        ["C7", "HA", "DA", "CA", "S9"],
        ["SA", "HA", "DA", "D8", "C4"],
    ]
    winning_cards = poker_score.get_winning_hands(hands)
    assert(winning_cards == ({1: ("HA", "DA", "CA", "S9")}, "three of a kind with kicker"))


def test_should_return_kicker_card_on_high_card_tie():
    hands = [
        ["SJ", "H8", "HK", "D2", "C4"],
        ["C7", "H3", "DA", "C8", "S9"],
        ["SA", "HJ", "DQ", "D8", "C4"],
    ]
    winning_cards = poker_score.get_winning_hands(hands)
    assert(winning_cards == ({2: ("SA", "DQ")}, "high card with kicker"))


def test_should_return_kicker_cards_on_four_high_card_ties():
    hands = [
        ["SA", "HK", "HQ", "D10", "C9"],
        ["CA", "HK", "DQ", "C10", "S8"],
    ]
    winning_cards = poker_score.get_winning_hands(hands)
    assert(winning_cards == ({0: ("SA", "HK", "HQ", "D10", "C9")}, "high card with kicker"))


def test_should_return_straight_from_hand():
    hand = ["SJ", "H8", "H10", "DQ", "C9"]
    straight_hand = poker_score.get_straight_from_hand(hand)
    assert(straight_hand == ("H8", "C9", "H10", "SJ", "DQ"))


def test_should_return_empty_tuple_if_no_straight_in_hand():
    hand = ["SJ", "H8", "HA", "DQ", "C9"]
    straight_hand = poker_score.get_straight_from_hand(hand)
    assert(straight_hand == ())


def test_should_return_low_ace_straight_from_hand():
    hand = ["S4", "HA", "H3", "D5", "C2"]
    straight_hand = poker_score.get_straight_from_hand(hand)
    assert(straight_hand == ("HA", "C2", "H3", "S4", "D5"))


def test_should_return_high_ace_straight_from_hand():
    hand = ["SJ", "HA", "H10", "DQ", "CK"]
    straight_hand = poker_score.get_straight_from_hand(hand)
    assert(straight_hand == ("H10", "SJ", "DQ", "CK", "HA"))


def test_should_return_straights_from_players():
    hands = [
        ["SJ", "H8", "HK", "D2", "C4"],
        ["C7", "H3", "DA", "C8", "S9"],
        ["SA", "HJ", "DQ", "DK", "C10"],
    ]
    winning_cards = poker_score.get_straights(hands)
    assert(winning_cards == ({2: ("C10", "HJ", "DQ", "DK", "SA")}, "straight"))


def test_should_return_tied_straights():
    hands = [
        ["S6", "H4", "H5", "D2", "C3"],
        ["C7", "H3", "DA", "C8", "S9"],
        ["SA", "HJ", "DQ", "DK", "C10"],
    ]
    winning_hands = poker_score.get_winning_hands(hands)
    assert(winning_hands == ({
        0: ("D2", "C3", "H4", "H5", "S6"),
        2: ("C10", "HJ", "DQ", "DK", "SA")
    }, "straight"))


def test_should_return_flush_from_hand():
    hand = ["SJ", "SA", "S10", "SQ", "SK"]
    flush_hand = poker_score.get_flush_from_hand(hand)
    assert(flush_hand == ("SJ", "SA", "S10", "SQ", "SK"))


def test_should_return_flush_from_players():
    hands = [
        ["SJ", "S8", "SK", "S2", "S4"],
        ["C7", "H3", "DA", "C8", "S9"],
        ["HA", "HJ", "CQ", "HK", "H10"],
    ]
    flush_hands = poker_score.get_flushes(hands)
    assert(flush_hands == ({0: ("SJ", "S8", "SK", "S2", "S4")}, "flush"))


def test_should_return_tied_flushes():
    hands = [
        ["SJ", "S8", "SK", "S2", "S4"],
        ["C7", "H3", "DA", "C8", "S9"],
        ["HA", "HJ", "HQ", "HK", "H10"],
    ]
    flush_hands = poker_score.get_winning_hands(hands)
    assert(flush_hands == ({
        0: ("SJ", "S8", "SK", "S2", "S4"),
        2: ("HA", "HJ", "HQ", "HK", "H10")
    }, "flush"))


def test_should_return_full_house_from_hand():
    hand = ["SJ", "HJ", "S2", "CJ", "H2"]
    full_house = poker_score.get_full_house_from_hand(hand)
    assert(full_house == ("SJ", "HJ", "S2", "CJ", "H2"))


def test_should_return_full_house_from_players():
    hands = [
        ["SJ", "HJ", "S2", "CJ", "H2"],
        ["C7", "H3", "DA", "C8", "S9"],
        ["HA", "CK", "HK", "CA", "DA"],
    ]
    full_house_hands = poker_score.get_winning_hands(hands)
    assert(full_house_hands == ({
        0: ("SJ", "HJ", "S2", "CJ", "H2"),
        2: ("HA", "CK", "HK", "CA", "DA")
    }, "full house"))


def test_should_return_four_of_a_kind_from_hand():
    hand = ["SJ", "HJ", "DJ", "CJ", "H2"]
    four_of_a_kind_hand = poker_score.get_highest_group_from_hand(hand, 4)
    assert(four_of_a_kind_hand == ("SJ", "HJ", "DJ", "CJ"))


def test_should_return_four_of_a_kind_from_players():
    hands = [
        ["SJ", "HJ", "S2", "CJ", "H2"],
        ["SJ", "HJ", "DJ", "CJ", "H2"],
        ["HA", "CK", "HK", "CA", "DA"],
    ]
    four_of_a_kind_hands = poker_score.get_winning_hands(hands)
    assert(four_of_a_kind_hands == ({
        1: ("SJ", "HJ", "DJ", "CJ")
    }, "four of a kind"))


def test_should_return_four_of_a_kind_with_kicker_from_players():
    hands = [
        ["SJ", "HJ", "S2", "CJ", "H2"],
        ["SA", "HA", "DA", "CA", "H7"],
        ["HA", "CA", "H4", "SA", "DA"],
    ]
    four_of_a_kind_hands = poker_score.get_winning_hands(hands)
    assert(four_of_a_kind_hands == ({
        1: ("SA", "HA", "DA", "CA", "H7")
    }, "four of a kind with kicker"))


def test_should_return_tied_four_a_kind():
    hands = [
        ["SJ", "HJ", "S2", "CJ", "H2"],
        ["SA", "HA", "DA", "CA", "H7"],
        ["HA", "CA", "C7", "SA", "DA"],
    ]
    four_of_a_kind_hands = poker_score.get_winning_hands(hands)
    assert(four_of_a_kind_hands == ({
        1: ("SA", "HA", "DA", "CA", "H7"),
        2: ("HA", "CA", "SA", "DA", "C7")
    }, "four of a kind with kicker"))


test_should_return_higher_of_two_cards()
test_should_return_first_card_if_same_value()
test_should_return_highest_card_from_hand()
test_should_return_next_highest_card_when_tied_highest_value_in_hand()
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
test_should_remove_used_cards()
test_should_return_kicker_card_on_pair_tie()
test_should_return_three_of_a_kind_from_hand()
test_should_return_highest_three_of_a_kind_for_each_hand()
test_should_return_winning_three_of_a_kinds()
test_should_return_kicker_card_on_three_of_a_kind_tie()
test_should_return_kicker_card_on_high_card_tie()
test_should_return_kicker_cards_on_four_high_card_ties()
test_should_return_straight_from_hand()
test_should_return_empty_tuple_if_no_straight_in_hand()
test_should_return_low_ace_straight_from_hand()
test_should_return_high_ace_straight_from_hand()
test_should_return_straights_from_players()
test_should_return_tied_straights()
test_should_return_flush_from_hand()
test_should_return_flush_from_players()
test_should_return_tied_flushes()
test_should_return_full_house_from_hand()
test_should_return_full_house_from_players()
test_should_return_four_of_a_kind_from_hand()
test_should_return_four_of_a_kind_from_players()
test_should_return_four_of_a_kind_with_kicker_from_players()
test_should_return_tied_four_a_kind()
print("All passed!")
