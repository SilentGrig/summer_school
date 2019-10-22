import cardGame

ACE_HIGH = True


def get_higher_card(card_one, card_two):
    card_one_value = cardGame.getCardValue(card_one, ACE_HIGH)
    card_two_value = cardGame.getCardValue(card_two, ACE_HIGH)
    return card_one if card_one_value >= card_two_value else card_two


def get_highest_card_from_hand(hand):
    highest_card = None
    for card in hand:
        if not highest_card:
            highest_card = card
        else:
            highest_card = get_higher_card(highest_card, card)
    return highest_card


def get_highest_card_for_each_player(hands):
    highest_cards = []
    for hand in hands:
        highest_card_this_hand = get_highest_card_from_hand(hand)
        highest_cards.append(highest_card_this_hand)
    return highest_cards


def score_high_card(hands):
    highest_cards = get_highest_card_for_each_player(hands)
    winning_cards = {}
    for index, card in enumerate(highest_cards):
        if not card:
            continue
        if not winning_cards or cardGame.getCardValue(card, ACE_HIGH) > cardGame.getCardValue(list(winning_cards.values())[0][0], ACE_HIGH):
            winning_cards = dict([(index, (card,))])
        elif cardGame.getCardValue(card, ACE_HIGH) == cardGame.getCardValue(list(winning_cards.values())[0][0], ACE_HIGH):
            winning_cards[index] = (card, )
    return winning_cards


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
        if not highest_group or value > cardGame.getCardValue(highest_group[0], ACE_HIGH):
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
            continue
        if not winning_groups or cardGame.getCardValue(group[0], ACE_HIGH) > cardGame.getCardValue(list(winning_groups.values())[0][0], ACE_HIGH):
            winning_groups = dict([(index, group)])  # create new dict
        elif cardGame.getCardValue(group[0], ACE_HIGH) == cardGame.getCardValue(list(winning_groups.values())[0][0], ACE_HIGH):
            winning_groups[index] = group
    return winning_groups


def get_kicker_winners(hands, usedCards):
    updatedHands = handsRemovingUsedAndFoldedPlayers(hands, usedCards)
    kicker_cards = score_high_card(updatedHands)  # returns highest remaining high card
    winning_cards = {}
    for player, kicker_card in kicker_cards.items():
        winning_cards[player] = usedCards[player] + kicker_card
    return winning_cards


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


def get_triples(hands):
    winning_triples = score_group_cards(hands, 3)
    if winning_triples:
        if len(winning_triples) == 1:  # if only one player has pair they win
            return (winning_triples, "three of a kind")
        # if more than one player with three of a kind then determine winner(s) on remaining kicker
        # this should only happen with multiple decks
        return (get_kicker_winners(hands, winning_triples), "three of a kind with kicker")


def get_winning_hands(hands):
    # checking triples
    triples = get_triples(hands)
    if triples:
        return triples

    # checking pairs
    pairs = get_pairs(hands)
    if pairs:
        return pairs

    # checking high card if no other
    return (score_high_card(hands), "high card")


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
