+++
title = "{{ if eq .File.TranslationBaseName "index" }}{{ replace (.File.Dir | path.Base) "-" " " | title }}{{ else }}{{ replace .File.TranslationBaseName "-" " " | title }}{{ end }}"
description = ""
author = "nathan"

date = {{ .Date }}
weight = 5
draft = true

difficulty = "beginner"
keywords = ["tutorial"]
+++
