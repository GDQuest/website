---
author: razoric
coAuthor:
- nathan
date: "2021-03-30T00:00:00-06:00"
description: ""
difficulty: intermediate
keywords:
- godot best practices
- godot save
- godot save game
menuTitle: Save formats
software: godot
title: Choosing the right save game format
weight: 5
---

Frequently, we see questions come up about saving the player's game data. The questions are often about what that file should look like.

There's no single answer as all situations are unique. But there are some guidelines you can follow to guide your choice better in the process.

In this guide, you'll learn:

1. How to choose an appropriate data format for your savegames.
1. How to save data to binary, JSON, and native text with Godot.
1. What are the pros and cons of each of these formats.

## Allowing players to read edit save data

If you want your players to either read or edit savegames, your file format should be text-based. Anyone can open such a file in a text editor to see and edit the data in a text editor.

If you must store complex binary objects, you should store them separately to keep the text file lightweight and editable. For example, if the player can draw a flag in-game and you want to save that image to the disk, it should be separate from the savegame.

Either that or you would have to create a tool for your player to see and edit the data.

## Preventing players from reading the saved data

If you want to prevent players from reading the saved data, whether it's to slow down cheating or data mining, you should use binary files.

To do so, you will use the `store_*()` functions in Godot's [File](https://docs.godotengine.org/en/stable/classes/class_file.html) class. They convert values to chains of ones and zeros.

Binary makes it harder for most people to use the data, although some still can. Programmers or people who are savvy with hex editors can figure out your system with some patience.

To further slow them down while reverse-engineering your data format, you can save and load data in a particular order and omit variable names in the file.

Binary also creates small and compact files since it takes out all the extra characters text-based files require for parsing. But you _must_ load the file in the same order you saved it and need to encode certain variable types appropriately.

Below, you'll find an example of saving character data to binary. We will later show you how to save the same data in JSON, then a convenient and lightweight Godot text format.

Each character has an age (integer), a name (text string), and a position on the map (Vector2).

Here's the data we'll save:

1. Larry, 50 years old, at position `Vector2(120.206, 119.449)`
1. Harry, 25 years old, at position `Vector2(211.11, 107.883)`

With two characters, in binary, the savegame has a size of **42 bytes**.

Here's the code to save and load that binary data.

```gdscript
## Exports relevant data for a character in binary to the provided `File`. Each piece of
## data is in binary, non-human readable format.
func export_to_bin(file: File) -> void:
	# Store an integer as a 32-bit number, a value between -2,147,483,648 and 2,147,483,647
	file.store_32(age)

	# Store the length of a string as a 32-bit number. In binary, we have no way to know
	# if one byte or the next is part of a variable except by writing how many to expect.
	# The result is the number of characters to load later, followed by the string.
	file.store_32(character_name.length())
	file.store_string(character_name)

	# Store a Vector2 using its constituent X and Y parts as floating-point numbers:
	# 32-bit numbers that have a decimal number component.
	file.store_float(position.x)
	file.store_float(position.y)


## Imports the relevant class data from the provided binary `File`. Expects the
## the caret to be at the start of the data. The data must load in the same order
## it was saved in.
func import_from_bin(file: File) -> void:
	# Gets an integer from a 32-bit piece of binary data.
	age = file.get_32()

	# Gets the number of characters that make up the follow-up string, then
	# get each one as an 8-bit number - one byte - and transform it into a string
	# using the `char()` function. This uses the standardized ASCII table for the text.
	var name_length := file.get_32()
	character_name = ""
	for i in name_length:
		character_name += char(file.get_8())

	#Load a Vector2 out of its constituent X and Y parts from floating-point numbers.
	position.x = file.get_float()
	position.y = file.get_float()
```

With the example above, you would call `export_to_bin()` once for each character you want to save.

Here's how you would use the code example you just saw.

```gdscript
const SAVE_BINARY := "user://save.dat"

## Saves children to a binary file.
func save_binary() -> void:
	# Initializes a new `File` and opens the file in write mode, creating it
	# if it's missing.
	var file := File.new()
	file.open(SAVE_BINARY, File.WRITE)

	# For each child, pass in the handle to the file and have the child write
	# its data.
	for child in get_children():
		child.export_to_bin(file)

	# Clean up and close the file so the operating system can claim it
	file.close()


## Loads children from a binary file.
func load_binary() -> void:
	# Initializes a new `File` and open the file in read mode. If it's missing
	# or otherwise un-openable, report it as an error and return.
	var file := File.new()
	var error := file.open(SAVE_BINARY, File.READ)

	if not error == OK:
		print_error("Could not load file at %s" % SAVE_BINARY)
		return

	# Have each child import its data in the same order they were saved in.
	for child in get_children():
		child.import_from_bin(file)

	# Clean up and close the file so the operating system can claim it.
	file.close()
```

We directly apply the loaded data to child nodes, but you don't necessarily have to do this to load the data. We used this example for simplicity.

## Taking save data into other software

What if you want to save and export data to use in other programs?

When you step outside Godot, you want a format that is universal across platforms. There are popular text-based ones like YAML, TOML, or XML. In Godot, the format of choice is JSON, one of the best-supported ones out there.

It's lightweight, has universal support in other programming languages and libraries, is integral to web development, and supports complex objects through dictionaries and arrays. In JSON, the data's order does not matter, except in arrays since dictionaries have no order. With it, you can save variable names as keys to make loading easier.

Note that you don't have to use a text-based interchange format. Other programming languages also have the concept of 8, 16, 32, or 64-bit numbers, strings, and variables. If you do not want to use a human-readable format like JSON, you can save in binary and use the other language's facilities to load the data like C++'s `ifstream` or C's `fread`.

Once again, we'll save our two characters, Larry and Harry. Here's the JSON our code example outputs. Its final size is **160 bytes** non-minified, in this readable form, as opposed to the 42 bytes of our binary version.

```json
[
  {
    "age": 50,
    "character_name": "Larry",
    "position": {
      "x": 120.046242,
      "y": 119.111282
    }
  },
  {
    "age": 25,
    "character_name": "Harry",
    "position": {
      "x": 211.275574,
      "y": 108.217361
    }
  }
]
```

Here's the code that generates this JSON.

```gdscript
## Exports relevant class data in a dictionary that will be converted into a JSON
## format by by the saving class. The variable names match to make it easier to
## read and load later.
func export_to_dict() -> Dictionary:
	return {
		"age": age,
		"character_name": character_name,
		"position": {"x": position.x, "y": position.y}
	}


## Imports relevant class data from a dictionary that was loaded from JSON data.
func import_from_dict(dict: Dictionary) -> void:
	age = dict.age
	character_name = dict.character_name
	position.x = dict.position.x
	position.y = dict.position.y
```

As you can see, all we have to do is to output and read a dictionary for each character. However, notice how we have to split our `position`, a Vector2, into two numbers.

To save that data to a file, we store all our characters' dictionary in an array and call `JSON.print()` to convert the data to a JSON string.

To load the JSON from the disk, we use `JSON.parse()` instead.

```gdscript
const SAVE_JSON := "user://save.json"

## The saving class' method for saving a file to JSON.
func save_json() -> void:
	# Gather each dictionary from each children to save into a single array
	var output := []
	for child in get_children():
		output.push_back(child.export_to_dict())

	# Convert the array, and its dictionaries, using the `JSON` singleton
	# into a block of JSON. Note the second parameter that specifies how to
	# indent the file. Without this parameter, the JSON would be on a single line.
	var json := JSON.print(output, "  ")

	# Save the resulting JSON to a file using the `File` class in write mode
	var file := File.new()
	file.open(SAVE_JSON, File.WRITE)

	# Since our JSON is indented, we can store the entire string in one call.
	file.store_string(json)

	# Clean up
	file.close()


## The saving class' method for loading a file to JSON and spreading the data
## back to its children.
func load_json() -> void:
	# Load the file using the `File` class in read mode. Report an error if the
	# file is missing or cannot be opened.
	var file := File.new()
	var error := file.open(SAVE_JSON, File.READ)

	if not error == OK:
		print_error("Could not load file at %s" % SAVE_JSON)
		return

	# Get the array of dictionaries from the file. Note that we load the entire
	# file with get_as_text because our JSON is on multiple lines.
	var input := file.get_as_text()

	# Clean up
	file.close()

	# Use the JSON singleton to parse the string into an array of dictionaries.
	# JSON.parse returns JSONParseResult, in case of errors, and the actual
	# array is in the `result` property.
	var json: Array = JSON.parse(input).result

	# In the same order as they were saved, we iterate over each child and
	# provide the dictionary from that part of the array.
	for i in get_child_count():
		get_child(i).import_from_dict(json[i])
```

## Saving data that exists solely in Godot

A middle ground between a fully human-readable format like JSON and a fully non-human-readable format in binary is to save the data as strings of data.

Godot provides the global functions `var2str` for saving. It will store the script location and variable data of even complex objects like Vector2 or String into a format that it's able to read back with `str2var`, recreating the object as you saved it. The order matters since variable names and positions are not parsed, but it takes out the problem of encoding string lengths or individual components of primitives like X and Y.

Here's the data this approach produces. The final file size is **77 bytes**. It's more than our binary's 42 bytes, but less than JSON's 160 bytes for an output that's easy to read and to edit.

```json
50
"Larry"
Vector2( 120.206, 119.449 )
25
"Harry"
Vector2( 211.11, 107.883 )
```

Here's the code to produce and load this output. We store one value per line.

```gdscript
## Export the class' relevant data as Godot-recognized data lines of strings
## Each piece of data is saved in order as a line using `var2str` so Godot
## can load it later.
func save_to_var(file: File) -> void:
	file.store_line(var2str(age))
	file.store_line(var2str(character_name))
	file.store_line(var2str(position))


## Import the class' relevant data from data lines of strings.
## Each piece of data is loaded in as a line, then run through the `str2var` to
## turn it back into data. Must load in the same order it was saved in.
func load_from_var(file: File) -> void:
	age = str2var(file.get_line())
	character_name = str2var(file.get_line())
	position = str2var(file.get_line())
```

Notice how we can directly save a Vector2 with `var2str()`. You can convert any built-in type to text with this function.

Loading is also the simplest with this approach, as shown by the code below. If your data isn't meant to be imported in other programs, `var2str()` and `str2var()` are your most efficient tools to save and load information.

```gdscript
const SAVE_VAR := "user://sav1.sav"

## The save class' method to prompt its children to save their data to a file.
func save_var() -> void:
	# Instances a new `File` in write mode and iterate over each child to use it
	# to save.
	var file := File.new()
	file.open(SAVE_VAR, File.WRITE)

	for child in get_children():
		child.save_to_var(file)

	# Clean up
	file.close()


func load_var() -> void:
	# Instances a new `File` in read mode and attempt to load the file, if it is
	# open-able and readable.
	var file := File.new()
	var error := file.open(SAVE_VAR, File.READ)

	if not error == OK:
		print_error("Could not load file at %s" % SAVE_VAR)
		return

	# Send the loaded file to each child in the same order they were saved to
	# have them load their data.
	for child in get_children():
		child.load_from_var(file)

	# Clean up
	file.close()
```

## Large, complex save files with relationships

Games with massive amounts of interconnected content, like MMOs or RTS,' do not scale well with a single text or binary file.

At that point, you should be looking into using a complete database system that can keep track of both data and relationships between data.

This topic is beyond this guide's scope, but if you're in this situation, you can look into SQL databases. They're commonly used in large-scale video games.

