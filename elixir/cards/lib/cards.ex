defmodule Cards do
  #arity is the number of argument passed to function
  def create_deck do
    values=["Ace","Two","Three","Four","Five"]
    suits = ["Spades","Clubs","Hearts","Diamond"]
    #list comprehension
     for value <- values, suit <- suits do
        "#{value} of #{suit}"
      end
  end

  def shuffle(deck) do
    Enum.shuffle(deck)
  end

  def contains?(deck, card) do
    Enum.member?(deck,card)
  end

  def deal(deck, head_size) do
    Enum.split(deck,head_size)
  end


end
