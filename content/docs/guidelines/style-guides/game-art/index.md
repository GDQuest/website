+++
title = "Game art style guide"
menuTitle = "Art style guide"
description = "This document describes an accessible art style to create game art efficiently. This is the style we use in our Godot tutorials."
author = "henrique"
date = "2020-02-06"
weight = 5
+++

This document describes an accessible art style to create game art efficiently. This is the style we use in our [Godot tutorials](https://youtu.be/Mc13Z2gboEk). It uses a flat design to make the sprites read well.

![Landscape Platformer](samples/landscape-platformer.svg)

We designed this visual language to be:

- **Clear**. The game should always read well.
- **Colorful and appealing**. We want it to be warm and attractive to the eye.
- **Accessible** even to inexperienced digital artists. It relies on simple shapes and vector graphics.

## Colors ##

We use the [Pear36 color palette](https://lospec.com/palette-list/pear36) for all of our sprites. With 36 colors, it has enough hues to distinguish props in the game without becoming too hard to pick the right color.

Here are some tips on picking striking colors.

### Value contrast ###

Use value contrast to make gameplay assets more visible than the background:

- Use bright tones for the characters, enemies, loot, and interactive objects.
- Use darker tones for trees, the grass, houses, and everything that's part of the background.

You should also use outlines to highlight foreground sprites.

### Picking good hues ###

You can use the natural hue of an element whenever possible such as orange and red for lava, or brown for a tree's trunk.

However, there are many cases where colors are symbolic. An example of this is using green to represent the health of a character. In these cases, look for references and use standard conventions:

- Red is a great tone to convey danger. It can also represent love or life as in a red heart.
- Green can represent health, healing, bonuses, or endurance.
- Yellow stands out and works well for coins, but also indicators like an arrow that tells the player where to go, or a quest marker.

There are no hard rules. What matters is that the players understand the game from its graphics.

{{% notice note %}}
You may have seen infographics about [the meaning of colors](https://www.color-meanings.com/). Take them with a pinch of salt. The perception of colors varies between cultures and depends on the context. I've read multiple times that purple would be the color of royalty. But if you look at historical portraits or outfits of kings and queens, you'll find a lot of red, gold, beige, or black. These are the colors that come to my mind when thinking of "royalty."
{{% / notice %}}

### Complementary colors ###

Complementary colors are colors that, when mixed, cancel each other out and turn into gray. On the computer, in the RGB color model, these colors correspond to hues that are opposite on the color wheel.

{{< figure src="./img/complementary-colors.svg" alt="Star-shaped wheel representing complementary colors" title="Complementary color star used by the painters of the 19th century" caption="By Kwamikagami - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=43056011" >}}

These colors offer a striking visual contrast. You can use them to express relationships between game elements:

- Orange and blue portals can be two parts of the same system.
- Blue walls and floor can suggest a safe environment while the red lava reads as unsafe.
- A green player and a purple enemy indicate opposite characters.

### Use lighter outline colors ###

With a dark background, a bright outline offers maximum visual contrast. That's why we use a lighter outline color compared to a sprite's fill.

Not every element needs outlines. In the image at the top of this guide, the coins stand out thanks to their bright yellow fill.

## Shapes ##

Minimalism is the core of the shapes design. Simplicity is important and helps distinguish each individual element.

Reliable elements are usually represented by squares. Their behavior is predictable and consistent. You could use squares for the player, static platforms, floors, walls and even lava since its behavior is consistent.

Circles usually represent interactive elements such as coins, hearts, portals, or the top part of enemies since players can stomp them.

Triangles usually convey danger and avoidance. Use them for elements that cause damage on contact or to give direction. For example, an enemy could consist of a circle and a triangle, meaning its top part is safer than its sides.

You can mix these characteristics to convey better meaning with slightly more complex shapes.

Take the following image:

![Topdown shooter](samples/landscape-topdown-shooter.svg)

Here, the meteors are created from two differently sized circles to easily distinguish their rotation. The players are also notched triangles to communicate their look direction, bullets are capsules to convey movement.

## Type ##

We are currently using *Montserrat Bold* font for most of the text used in game. It's a good *sans serif* font with enough weight to be readable while still maintaining its place in the game screen's hierarchy.

![Some UI Elements](samples/ui-elements.svg)

While teaching, we often use debug elements that need to be readable yet distinguishable from in-game elements. This helps us properly explain technical information. For that we use a *monospace bold* font.
![More Debug Elements](samples/topdown-debug.svg)

Transparent debug elements allow us to show how our input affects the game instantly.

![In game Debug Console](samples/debug-console.svg)

## Conclusion ##

With this in mind, be as creative as necessary to express information without complexity. Focus on teaching good game development concepts with quality visuals.
![Feature Rich Topdown Game Demo](samples/landscape-topdown-adventure.svg)

In sum:

- Form follows function
- Each element should be distinct and unique
- Simplicity over complexity
- Abstraction through well established concepts

## Resources ##

- Pear36: https://lospec.com/palette-list/pear36
- Montserrat font family: https://fonts.google.com/specimen/Montserrat
- Monospace font: https://fonts.google.com/specimen/PT+Mono
- Flat design principles
  - https://designmodo.com/flat-design-principles/
  - https://simplicable.com/new/flat-design

## Samples ##

Here are some game mockups based on this art style.

{{< figure src="samples/landscape-topdown-shooter.svg" alt="Landscape Topdown Shooter" title="Landscape Topdown Shooter" >}}

{{< figure src="samples/landscape-topdown.svg" alt="Landscape Topdown Strategy" title="Landscape Topdown Strategy" >}}

{{< figure src="samples/main-screen.svg" alt="Main Screen" title="Main Screen" >}}

{{< figure src="samples/ui-elements.svg" alt="Options Menu" title="Options Menu" >}}

{{< figure src="samples/portrait-topdown-shooter.svg" alt="Mobile Topdown Shooter" title="Mobile Topdown Shooter" >}}

{{< figure src="samples/portrait-platformer.svg" alt="Mobile Platformer" title="Mobile Platformer" >}}

{{< figure src="samples/portrait-topdown-adventure.svg" alt="Mobile Topdown Adventure" title="Mobile Topdown Adventure" >}}

{{< figure src="samples/debug-console.svg" alt="Debug Console" title="Debug Console" >}}

{{< figure src="samples/topdown-debug.svg" alt="Topdown Debug Mode" title="Topdown Debug Mode" >}}

## Elements ##

Here are individual svg files you can use as a base to create game art in this art style.

| Name  | Graphic   |
|------	|:---------:	|
|Topdown Player	|![](elements/topdown-player.svg)|
|Topdown Player Selected|![](elements/topdown-player-selected.svg)|
|Topdown Enemy|![](elements/topdown-enemy.svg)|
|Topdown Enemy Selected|![](elements/topdown-enemy-selected.svg)|
|Topdown Neutral|![](elements/topdown-neutral.svg)|
|Sidescroll Player|![](elements/side-scroll-player.svg)|
|Sidescroll Enemy|![](elements/side-scroll-enemy.svg)|
|Sidescroll Portal Orange|![](elements/side-scroll-portal-orange.svg)|
|Sidescroll Portal Blue|![](elements/side-scroll-portal-blue.svg)|
|Topdown Portal Orange|![](elements/topdown-portal-orange.svg)|
|Topdown Portal Blue|![](elements/topdown-portal-blue.svg)|
|Chest|![](elements/chest.svg)|
|Coin|![](elements/coin.svg)|
|Heart|![](elements/heart.svg)|
|Sign|![](elements/sign.svg)|
|Spike|![](elements/spike.svg)|
|Projectile Enemy|![](elements/projectile-enemy.svg)|
|Projectile Player|![](elements/projectile-player.svg)|
