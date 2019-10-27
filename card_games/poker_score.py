import cardGame

ACE_HIGH = True


def get_higher_card(card_one, card_two):
    card_one_value = cardGame.getCardValue(card_one, ACE_HIGH)
    card_two_value = cardGame.getCardValue(card_two, ACE_HIGH)
    return card_one if card_one_value >= card_two_value else card_two


def get_cards_grouped_by_value(hand):
    card_groups = {}
    for card in hand:
        card_value = cardGame.getCardValue(card, ACE_HIGH)
        if card_value not in card_groups:
            card_groups[card_value] = [card]
        else:
            card_groups[card_value].append(card)
    return card_groups


def get_highest_group_from_hand(hand, groupSize):
    grouped_cards = get_cards_grouped_by_value(hand)
    highest_group = ()
    for value, cards in grouped_cards.items():
        if not len(cards) == groupSize:
            continue
        if not highest_group or value > get_card_value_from_list_of_cards(highest_group):
            highest_group = tuple(cards)
    return highest_group


def get_highest_group_per_player(hands, groupSize):
    highest_groups = []
    for hand in hands:
        highest_group_from_hand = get_highest_group_from_hand(hand, groupSize)
        highest_groups.append(highest_group_from_hand)
    return highest_groups


def score_group_cards(hands, groupSize):
    highest_groups = get_highest_group_per_player(hands, groupSize)
    winning_groups = {}
    for index, group in enumerate(highest_groups):
        if not group:
            continue  # if player doesn't have cards for group size, out of round
        highest_value_in_group = get_card_value_from_list_of_cards(group)
        highest_value_in_winning_groups = get_highest_card_value_so_far(winning_groups)
        if not winning_groups or highest_value_in_group > highest_value_in_winning_groups:
            winning_groups = dict([(index, group)])  # replace old winning group
        elif highest_value_in_group == highest_value_in_winning_groups:
            winning_groups[index] = group
    return winning_groups


def get_card_value_from_list_of_cards(group):
    # get first card from group - all cards in group have same value
    return cardGame.getCardValue(group[0], ACE_HIGH)


def get_highest_card_value_so_far(winning_groups):
    if not winning_groups:
        return None
    first_group = list(winning_groups.values())[0]
    return get_card_value_from_list_of_cards(first_group)


def get_kicker_winners(hands, usedCards):
    if len(usedCards) == 1 or not hands[0]:
        return usedCards
    updatedHands = handsRemovingUsedAndFoldedPlayers(hands, usedCards)
    kicker_cards = score_group_cards(updatedHands, 1)  # returns highest remaining high card
    winning_cards = {}
    for player, kicker_card in kicker_cards.items():
        winning_cards[player] = usedCards[player] + kicker_card
    return get_kicker_winners(updatedHands, winning_cards)


def get_second_pairs(hands, usedCards):
    updatedHands = handsRemovingUsedAndFoldedPlayers(hands, usedCards)
    second_pair_cards = score_group_cards(updatedHands, 2)  # returns highest remaining high card
    if not second_pair_cards:
        return None
    winning_cards = {}
    for player, kicker_card in kicker_cards.items():
        winning_cards[player] = usedCards[player] + kicker_card
    return winning_cards


def get_pairs(hands):
    winning_pairs = score_group_cards(hands, 2)
    if winning_pairs:
        if len(winning_pairs) == 1:  # if only one player has pair they win
            return (winning_pairs, "one pair")
        second_pairs = get_second_pairs(hands, winning_pairs)
        if not second_pairs: # if no second players check for kicker high card
            return (get_kicker_winners(hands, winning_pairs), "one pair with kicker")
        if len(second_pairs) == 1:  # if only one player has second pair they win
            return (second_pairs, "two pairs")
        # if more than one player with two pairs determine winner(s) on remaining kicker
        return (get_kicker_winners(hands, second_pairs), "two pairs with kicker")
    return None


def get_triples(hands):
    winning_triples = score_group_cards(hands, 3)
    if winning_triples:
        if len(winning_triples) == 1:  # if only one player has pair they win
            return (winning_triples, "three of a kind")
        # if more than one player with three of a kind then determine winner(s) on remaining kicker
        return (get_kicker_winners(hands, winning_triples), "three of a kind with kicker")
    return None


def get_high_cards(hands):
    high_cards = score_group_cards(hands, 1)
    if len(high_cards) == 1:
        return (high_cards, "high card")
    return (get_kicker_winners(hands, high_cards), "high card with kicker")


def handsRemovingUsedAndFoldedPlayers(hands, usedCards):
    newHands = []
    for index, hand in enumerate(hands):
        newHands.append([])
        if index not in usedCards:
            continue
        for card in hand:
            if card not in usedCards[index]:
                newHands[index].append(card)
    return newHands


def get_straight_from_hand(hand):
    hand_copy = hand.copy()
    hand_has_two_card = cardGame.doesHandContainValue(hand, 2)
    # if hand has a two card then treat Ace has low card to check for straight
    if hand_has_two_card:
        cardGame.sortHandByRank(hand_copy, aceHigh=False)
        last_card_value = cardGame.getCardValue(hand_copy[0], aceHigh=False)
    else:
        cardGame.sortHandByRank(hand_copy, ACE_HIGH)
        last_card_value = cardGame.getCardValue(hand_copy[0], ACE_HIGH)

    for i in range(1, len(hand)):
        card_value = cardGame.getCardValue(hand_copy[i], ACE_HIGH)
        if not card_value == last_card_value + 1:
            return ()  # if no straight don't return any cards
        last_card_value = card_value

    return tuple(hand_copy)


def get_matching_hands(hands, handCheck, checkType):
    matchedHands = {}
    for player, hand in enumerate(hands):
        matchedHand = handCheck(hand)
        if matchedHand:
            matchedHands[player] = matchedHand
    if not matchedHands:
        return None
    return (matchedHands, checkType)


def get_straights(hands):
    return get_matching_hands(hands, get_straight_from_hand, "straight")


def get_flush_from_hand(hand):
    first_suit = cardGame.getCardSuit(hand[0])
    for i in range(1,len(hand)):
        card_suit = cardGame.getCardSuit(hand[i])
        if not card_suit == first_suit:
            return None
    return tuple(hand)


def get_flushes(hands):
    return get_matching_hands(hands, get_flush_from_hand, "flush")


def get_full_house_from_hand(hand):
    grouped_cards = get_cards_grouped_by_value(hand)
    # there must be two groups of cards for full house
    if not len(grouped_cards) == 2:
        return None
    for group in list(grouped_cards.values()):
        # each group should be 2 or 3 cards in length
        # not 1 or 4 cards in length
        if not (len(group) == 2 or len(group) == 3):
            return None
    return tuple(hand)


def get_full_houses(hands):
    return get_matching_hands(hands, get_full_house_from_hand, "full house")


def get_four_of_a_kinds(hands):
    winning_fours = score_group_cards(hands, 4)
    if winning_fours:
        if len(winning_fours) == 1:  # if only one player has pair they win
            return (winning_fours, "four of a kind")
        # if more than one player with three of a kind then determine winner(s) on remaining kicker
        return (get_kicker_winners(hands, winning_fours), "four of a kind with kicker")
    return None


def get_winning_hands(hands):
    # checking four of a kind
    four_of_a_kinds = get_four_of_a_kinds(hands)
    if four_of_a_kinds:
        return four_of_a_kinds

    # checking full houses
    full_houses = get_full_houses(hands)
    if full_houses:
        return full_houses

    # checking flushes
    flushes = get_flushes(hands)
    if flushes:
        return flushes

    # checking straights
    straights = get_straights(hands)
    if straights:
        return straights

    # checking triples
    triples = get_triples(hands)
    if triples:
        return triples

    # checking pairs
    pairs = get_pairs(hands)
    if pairs:
        return pairs

    # checking high card if no other
    return get_high_cards(hands)
