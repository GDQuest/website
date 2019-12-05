---
title: {{ replace .Dir "-" " " | path.Base | title }}
date: {{ .Date }}
author: nathan

description: Short description

productUrl: https://gdquest.mavenseed.com/

resources:
- src: banner.svg
  name: banner
---
