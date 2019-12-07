# State pattern

## Wikipedia description (excerpt)

The state pattern allows an object to alter its behavior when its internal state changes. This can be a cleaner way for an object to change its behavior at runtime without resorting to conditional statements and thus improve maintainability.

## Main benefits

- Better testability: Class handling different states is broken down into smaller pieces that can be tested individually
- Better maintainability: Each state is represented within a separate class that is easier to handle than a large class containing all states

## Class diagram

## Example

A simple example application is a turnstile. It can either be locked or unlocked. If it is locked, you may insert money (coins) until a certain amount has been reached.

https://en.wikipedia.org/wiki/File:Turnstile_state_machine_colored.svg