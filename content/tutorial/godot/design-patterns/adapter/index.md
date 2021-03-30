+++
title = "The adapter pattern"
menuTitle = "Adapter"
description = ""
author = "razoric"

date = 2021-03-30
weight = 5

difficulty = "intermediate"
keywords = ["godot design patterns", "godot adapter pattern"]
+++

_The Adapter acts as a wrapper between two objects. It catches calls meant for one object and transforms them into a format that is recognizable for another._

## The problem

You're making an RPG that involves quests. You could code it yourself, but you got recommended a neat code asset with a quest system built-in. It's open-source and permissive, so long as you give credit where credit is due.

That's a lot of time saved, and it has everything you need to make quest chains!

But then you start looking at the API and realize that, to make the quest system detect the inventory, it expects a `CharacterInventory` class they coded with an "inventory_filled" signal and a `get_inventory_list()` function.

Your inventory does not have a `CharacterInventory` class. It has a `Inventory`, with a "inventory_changed" signal and a `get_all_inventory()` function instead.

Does that mean you need to ditch this cool quest system and code it yourself after all?

## The solution

Thankfully not. What you can do instead is to create an Adapter. It's a way of putting square pegs in holes that expect round pegs, comparing oranges to apples, and making cars run on train tracks.

- You have some `Client` class that expects a specific object type.
- The `Target` class is the class the `Client` expects.
- You have an incompatible `Adaptee` that works with your system, but not with `Client`
- You create an `Adapter` class that _extends_ `Target` and holds a reference to the `Adaptee`.

When the `Client` calls a function that expects data from the `Target`, you instead call a different function that returns `Adaptee`'s data in a format `Client` recognizes.

## Example

Let's take the example of a quest system. Specifically, this is the part of the system that can trigger a quest moving on or becoming completed when the character collects an item they need. This is a system you did not create. You got it online and want to use it.

```gdscript
class_name QuestSystem
extends Node


var _inventory: CharacterInventory
var _current_quest: Quest


## Sets the system's reference to the player inventory and connects to a signal
## triggered when the inventory gets a new piece of inventorty.
func setup(inventory: CharacterInventory) -> void:
    _inventory = inventory
    inventory.connect("inventory_filled", self, "_on_CharacterInventory_inventory_filled")


## Whenever the inventory changes and the quest needs the inventory,
## we provide the quest with a list of inventory items and, if it's the one we
## needed, we make the quest move forwards to the next step.
func _on_CharacterInventory_inventory_filled() -> void:
    if _current_quest and _current_quest.objective is InventoryObjective:
        var all_items := _inventory.get_inventory_list()

        if _current_quest.check_for_items(all_items):
            _current_quest.advance_quest()
```

We know the `CharacterInventory` class has a "inventory_filled" signal, and a `get_inventory_list()` function that returns an array of `QuestItem`s.

But your inventory has an "inventory_changed" signal and a `get_all_inventory()` function that returns an array of `Item`s. It's incompatible.

Besides that, the class types don't match, and it wouldn't accept it anyway.

To put this `Inventory` class into the `QuestSystem`, we need a translation layer. That's the Adapter. It will be a subclass of `CharacterInventory` and override all the functions `QuestSystem` expects to use and return data, so it's translated into a format it understands.

```gdscript
class_name InventoryAdapter
extends CharacterInventory


var _inventory: Inventory


func setup(inventory: Inventory) -> void:
    _inventory = inventory
    _inventory.connect("inventory_changed", self, "emit_signal", ["inventory_filled"])


func get_inventory_list() -> Array:
    var output := []
    var inventory_items := _inventory.get_all_inventory()
    for item in inventory_items:
        var quest_item := QuestItem.new()
        quest_item.name = item.name
        quest_item.quantity = item.quantity
        quest_item.id = item.id
        
        output += quest_item
    
    return output
```

You'd repeat this process with every other function with some inventory data that is incompatible with the current function. Now, when you instance your quest system and set it up, you have a handy class you can use to pass along without needing to change either the quest system or your inventory system.

```gdscript
onready var quest_system := $QuestSystem
onready var inventory := $Inventory


func _ready() -> void:
    var inventory_adapter := InventoryAdapter.new()
    inventory_adapter.setup(inventory)
    
    quest_system.setup(inventory_adapter)
    quest_system.start_quest("Tutorial")
```

No one is any the wiser about the subterfuge, and everything works invisibly (at least, so long as you don't forget any function or signal).

## Usage

If you write all your game's code yourself, you won't need the Adapter pattern often. But there are cases where it could happen. If you coded previous projects and you'd like to re-use the code from them into your new game, but you find that they don't play nicely with one another, the Adapter can help out.

It could also come into play when refactoring code later down the line of a growing project. You could code a particular system and discover only weeks or months down the line that it could be useful with some of your existing classes. Instead of re-making either the old system or the old targets, you can create an Adapter to stand between the two.

Where it truly shines is when you bring in code from outside sources. This is code you either do not have access to (like a closed-source C++ library), or would be prohibitively expensive on time to change (a complex codebase). It comes into play when you already have your own code in place that you do not want or cannot change.
