---
author: nathan
date: "2021-05-16T00:00:00-06:00"
description: ""
title: The checklist
weight: 5
---

- Use this checklist as a guide to make sure you're not forgetting anything at every stage of your project.
- It is best referred to as you work along rather than at the very end.
- Depending on the editor you use, you can download an extension like [ToDo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) to display the checklist in the sidebar.

## 1. Scoping the project and getting a prototype review

- [ ] I singled out one real problem users have
- [ ] In case I'm writing for advanced users:
  - [ ] I discussed the topic with users in the target audience
  - [ ] I only touched on topics I'm very comfortable with
  - [ ] I got in touch with experts/core developers
- [ ] I wrote the tutorial header:
  - [ ] I made a bullet list with key information (title, pitch, audience, and teaching points)
  - [ ] I wrote the tutorial title
  - [ ] I listed the things the user will learn
  - [ ] I listed the prerequisites
  - [ ] I wrote a short introduction
- [ ] I created a prototype for the code demo using geometric shapes
- [ ] I created a pull request to submit it for review
  - [ ] I included the tutorial header in a PR comment
- [ ] I got confirmation from peers and members of my target audience on the scope of the tutorial and demo
- [ ] I agreed on review milestones if the code will take more than 2 days of work

## 2. Finalizing the code demo and getting a final review

- [ ] I defined the limits of my code instructions
  - [ ] I grouped all irrelevant but required assets, scenes, and scripts
  - [ ] I created an API to contain all relevant scripts: properties, methods' signatures, docstrings
- [ ] I kept my code as simple and readable as possible
  - [ ] I did not future-proof
  - [ ] I picked one valid solution
  - [ ] I favored inline code in functions (over splitting code across many functions)
  - [ ] I avoided popular principles that don't create a concrete benefit
  - [ ] I know why I chose every line of code over an alternative
- [ ] I followed the GDScript code order
  1. class docstrings
  2. class_name
  3. extends
  4. signals
  5. enums
  6. constants
  7. exported variables
  8. public variables
  9. private variables
  10. onready variables
  11. optional built-in virtual \_init method
  12. built-in virtual \_ready method
  13. remaining built-in virtual methods
  14. public methods
  15. private methods

- [ ] I followed the code style guidelines and syntax rules

  - [ ] Docstrings start with `##`
  - [ ] Signals are plain verbs in past tense and do not repeat class names
  - [ ] Signals take no parentheses if they do not pass function parameters
  - [ ] Signals corresponding to the beginning or end of an action are called `<action>_started` or `<action>_finished`
  - [ ] Function names are verbs
  - [ ] Variable names are nouns
  - [ ] Enum type names are in `PascalCase` and values are `ALL_CAPS_SNAKE_CASE`
  - [ ] Booleans start with `is_` , `can_` or `has_`
  - [ ] Public variable names are in `snake_case`
  - [ ] Pseudo-private variables names are in `_snake_case_with_leading_underscore`
  - [ ] Setters and getters are defined every time properties alter the object’s state
  - [ ] Docstrings are added for setters and getters if they modify the node/class state in a complex way
  - [ ] Setters and getters for a private variable start with a leading underscore
  - [ ] Onready variables are placed right before `_init` and/or `_ready` functions
  - [ ] Methods are separated by 2 blank lines
  - [ ] Signal callbacks use `_on_NodeName_signal_name`
  - [ ] `NodeName` is omitted when the object connects to itself
  - [ ] Variables have type hints and functions have the correct return type
  - [ ] Docstrings are added to public functions to describe what they do and what they return
  - [ ] Docstrings describing what a function returns start with `Returns`
  - [ ] Comments and docstrings use the present tense and active voice
  - [ ] Early `return` only occurs at the beginning of a function
  - [ ] Variable declarations use a colon `:` so Godot can infer type whenever possible
  - [ ] `null` references are avoided whenever possible
  - [ ] Variable names are simple and unabbreviated
  - [ ] Method names and arguments do not repeat the same word
  - [ ] Local variables inside a method can have short names

- [ ] I reviewed my code for readability and made sure it's self-explanatory
- [ ] I used comments whenever there is obscure code, calculations, or a strange bug workaround
- [ ] I ran [GDScript code formatter](https://github.com/Scony/godot-gdscript-toolkit) before pushing the code for review

- [ ] I named and organized files and directories according to our guidelines

  - [ ] I used `PascalCase` to name directories, scenes, and script files
  - [ ] I did not leave spaces in filenames
  - [ ] I named scripts and scenes after their root node
  - [ ] I grouped assets, scripts, and scenes together whenever possible
  - [ ] I placed files we may reuse across projects in Godot's addons directory (besides editor plug-ins)

- [ ] I submitted my code for final review and at every milestone if necessary
- [ ] I included the tutorial header in a comment in each pull request

## 3. Creating a tutorial outline

- [ ] I revised the tutorial header after the scope and code reviews
- [ ] I created logical sections for each main teaching point
- [ ] I wrote a descriptive heading and sub-headings for each section
  - [ ] I did not use new class names and technical titles
  - [ ] I did not use headings composed of one or two words
  - [ ] My headings capture the problem I'm trying to solve or the game mechanic I'm adding
- [ ] I filled each section heading with short notes and code snippets
- [ ] I focused on key teaching points and the order in which I'll teach them
- [ ] I wrote down questions the reader might have
- [ ] I worked with a peer to ensure I'm not forgetting anything

## 4. Writing the tutorial

### 4.1 Crafting the tutorial body

- [ ] I reread the writing style guidelines (in checklist 5) before getting started
- [ ] I put myself in the reader's shoes
  - [ ] I started from the users' problem
  - [ ] I remembered what it was like when I was trying to learn the concepts
  - [ ] I explained why I chose to structure my project this way
  - [ ] I mentioned other potential solutions, their advantages, and drawbacks
  - [ ] If I'm teaching a pattern, I explained its general form
  - [ ] I explained the limits of my example compared to a real-world scenario
  - [ ] If I'm writing for beginners:
    - [ ] I included spatial indications (where to find buttons, etc.)
    - [ ] I used many pictures to help visualize the steps
    - [ ] I anticipated and answered questions
    - [ ] I anticipated common mistakes and errors
- [ ] I focused on one thing at a time
- [ ] I structured the content to make it easy to follow
  - [ ] My sections are ordered logically to provide the reader with the most accessible learning flow
- [ ] I shared my thought process with the reader
  - [ ] I explained "why", not just "how"
  - [ ] I told the reader why I picked this approach over another
- [ ] Inside each section, I detailed the steps to achieve the results
  - [ ] I verified my section headings are descriptive of the problem, not labels
- [ ] I supported my teaching with visuals
  - [ ] I set up Godot's interface according to the guidelines (in checklist 7) before taking any screenshots
  - [ ] I only included relevant detail in image crops
  - [ ] The images are as close as possible to the relevant text
  - [ ] I labeled and referred to the visuals clearly
  - [ ] I kept inline videos and animated gifs to a minimum 
- [ ] I crafted my code references
  - [ ] I tried to append code at the end of existing functions rather than in the middle
  - [ ] I highlighted the change if I had to append or substitute code in the middle of a function
  - [ ] I included code comments:
    - [ ] I explained why I decided to write a function in a chosen way
    - [ ] I explained what the code does without paraphrasing it
    - [ ] I explained how the implementation affects performance
    - [ ] I explained how a function works under the hood or what else it does
    - [ ] I explained what edge cases I'm accounting for
  - [ ] If I'm writing for beginners:
    - [ ] I kept my code listings short
    - [ ] I wrote detailed code comments
- [ ] I crafted the flow of my tutorial
  - [ ] I avoided frequent back-and-forth between files
  - [ ] I did not use a robotic structure
  - [ ] I added game mechanics and features one after the other
  - [ ] I made sure the reader can run their game or edited scene at the end of each section without errors

### 4.2 Writing a footer

- [ ] I gave the reader a recap of what they achieved and learned
- [ ] I gave the reader insights on how they can go further and what other lessons they can check out next

### 4.3 Refining all the elements of the header

- [ ] I went back to check that the header still reflects the tutorial
  - [ ] The title includes search words for the problem I'm solving
  - [ ] The introductory sentences do explain the problem or topic
  - [ ] I showed the result in a screenshot or video clip
  - [ ] The list of learnings is complete and in a logical order
  - [ ] I did not forget any important prerequisites
  - [ ] I did follow the sentence or short paragraph in which I explained how I will tackle the problem

## 5. Reviewing the writing style

- [ ] My tone is kind, genuine, clear, accessible, inclusive, and professional
- [ ] I avoided exaggerations, unnecessary jargon, and colloquial expressions
- [ ] I achieved a welcoming feel without being too close
- [ ] I used gender-neutral pronouns
- [ ] I avoided generalizations about the presumed desires, capabilities, or actions of some demographic group
- [ ] I used American English
- [ ] I wrote with the least experienced reader in mind
- [ ] I repeated keywords
- [ ] I broke down complex or abstract ideas
- [ ] I used plain language and avoided uncommon or overly academic words
- [ ] I was as clear and precise as possible
- [ ] I used the direct voice
- [ ] I kept sentences short and limited to one idea each (Under 25 words)
- [ ] I used paragraphs to group sentences related to a broader idea
- [ ] I broke up paragraphs and used subheadings and lists
- [ ] I did not use ambiguous pronouns like "this" and "that" without specifying the noun they refer to
- [ ] I used italics to mention labels like node names, dock names, or property names
- [ ] I wrote labels as they appear in the interface
- [ ] I used inline code for symbols, variable names, function names, values, and any code in a sentence
- [ ] I used inline code for absolute and relative paths
- [ ] I used parentheses in function names to differentiate them from variables
- [ ] I spelled out numbers in words outside of the code
- [ ] I used plain English over symbols like & or /
- [ ] I used Title Case for the document title
- [ ] I capitalized only the first letter of other headings
- [ ] I created meaningful links that describe what the user will accomplish if they click

## 6. Reviewing my work and using editing tools

- [ ] I reread and edited my text for clarity
- [ ] I followed all the steps I gave and made sure they lead to the expected results
- [ ] I used a markdown formatter
- [ ] I used a prose linter like write-good to highlight complicated terms and sentence structures
- [ ] I used a spellchecker
- [ ] I used an online tool like the [Hemingway app](https://hemingwayapp.com/) or [Grammarly](https://www.grammarly.com/) for sentence length and style

## 7. Adding great pictures

- [ ] I set up Godot's interface following the guidelines

  - [ ] I'm using the default editor theme
  - [ ] My screen resolution is 1920×1080
  - [ ] My editor font size is 22 points
  - [ ] My code font size is 24 points

- [ ] I used many contextual pictures to illustrate the content
- [ ] I cropped pictures to only show what's necessary
- [ ] I trimmed pictures to avoid inconsistent borders
- [ ] I outlined key areas with a 4 pixels yellow stroke
- [ ] I used short inline video clips and animated GIFs sparingly
- [ ] I ran the scripts and commands to batch optimize all media files

## 8. Submitting the tutorial for review

- [ ] I submitted my tutorial to an editor
- [ ] A reviewer tested my demo
- [ ] I incorporated feedback and recommendations
- [ ] I re-submitted for a final check
