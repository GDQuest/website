del /q public\* && for /d %%x in (public\*) do @rd /s /q "%%x"
hugo
gulp htmlmin
