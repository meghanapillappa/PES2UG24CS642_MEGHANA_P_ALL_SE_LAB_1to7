from cards import Deck, hand_value


def is_natural(hand):
    """A natural blackjack is a two-card 21."""
    return len(hand) == 2 and hand_value(hand) == 21


def fmt(card):
    return f"{card[0]}{card[1]}"


class Blackjack:
    def __init__(self):
        self.chips = 100

    def show(self, player, dealer, hide=True):
        if hide:
            print("Dealer: ??")
        else:
            print("Dealer:", " ".join(fmt(c) for c in dealer),
                  "=", hand_value(dealer))
        print("Player:", " ".join(fmt(c) for c in player),
              "=", hand_value(player))

    def ask_wager(self):
        """Ask for a wager until valid. Returns None if the player quits.
        Invalid input never changes chips."""
        while True:
            raw = input(f"Chips: {self.chips}. Wager (1-{self.chips}) or [q]uit: ").strip().lower()
            if raw == "q":
                return None
            if not (raw.isascii() and raw.isdigit()):
                print("Invalid wager. Enter a whole number.")
                continue
            bet = int(raw)
            if bet < 1 or bet > self.chips:
                print(f"Invalid wager. Must be between 1 and {self.chips}.")
                continue
            return bet

    def ask_play_again(self):
        while True:
            raw = input("Play again? [y/n]: ").strip().lower()
            if raw == "y":
                return True
            if raw == "n":
                return False
            print("Invalid input. Enter y or n.")

    def settle(self, outcome, bet):
        """Update chips for a finished round. Called exactly once per round."""
        if outcome == "blackjack":
            win = bet * 3 // 2  # pays 3:2, rounded down
            self.chips += win
            print(f"Blackjack pays 3:2. Player wins +{win}.")
        elif outcome == "player":
            self.chips += bet
            print(f"Player wins +{bet}.")
        elif outcome == "dealer":
            self.chips -= bet
            print(f"Dealer wins -{bet}.")
        else:
            print("Push. Bet returned.")
        print("Chips:", self.chips)

    def play_hand(self):
        """Play one hand. Returns the outcome, or None if the player quit.
        Does not touch chips; settlement happens once in round()."""
        deck = Deck()
        player = [deck.draw(), deck.draw()]
        dealer = [deck.draw(), deck.draw()]
        self.show(player, dealer)

        # Natural blackjack: resolve immediately
        p_nat, d_nat = is_natural(player), is_natural(dealer)
        if p_nat or d_nat:
            self.show(player, dealer, hide=False)
            if p_nat and d_nat:
                print("Both have blackjack.")
                return "push"
            if p_nat:
                print("Blackjack!")
                return "blackjack"
            print("Dealer has blackjack.")
            return "dealer"

        # Player turn
        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()
            if key == "q":
                return None
            if key == "s":
                break
            if key == "h":
                card = deck.draw()
                player.append(card)
                print("You drew", fmt(card))
                self.show(player, dealer)
                if hand_value(player) > 21:
                    print("Bust.")
                    return "dealer"
            else:
                print("Invalid command. Use h, s, or q.")

        # Dealer turn: reveal, then draw until 17 or more
        print("Dealer reveals.")
        self.show(player, dealer, hide=False)
        drew = False
        while hand_value(dealer) < 17:
            card = deck.draw()
            dealer.append(card)
            drew = True
            print("Dealer draws", fmt(card))
        if drew:
            self.show(player, dealer, hide=False)

        pv, dv = hand_value(player), hand_value(dealer)
        if dv > 21:
            print("Dealer busts.")
            return "player"
        if pv > dv:
            return "player"
        if pv < dv:
            return "dealer"
        return "push"

    def round(self):
        bet = self.ask_wager()
        if bet is None:
            return False
        outcome = self.play_hand()
        if outcome is None:  # quit mid-hand: bankroll unchanged
            return False
        self.settle(outcome, bet)
        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)
        while self.chips > 0:
            if not self.round():
                return
            if self.chips <= 0:
                break
            if not self.ask_play_again():
                return
        print("Out of chips. Game over.")