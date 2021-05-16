+++
title = "The checklist"
description = ""
author = "sally"

date = 2021-05-16
weight = 5
+++

- Use this checklist as a guide to make sure you're not forgetting anything at every stage of your project. 
- It is best referred as you work along rather than at the very end. 
- Depending on the editor you use, you can download an extension like [ToDo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) to display the checklist in the sidebar.

## 1. Did you scope your project and get a prototype review?
- [ ] Did you single out and set out to solve one real problem that users in your target audience have?
- [ ] If you’re writing for advanced users: 
    - [ ] Did you discuss the topic thoroughly with users in the target audience to make sure you understand the problem?
    - [ ] Did you only touch on topics you’re very comfortable with?
    - [ ] Did you get in touch with experts/core developers for insight on how a specific part of the engine works?
- [ ] Did you write the header of your tutorial?
    - [ ] Did you make a bullet list with key information (title, pitch, audience, and teaching points)?
    - [ ] Did you write the tutorial title? 
    - [ ] Did you list the things the user will learn?
    - [ ] Did you list the prerequisites?
    - [ ] Did you write a short introduction?
- [ ] Did you create a prototype for your code demo using geometric shapes?
- [ ] Did you create a pull request to submit it for review? 
    - [ ] Did you add the header of your outline in a PR comment before you submit your prototype? 
- [ ] Did you get confirmation from peers and members of your target audience on the direction and scope of your tutorial and demo?
- [ ] If your code will take more than 2 days of work, did you agree on review milestones?


## 2. Did you finalize your code demo and get a final review?
- [ ] Did you define the limits of your code instructions?
    - [ ] Did you encapsulate all irrelevant but required assets, scenes and scripts?
    - [ ] Did you create an API to contain all relevant scripts: properties, methods’ signature, docstrings?
- [ ] Did you keep your code as simple and readable as possible?
    - [ ] Did you avoid making your code flexible and future-proof?
    - [ ] Did you pick one valid solution?
    - [ ] Did you favor inline code in functions over splitting code across many functions?
    - [ ] Did you avoid popular principles that don’t create a concrete benefit?
    - [ ] Do you know why you chose every line of code over an alternative?1
- [ ] Did you follow the GDScript code order?
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
    11. optional built-in virtual _init method
    12. built-in virtual _ready method
    13. remaining built-in virtual methods
    14. public methods
    15. private methods

- [ ] Did you follow the right code style and syntax rules?
    - [ ] Do your docstrings start with `##`?
    - [ ] Did you use the past tense for signals?
    - [ ] Did you omit parentheses if the signal does not pass function parameters?
    - [ ] Did you append `_started` or `_finished` if the signal corresponds to the beginning or end of an action?
    - [ ] Did you use plain verbs instead of repeating the class name in signals?
    - [ ] Did you use verbs for function names?
    - [ ] Did you use nouns for variable names?
    - [ ] Did you use `PascalCase` for enum type names and `ALL_CAPS_SNAKE_CASE` for the values?
    - [ ] Did you include `is_` , `can_` or `has_` for booleans?
    - [ ] Did you use `snake_case` for public variable names?
    - [ ] Did you use `_snake_case_with_leading_underscore` for pseudo-private member variables?
    - [ ] Did you define setters and getters every time properties altered the object’s state and whenever you changed the property trigger methods?
    - [ ] Did you include a docstring in the setters/getters if they modify the node/class state in a complex way?
    - [ ] Did you start with a leading underscore when the setters and getters are for a private variable?
    - [ ] Did you place onready variables right before `_init` and/or `_ready` functions?
    - [ ] Did you leave 2 blank lines between methods?
    - [ ] Did you use `_on_NodeName_signal_name` for signal callbacks? 
    - [ ] Did you remove `NodeName` if the object connects to itself?
    - [ ] Did you include type hints and the return type for variables?
    - [ ] Did you use a brief comment to describe what a public function does and what it returns?
    - [ ] Did you start the sentence with `Returns` ?
    - [ ] Did you use the present tense and the active voice?
    - [ ] Did use use `return` only at the beginning?
    - [ ] Did you avoid `return` in the middle of the method?
    - [ ] Did you use static type hints?
    - [ ] Did you add a colon `:` after the variable name to let Godot infer type whenever possible?
    - [ ] Did you try to avoid `null` references?
    - [ ] Did you use clear variable names unabbreviated and in plain English?
    - [ ] Did you avoid repeating the same word in method names and arguments?
    - [ ] Did you use short variable names for local variables inside your method?

- [ ] Did you review your code for readability?
- [ ] Did you make sure your code is self-explanatory?
- [ ] Did you use comments whenever there is obscure code, calculations or a strange bug workaround? 
- [ ] Did you run [GDScript code formatter](https://github.com/Scony/godot-gdscript-toolkit) before pushing your code for review?

- [ ] Did you name and organize files and directories according to our guidelines?
    - [ ] Did you use `PascalCase` to name directories, scenes, and script files?
    - [ ] Did you make sure not to leave spaces in file names?
    - [ ] Did you name scripts and scenes after their root node?
    - [ ] Did you group assets, scripts and scenes together whenever possible?
    - [ ] Did you place files we may reuse across projects in Godot’s addons directory (besides editor plug-ins). 

- [ ] If your code takes more than 2 days of work, did you submit it for review at every milestone?
- [ ] Did you submit your completed code demo for final code review?
- [ ] Did you remember to include the tutorial header in a comment with each pull request?


## 3. Did you outline your tutorial?
- [ ] Did you revise your tutorial header after the scope and code reviews? 
- [ ] Did you create logical sections for each main teaching point? 
- [ ] Did you write a descriptive heading and sub-headings for each section?
    - [ ] Did you avoid using new class names and technical titles?
    - [ ] Did you avoid one or two word headings?
    - [ ] Did you capture the problem you will be solving or the game mechanic you will be adding?
- [ ] Did you fill each section heading with short notes and code snippets?
- [ ] Did you focus on key teaching points and the order in which you’ll teach them?
- [ ] Did you write down questions the reader might have?
- [ ] Did you work with a peer to ensure you’re not forgetting anything?


## 4. Did you craft your tutorial?

### 4.1 Did you craft the Tutorial Body?
- [ ] Did you review and keep in mind the writing style guidelines before you got started writing? (refer to checklist 5).
- [ ] Did you put yourself in the reader’s shoes?
    - [ ] Did you start from the users’ problem?
    - [ ] Did you think of yourself when you were trying to learn the concepts you’re teaching?
    - [ ] Did you explain why you chose to structure your project this way?
    - [ ] Did you mention other potential solutions, their advantages and drawbacks?
    - [ ] If you’re teaching a pattern, did you explain its general form?
    - [ ] Did you indicate the limits of your example or tutorial compared to a real-world scenario?
    - [ ] If you’re writing for beginners: 
        - [ ] Did you include spatial indications (where to find buttons, etc…)
        - [ ] Did you use many pictures to help visualize the steps?
        - [ ] Did you anticipate and answer questions?
        - [ ] Did you troubleshoot common mistakes and errors?
- [ ] Did you focus on one thing at a time? 
- [ ] Did you structure your content to make it as easy as possible to follow?
    - [ ] Did you order your sections to provide the reader with the most accessible learning flow?
    - [ ] Did you verify your sections are logical and follow the outline you gave in the introduction?
- [ ] Did you share your thought process with the reader?
    - [ ] Did you explain “why” more than just “how”?
    - [ ] Did you tell the reader why you picked this approach over another?
- [ ] Did you detail inside each section the steps to achieve the result?
    - [ ] Did you verify section headings aren’t labels and actually explain the problem you’re going to solve?
- [ ] Did you support your teaching with visuals?
    - [ ] Do the pictures illustrate or show the result of an action?
    - [ ] Are the images as close as possible to the relevant text?
    - [ ] Did you label and refer to visuals in an unambiguous way?
- [ ] Did you craft your code references?
    - [ ] Did you favor appending code at the end of existing functions rather than in the middle?
    - [ ] Did you highlight the change if you had to append or substitute code in the middle of a function?
    - [ ] Did you include code comments?
    - [ ] Did you explain why you decided to write a function in your chosen way?
    - [ ] Did you explain what the code does without paraphrasing it?
    - [ ] Did you explain how the implementation affects performance?
    - [ ] Did you explain how a function works under the hood or what else it does?
    - [ ] Did you explain what edge cases you’re accounting for?
    - [ ] If you’re writing for beginners:
        - [ ] Did you keep your code listings short?
        - [ ] Did you write detailed code comments?
- [ ] Did you craft the flow?
    - [ ] Did you avoid frequent back-and-forth between files?
    - [ ] Did you avoid a robotic structure?
    - [ ] Did you use a natural flow by adding game mechanics and features one after the other?
    - [ ] Did you make sure the reader is able to run their game or edited scene at the ed of each section without errors? 

### 4.2 Did you write a footer?
- [ ] Did you provide the reader with a recap of what they achieved and learned?
- [ ] Did you give the reader insights on how they can go further and what other lessons they can check out next?

### 4.3 Did you remember to go back and craft all the elements of the Header?
- [ ] Did you use a descriptive title that includes search words for the problem you’re solving?
- [ ] Did you explain the problem or topic in one or two introductory sentences?
- [ ] Did you show the result in a screenshot or video clip?
- [ ] Did you list the things the reader will learn in logical order?
- [ ] Did you list the prerequisites and link to existing series keeping the user’s level or tutorials in mind?
- [ ] Did you explain in a sentence or short paragraph how and why you will tackle the problem?

## 5. Did you watch your writing style? 
- [ ] Was your tone kind, genuine, clear, accessible, inclusive and professional?
- [ ] Did you avoid exaggerations, unnecessary jargon and colloquial expressions?
- [ ] Did you aim for a welcoming feel without being too close?
- [ ] Did you use gender neutral pronouns? Did you address the reader as “you”, yourself as “I”, the team as “we” and any third parties as “they”?
- [ ] Did you void statements about the presumed desires, capabilities or actions of some demographic group?
- [ ] Did you use American English?
- [ ] Did you write with your least experienced reader in mind? 
- [ ] Did you remember to repeat keywords?
- [ ] Did you break down complex or abstract ideas?
- [ ] Did you use plain language and avoid uncommon or overly academic words?
- [ ] Were you as clear and precise as possible?
- [ ] Did you use the direct voice?
- [ ] Did you keep your sentences short and limited to one idea each? (Under 25 words)
- [ ] Did you use paragraphs to group sentences related to a broader idea?
- [ ] Did you break up paragraphs and use subheadings and lists to structure your writing?
- [ ] Did you avoid ambiguous pronouns like “this” and “that” or specify what the noun they refer to?
- [ ] Did you use italics to mention labels like node names, dock names, or property names?
- [ ] Did you write labels as they appear in the interface? 
- [ ] Did you use inline code when for symbols (variable names, function names), values and any code in a sentence? 
- [ ] Did you use inline code for absolute and relative paths?
- [ ] Did you use parenthesis in function names to differentiate them from variables?
- [ ] Did you spell out numbers in words outside of the code?
- [ ] Did you use plain English over symbols like & or /?
- [ ] Did you use Title Case for the document title and only capitalize the first letter for other headings?
- [ ] Did you create meaningful links that describe what the user will accomplish if they click?
    - [ ] Did you explain where the link leads and why?
    - [ ] Does the link help the user scan the page for essential information and related resources?


## 6. Did you review your work and use editing tools before submitting it for review? 
- [ ] Did you edit your text yourself first for clarity?
- [ ] Did you follow all the steps of your instructions and made sure they lead to the expected results?
- [ ] Did you seek critical feedback?
- [ ] Did you use a markdown formatter?
- [ ] Did you use a prose linter like write-good to highlight complicated terms and structures?
- [ ] Did you use a spellchecker?
- [ ] Did you run your text through an online tool like the [Hemingway app](https://hemingwayapp.com/) or [Grammarly](https://www.grammarly.com/) for sentence length and style?

## 7. Did you submit your work for final review?
- [ ] Did and editor edit and comment your tutorial?
- [ ] Did a tester test your demo?
- [ ] Did you incorporate the recommendations and re-submit for a final edit?


