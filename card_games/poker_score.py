import cardGame

ACE_HIGH = True


def get_higher_card(card_one, card_two):
    card_one_value = cardGame.getCardValue(card_one, ACE_HIGH)
    card_two_value = cardGame.getCardValue(card_two, ACE_HIGH)
    return card_one if card_one_value >= card_two_value else card_two


def get_highest_card_from_hand(hand):
    highest_card = None
    for card in hand:
        if highest_card is None:
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
    winning_cards = None
    for index, card in enumerate(highest_cards):
        if winning_cards is None or cardGame.getCardValue(card, ACE_HIGH) > cardGame.getCardValue(winning_cards[0][1], ACE_HIGH):
            winning_cards = [(index + 1, card)]
        elif cardGame.getCardValue(card, ACE_HIGH) == cardGame.getCardValue(winning_cards[0][1], ACE_HIGH):
            winning_cards.append((index + 1, card))
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
    highest_pair = None
    for value, cards in grouped_cards.items():
        if not len(cards) == 2:
            continue
        if highest_pair is None or value > cardGame.getCardValue(highest_pair[0]):
            highest_pair = tuple(cards)
    return highest_pair
