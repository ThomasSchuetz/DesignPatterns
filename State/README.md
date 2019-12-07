# State pattern

## Wikipedia description (excerpt)

The state pattern allows an object to alter its behavior when its internal state changes. This can be a cleaner way for an object to change its behavior at runtime without resorting to conditional statements and thus improve maintainability.

## Main benefits

- Better testability: Class handling different states is broken down into smaller pieces that can be tested individually
- Better maintainability: Each state is represented within a separate class that is easier to handle than a large class containing all states

## Class diagram

![State pattern class diagram](https://upload.wikimedia.org/wikipedia/commons/e/ec/W3sDesign_State_Design_Pattern_UML.jpg "State pattern class diagram")

## Example

A simple example application is a turnstile. It can either be locked or unlocked. If it is locked, you may insert money (coins) until a certain amount has been reached.

![Turnstile activity diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Turnstile_state_machine_colored.svg/790px-Turnstile_state_machine_colored.svg.png "Turnstile activity diagram")
