+++
title = "{{ replace .Dir "-" " " | path.Base | title }}"
date = {{ .Date }}
author = "nathan"

description = "Short description"

draft = true

category = "news"

[[resources]]
  name = "banner"
  src = "banner.svg"
+++
