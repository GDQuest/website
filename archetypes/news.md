+++
title = "{{ if eq .File.TranslationBaseName "index" }}{{ replace (.File.Dir | path.Base) "-" " " | title }}{{ else }}{{ replace .File.TranslationBaseName "-" " " | title }}{{ end }}"
description = "Temp description"
author = "nathan"

date = {{ .Date }}
weight = 5
draft = true

categories = ["news"]
tags = ["gdquest"]
+++
