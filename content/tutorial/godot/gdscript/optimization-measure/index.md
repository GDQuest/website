+++
title = "Measuring the speed of your code"
description = "Using the profiler and measuring individual blocks of code with timers"
menuTitle = "Optimization 1 - Measure your code"
author = "razoric"

date = 2020-08-19T14:00:45-04:00
weight = 4
draft = true

difficulty = "beginner"
keywords = ["gdscript optimization tutorial", "godot code optimizing", "godot optimization"]
+++

![The profiler](images/profiler.png)

You run your game from Godot and play around. It's fun, it's becoming feature complete, and you feel it's getting close to release. 

But then, you open the skill tree, and it grinds to a halt as something snags in your code. Watching the skill tree scroll by like it's a slide show is unacceptable. What went wrong? Is it the calculation of positioning the skill tree elements? Is it the UI? Is it looking at what is already unlocked? Is it the rendering?

You could try to optimize everything and run the game again and again until you find the culprit, but you can be smarter about this and narrow down the possibilities. Enter Godot's profiler.

## An overview of the profiler

### Starting profiling your code

Along the top is the toolbar, starting with the Start and Stop buttons. Godot's profiler does not run automatically because profiling is expensive. It has to constantly measure everything happening in the game and report back to the debugger, so it's off by default. To begin profiling, you press the Start button and it's ready to profile. Run your game and data will start filtering in. You can also start profiling at any time before or during gameplay, depending on if you want to profile loading times and initialization or a slice of your game.

You can clear the data and change what kind of data you want to see. The measurements panel and the graph will update accordingly. We start with the obvious feature: the measurements.

### The measurements

The two main elements are the graph of the functions running in your game on the right and the table of functions on the left.

The main measurements are frame time, physics time, idle time and physics time.

-   The frame time is the time it takes Godot to run through a single iteration of the engine. That includes _all_ other Godot facilities, from physics to rendering.
-   Physics frame is the time Godot has allocated between physics update. In an ideal scenario, the frame time is whatever you set it has: 60 FPS by default, which is 16.66 milliseconds. It's a frame of reference you can use for everything else around it.
-   Idle time is the time Godot took to update non-physics tasks, such as code that lives in `_process` or timers and cameras set to update on Idle.
-   Physics time is the time Godot took to update physics tasks, like `_physics_process` and built-in nodes set to Physics update.

<p class="note">
I'd like to emphasize that in Godot 3, Frame Time includes rendering time. If you find a mysterious spike of lag in your game but your physics and scripts are all running fast, it could be the sudden appearance of particles or visual effects!
</p>

By default, Godot ticks on Frame Time and Physics Time. This gives you an overview of how long each frame takes in relation to the allocated desired physics FPS, but you can toggle functions on and off with the checkboxes on the left. Other facilities make appearances as you go down the list, like Physics 2D, Physics and Audio, before reaching Script functions. This is where your code appears.

If you click on the graph, you change which frame's information appears on the left. In the top right, there is also a frame counter where you can manually adjust the frame you are looking at more granularly.

### Scope of measurement and measurement windows

You can change what measurement you are looking at using the _Measure_ drop down menu. By default, it starts with Frame Time and lists the time it takes to go through the frame in milliseconds. Average time is the average time any given function took when called more than once (ideally, something that took 0.05 milliseconds ran 5 times at an average of 0.01 milliseconds, for example).

If accurate milliseconds count are not so important and you want to see proportions of time relative to the rest of the frame, you have percentage measurements. Frame % is relative to Frame Time and Physics % is relative to Physics Time.

The last option is the scope of the Time. _Inclusive_ measures the time a function took _with_ any nested function calls. For example:

![Measuring inclusive](images/split_curve.png)

`get_neighbors`, `find_nearest_neighbor` and `move_subject` all took a lot of time. You could be fooled into thinking that this is because all three of them are slow.

But when changed to _Self_, Godot measures the time spent in the function body itself without considering function calls it made itself.

![Measuring self](images/self_curve.png)

You can see that `get_neighbors` and `move_subject` have lost a lot of their importance. In effect, that means that `get_neighbors` and `move_subject` have spent more time waiting for some other function call to finish than not, and `find_nearest_neighbor` is _actually_ slow.

### Debugging slow code with the profiler

The process of finding slow code with the profiler is to run your game and look at the graph as it streams by. When an unacceptable spike occurs in the frame time, you can click on the graph to pause your game and narrow the _Frame #_ to the start of the spike. You may need to search back and forth until you find the root cause.

Then, under the Script functions, you can turn on the checkboxes for some of the functions to find one that takes the most amount of time. That function is ideal for optimization (or replacement, if the problem is _really_ bad.)

## Measuring manually in microseconds

If your function is complex, it could be difficult to figure out which part actually needs optimization. Is it your math or the way you access other pieces of data to do the math with? Is it the `for` loop? The `if` statements?

You can narrow down the measurement by manually counting ticks as the code runs with some temporary functions. The two functions are part of the `OS` class object. They are `get_ticks_msec` and `get_ticks_usec`. The first one measures in milliseconds (1,000 per second) and the second measures in microseconds (1,000,000 per second).

Either one returns the amount of time since the game started in their respective time frame. This comes directly from the operating system rather than Godot itself.

If you wrap a piece of code with a start and end count of microseconds, the difference between the two is the amount of time it took to run that piece of code.

```gdscript
var start = OS.get_ticks_usec()

worker_function()

var end = OS.get_ticks_usec()

var worker_time = (end-start)/1000000.0


start = OS.get_ticks_usec()

for calc in calculations:
    result = pow(2, calc.power) * calc.product

end = OS.get_ticks_usec()

var loop_time = (end-start)/1000000.0


print("Worker time: %s\nLoop time: %s" % [worker_time, loop_time])
```

As you become a more experienced programmer, this technique becomes less necessary. You begin to learn what parts of a running program is slow. Knowing that loops and branches can be slow comes from experience, and you gain experience by measuring and researching.

But between the profiler and the ticks functions, you have enough to get started finding which parts of your code need optimizing.
