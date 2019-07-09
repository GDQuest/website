---
title: "Blender Python: best practices"
description: This is a living guide to help you write great Python code for Blender. The goal is to get code that's easy to read, to review, and to maintain, without compromising on performances.
author: nathan

date: 2019-07-08T07:48:23+09:00
---

This is a living guide to help you write solid Python code for Blender. The goal is produce code that's easy to read, to review, and to maintain, without compromising on performances.

{{< note >}}
This guide is a work-in-progress, [feedback is welcome](https://github.com/GDquest/GDquest-website/issues/81)! 🙂
{{< / note >}}

## Code conventions for blender python ##

To work together on Free Software efficiently, we need to follow some conventions. This helps to make the code easy to read and to explore for everyone. This makes it easy for new contributors or fellow developers to fix bugs in your code.

Here's a complete class that follows all the conventions below, with some code removed so it's not too long to read:

{{< highlight python >}}
class POWER_SEQUENCER_OT_gap_remove(bpy.types.Operator):
    """
    Remove gaps, starting from the time cursor, ignoring locked strips
    """
    bl_idname = 'power_sequencer.gap_remove'
    bl_label = 'Remove Gaps'
    bl_description = 'Removes gaps, starting from the time cursor, ignoring locked strips'
    bl_options = {'REGISTER', 'UNDO'}

    ignore_locked: bpy.props.BoolProperty(
        name="Ignore Locked Strips",
        description="Remove gaps without moving locked strips",
        default=True)
    all: bpy.props.BoolProperty(
        name="Remove All",
        description="Remove all gaps starting from the time cursor",
        default=False)
    frame: bpy.props.IntProperty(
        name="Frame",
        description="Frame to remove gaps from, defaults at the time cursor",
        default=-1)

    @classmethod
    def poll(cls, context):
        return (context.sequences and len(context.sequences) > 0)

    def execute(self, context):
        frame = self.frame if self.frame >= 0 else context.scene.frame_current

        sequences = context.sequences
        if self.ignore_locked:
        sequences = [s for s in context.sequences if not s.lock]
        sequences = [s for s in sequences
                     if s.frame_final_start >= frame
                     or s.frame_final_end > frame]

        sequence_blocks = slice_selection(context, sequences)
        if not sequence_blocks:
            return {'FINISHED'}

        gap_frame = self.find_gap_frame(context, frame, sequence_blocks[0])
        if gap_frame == -1:
            return {'FINISHED'}

        first_block_start = min(sequence_blocks[0], key=attrgetter('frame_final_start')).frame_final_start
        blocks_after_gap = (sequence_blocks[1:]
                            if first_block_start <= gap_frame else
                            sequence_blocks)
        self.gaps_remove(context, blocks_after_gap, gap_frame)
        return {'FINISHED'}

    def find_gap_frame(self, context, frame, sorted_sequences):
        """
        Takes a list sequences sorted by frame_final_start
        """
        ...
        return gap_frame

    def gaps_remove(self, context, sequence_blocks, gap_frame_start):
        """
        Recursively removes gaps between blocks of sequences
        """
        ...

    def move_markers(self, context, gap_frame, gap_size):
        ...
{{< / highlight >}}


Name classes as `CATEGORY_TYPE_name`:

1. `CATEGORY` is what the class works with or operates on. It can be `OBJECT`, `ACTION` for animation actions, `ARMATURE` if it affects an armature, `SEQUENCER`, etc.
1. `TYPE` is a two letters acronym that represents the nature of the class. You will use `OT` for operators, `MT` for menu templates, PT for panel templates, UL for UI lists, etc.
1. `name` is the name for your operator or UI element in `camel_case`. Find a clear name that represents the action the class will perform or the UI element that it represents.

This naming scheme makes it easy to find features in the codebase. You can search for `CATEGORY*operator_name` using tags or a search tool to find the source code of any operator listed in the program's keymaps.

In my code editor, searching code tags for `SEQ _OT`, I instantly get the list of all of the sequencer's operators:

![spacemacs-gtags-search-operators](./spacemacs-gtags-search-operators.png)

Some class name examples from Blender's source code:

```
OBJECT_OT_duplicate_move, duplicates and moves selected objects, when you press Shift D in the 3D view
ACTION_OT_select_all, selects all 
VIEW3D_MT_mesh_add, the Add -> Mesh menu in the 3D view
```

## Naming conventions and tips ##

### Tips to make your own code easier to read ###

The convention inside Blender is to use words common to several properties or methods as a prefix of the property or the function's name. For instance, the property names of sequences in the VSE  related to climb on duration in frames all start with frame: `frame_start`, `frame_end`, and `frame_duration` rather than `start_frame`, `end_frame`, and `duration_frame`.

Even though the last three names are a bit more natural to read in English, when you are programming, it will be much easier to find all the *frame* related properties thanks to your code editor's autocomplete feature.
