---
aliases:
- /post/2016/programming/hugo-tips-concat-node-paths-variable/
author: nathan
category:
- Webdesign
date: "2016-04-20T09:34:58+02:00"
description: Have you ever wondered how to access a file from your database based
  on a variable in your front matter in Hugo? This tutorial will show you how to achieve
  that using the index function.
highlight: templates
keywords:
- hugo
- gohugo
- static html engine
- create a website
title: 'Hugo Tips: Concatenate paths with variables'
type: post
---

<span class="text-muted"> This tutorial is a post I initially wrote on the [Hugo](//gohugo.io/) forums. Hugo is the static website generator that powers GDQuest.
It is a really flexible and elegant system, based on Google's Go programming language. Sometimes, it is a bit hard to use for a non-tech-savvy user. So I decided to share some tips on things that got me stuck at some point. </span>

In a template, you sometimes need to load data from a path based on a parameter in your content file’s front matter. For example, you may want to add an author to every post that tells the visitor a bit more about the writer. You want to tell Hugo who the author is, and let the template load all of that person’s info from the data folder.

The first step is simple. We just have to properly set the author variable in the post’s front matter. We will use it to access the right file in our database:

~~~
+++
author = "nathan"
+++
~~~

Based on this variable, in your template/partial, you want to access a specific data file stored in the **data/authors/** folder of your website, named exactly the same as your author variable in your content piece. In my case, this file is **data/authors/admin.toml**.

The content of this file can be accessed from your template using the following node path: **.Site.Data.authors.admin**
The problem is, we don’t always want to have the page’s author set to Admin. If a guest writes a post for my website, I want to use his name instead. For every content piece, the author’s name is available at **.Params.author** in your template, as we added this variable to our content's front matter. So you want to load the data from the file at **.Site.Data.authors** called the same as the variable **.Params.author**.

To do that, in go template, we have to use the index function. Index takes 2 parameters: the first one is a node path, and the 2nd one is a string corresponding to the data we want to access. For example:

~~~
{{ index .Site.Data.authors “admin” }}
~~~

Will return the content of .Site.Data.authors.admin. Now, as the variable .Params.author is a string, we can use it with the index function. So this:

~~~
{{ index .Site.Data.authors .Params.author }}
~~~

Will return the content of the data file at data/authors/our_post_author.

You can put your index operation in parentheses and keep going down the node tree by adding a “.” right after it:

~~~
{{ (index .Site.Data “authors”).admin}}
~~~

Last but not least, by nesting parentheses, you can compound multiple index operations together and access more complex paths that way:

~~~
{{ index (index .Site.Data "authors") "admin" }}
~~~

You can see the resulting author banner at the bottom of this post!

I hope this helps! As a non-web developer, I find it hard sometimes to wrap my head around the way go template work. It's really simple once you know how to do it, but it can take a while before you find how to use a function the right way, even with the help of the documentation.

_Happy Hugo coding!_
