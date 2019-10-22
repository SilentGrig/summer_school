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


def get_highest_pair_from_hand(hand):
    grouped_cards = get_cards_grouped_by_value(hand)
    highest_pair = ()
    for value, cards in grouped_cards.items():
        if not len(cards) == 2:
            continue
        if not highest_pair or value > cardGame.getCardValue(highest_pair[0], ACE_HIGH):
            highest_pair = tuple(cards)
    return highest_pair


def get_highest_pair_per_player(hands):
    highest_pairs = []
    for hand in hands:
        highest_pair_from_hand = get_highest_pair_from_hand(hand)
        highest_pairs.append(highest_pair_from_hand)
    return highest_pairs


def score_pair_cards(hands):
    highest_pairs = get_highest_pair_per_player(hands)
    winning_pairs = {}
    for index, pair in enumerate(highest_pairs):
        if not pair:
            continue
        if not winning_pairs or cardGame.getCardValue(pair[0], ACE_HIGH) > cardGame.getCardValue(list(winning_pairs.values())[0][0], ACE_HIGH):
            winning_pairs = dict([(index, pair)])  # create new dict
        elif cardGame.getCardValue(pair[0], ACE_HIGH) == cardGame.getCardValue(list(winning_pairs.values())[0][0], ACE_HIGH):
            winning_pairs[index] = pair
    return winning_pairs


def get_kicker_winners(hands, usedCards):
    updatedHands = handsRemovingUsedAndFoldedPlayers(hands, usedCards)
    kicker_cards = score_high_card(updatedHands)  # returns highest remaining high card
    winning_cards = {}
    for player, kicker_card in kicker_cards.items():
        winning_cards[player] = usedCards[player] + kicker_card
    return winning_cards


def get_second_pairs(hands, usedCards):
    updatedHands = handsRemovingUsedAndFoldedPlayers(hands, usedCards)
    second_pair_cards = score_pair_cards(updatedHands)  # returns highest remaining high card
    if not second_pair_cards:
        return None
    winning_cards = {}
    for player, kicker_card in kicker_cards.items():
        winning_cards[player] = usedCards[player] + kicker_card
    return winning_cards


def get_winning_hands(hands):
    # checking pairs
    winning_pairs = score_pair_cards(hands)
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

    # checking high card
    high_cards = score_high_card(hands)
    return (high_cards, "high card")


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
