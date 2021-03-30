+++
title = "The strategy pattern"
menuTitle = "Strategy"
description = ""
author = "razoric"

date = 2021-03-30
weight = 5

difficulty = "intermediate"
keywords = ["godot design patterns", "godot strategy pattern"]
+++

The Strategy pattern defines a _family_ of algorithms, each coded in a separate class with the same interface.

Another class can then use them interchangeably and delegate the implementation details to those sub-classes.

The pattern mostly helps to prevent a class from growing too big by splitting some of its features into multiple files and classes, separating concerns. It also helps to avoid merge conflicts when working with a team.

## The problem

You are making a multiplayer game.

You have a lot of communication with that central server to make the game function, keep it fair and cheat-free, and save data so players can leave and come back without losing their progress.

Since the entire game needs to ask the server questions and send requests frequently, you make your `ServerConnection` class a global singleton in Godot's Autoload tab.

When you need to save some data, you call `save_player_data()`, and when you want to send some gameplay update, like an input event or a change in position, you call `send_player_update()`.

Likewise, you may also have functions like `send_player_chat()`, `choose_game_lobby()`, `get_friends_list()`, and so on.

Your `ServerConnection` class soon grows large. Whenever you want to make a change, you need to scroll through the endless list of functions to find the one to edit.

Then you have teammates. When one teammate tries to change the player data storage function while another tries to change the player update loop, the source control complains about merge conflicts.

They both tried to change the same file simultaneously, and now you have to pick and choose which parts you need to keep.

There has to be a better way, right?

## The solution

Enter the Strategy pattern.

In this pattern, you wrap an algorithm or set of work inside an object with a known interface.

The strategy-caller delegates the work of figuring out _how_ to do a task to the strategies.

Following the `ServerConnection` example, instead of putting all the work inside the class, we could split it into different modules.

You have the `Storage` module, the `FriendsList` module, along with `Chat` and `GameData`. Each one exposes some functions, like `save_data()` or `send_message()`.

The `ServerConnection` class does not need to know _how_ the function call will happen. _How_ is a job for the modules.

Those modules are the strategies. They are special classes that extend those interfaces.

The use of the strategy pattern splits the work a single class has to do into specialized classes, which you can freely use to delegate tasks without knowing how each strategy works.

You can even swap out one strategy for another for the same module. For example, you can replace the chat module that sends data to the server with one that pretends to so you can test your chat code even when you're offline.

That's where the idea of interchangeability comes in handy. As all strategy classes follow the same code interface, you can replace them anytime.

## Implementations

Let's look at some examples of how you would build this pattern in Godot.

We'll continue with the server connection and chat theme. We have a central `ServerConnection` class, and we want to split it up into modules responsible for individual parts.

_Note that the code below is for demonstration only. Real-world network code would get a bit big, so I've made a simple fictional example._

_To see how we use the idea behind this pattern in a real-world example, see the [Nakama Godot demo](https://github.com/heroiclabs/nakama-godot-demo). In particular, the `Autoload/Delegates/` directory._

All strategies have a known public interface that gets overridden by sub-classes.

Our chat code should be able to call a function to send a message, and connect to a signal to receive them from the game server.

We begin with a base class that exposes that interface. We also add a function we can call to establish a connection and configure everything.

```gdscript
class_name ChatStrategy
extends Reference

## Emitted by the strategy when a message arrives.
signal received_message(message)


## Sets up the chat connection and connects to required signals using built-in data.
func setup() -> void:
    pass


## Sends a message to the server if connected. Otherwise, prints an error message.
func send_message(message) -> void:
    pass
```

This is the base for our strategy and all that the connection class needs to know about. To make it actually useful, we extend it and replace those `pass` statements with useful work.

```gdscript
class_name ServerChatStrategy
extends ChatStrategy

var server_address = ""
var connection: Connection
var game_id = ""


func setup() -> void:
    # If we lack an address to connect to, complain and return.
    if server_address.empty():
        print("Error, no server to connect to.")
        return

    # Use a third-party code library of some kind to connect to the server.
    # Because connecting takes time, we use a yield statement to wait until the
    # job finishes.
    connection = yield(NetworkAPI.connect_async(server_address, 5555), "completed")
    
    # If we failed to connect, complain and return.
    if not connection:
        print("Error, cannot connect to server %s:5555" % [server_address])
        return
    
    # Get data out of the connection and connect signals.
    game_id = connection.get_room_id()
    connection.connect("received_message", self, "_on_received_message")


func send_message(message) -> void:
    # If we're not connected, complain and return.
    if not connection:
        print("Error, no connection.")
        return
    
    # Encode the data into a format the server expects.
    var data = {"msg": message}
    
    # Because sending a message over the internet takes time, we use a yield
    # statement to wait until the job finishes.
    var result = yield(connection.send_chat_message_async(game_id, data), "completed")
    
    # If something went wrong, complain and return.
    if not result.error_code == OK:
        print("Error, failed to send chat. Error code %s" % [result.error_code])


func _on_received_message(sender, message) -> void:
    # Echo the message into a format our game expects.
    emit_signal("received_message", "%s: %s" % [sender, message])
```

We can create different kinds of strategies that have the same interface. For example, you can create a class that is all about testing without actually needing to connect to a server, which takes time or would fail because the server isn't online yet.

```gdscript
class_name TestChatStrategy
extends ChatStrategy


func send_message(message) -> void:
    emit_signal("received_message", "Test, echoing back: %s" % [message])
```

Now, we can replace the chat functions in `ServerConnection` that made it so long with the appropriate strategy.

```gdscript
const TESTING := false
var chat: ChatStrategy


func setup() -> void:
    if TESTING:
        chat = TestChatStrategy.new()
    else:
        chat = ServerChatStrategy.new()
        chat.server_address = "127.0.0.1"
    chat.setup()
    chat.connect("received_message", self, "_on_Chat_received_message")


func send_chat_message(message: String) -> void:
    if not chat:
        return
    
    chat.send_message(message)
    GUI.print_chat_message(message)


func _on_Chat_received_message(message: String) -> void:
    GUI.print_chat_message(message)
```

Now, your teammate working on chat connection can edit `ServerChatStrategy.gd` without impacting the developer working server storage.

This also makes `ServerConnection` a lot smaller as you can get rid of every private function that deals with the logic of sending or receiving messages.

Those details are part of the strategy now. Your `ServerConnection` class delegates the work to specialists.

It uses the single-responsibility principle for Object-Oriented Programming.

`ServerConnection`'s job is connecting to servers. `ChatStrategy`'s job is to handle the chat.

You can apply this idea to `DataStorage`, `FriendList`, so on and so forth. How granular you get depends on your particular project.

Still, the Strategy pattern is there to help you break down your classes that are growing too large and too unwieldy into iteration-friendly chunks and delegates.

