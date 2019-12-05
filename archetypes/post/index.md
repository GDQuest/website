---
title: {{ replace .Dir "-" " " | path.Base | title }}
date: {{ .Date }}
author: nathan

description: Short description

draft: true

category: news
tags:
    - gdquest

banner:
    src: banner.svg
    alt: banner
---
