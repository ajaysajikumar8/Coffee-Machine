# Coffee Maker

This is a virtual coffee maker. There are three types of coffee for you: Latte, Cappuccino and Espresso. After you select your coffee, You have to pay.

The payment is done through coins. The cost of each type of coffee is given below:

* Espresso: $1.5,
* Latte: $2.5,
* cappuccino: $3.0.

If the user has inserted too much money, the machine should offer change.
E.g.

    “Here is $2.45 dollars in change.” 

When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.

    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5

When the user chooses a drink, the program should check if there are enough resources to make that drink.
E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print:

    “Sorry there is not enough water.”
