#!/usr/bin/env bash
#
# Creates content pieces for our hugo website.
NAME="create_content.sh"

# UTILS
FORMAT_NORMAL=$(tput sgr0)
FORMAT_BOLD=$(tput bold)

format_bold() {
	printf "%s%s%s" "$FORMAT_BOLD" "$*" "$FORMAT_NORMAL"
}

# Prints the text with inserted color codes for the current terminal.
# Resets to the normal format at the end of the text
#
# Arguments:
# $1 - a string representing the color, e.g. b or bold. See valid colors below.
# $* - The text to format.
color_apply() {
	case $1 in
	r | red) col=$COLOR_RED ;;
	*) col=$FORMAT_NORMAL ;;
	esac
	shift
	printf "%s%s%s" "$col" "$*" "$FORMAT_NORMAL"
}

# Outputs the string of text lowercase and with hyphens instead of spaces.
path_sanitize() {
	echo "$@" | tr "[:upper:]" "[:lower:]" | sed 's/ /-/g'
	exit $?
}

# Prints information about the program and how to use it.
echo_help() {
	test
	printf "Creates content pieces for our hugo website.

%s:
%s type name [category] [Options]

%s:

type		 -- Type of content, one of \`${TYPES[*]}\`
name		 -- File or directory name for the new content
category	 -- (Optional) Sub-directory name for tutorials, one of \`${CATEGORIES[*]}\`

%s:
-h/--help             -- Display this help message
-x/--dry-run          -- Display debug messages without modifying any file
-d/--date             -- (Optional) date override to create news posts
" "$(format_bold Usage)" "$NAME" "$(format_bold Positional arguments)" "$(format_bold Options)"
	exit 0
}

# Parses the arguments passed to the program.
parse_arguments() {
	args=()
	# Handle long options
	for arg; do
		case "$arg" in
		--help) args+=(-h) ;;
		--dry-run) args+=(-x) ;;
		--date) args+=(-d) ;;
		*) args+=("$arg") ;;
		esac
	done

	set -- "${args[@]}"
	while getopts "h,x,d:,n:" OPTION; do
		case $OPTION in
		h) echo_help ;;
		d)
			date=$(date -d "$OPTARG" -I)
			test $? -ne 0 && echo "Invalid date. Use a format supported by date, like $(date -I). Exiting" && exit 1
			;;
		x)
			is_dry_run=1
			;;
		--)
			break
			;;
		\?)
			echo "Invalid option: $OPTION" 1>&2
			;;
		:)
			echo "Invalid option: $OPTION requires an argument" 1>&2
			;;
		*)
			echo "There was an error: option '$OPTION' with value $OPTARG"
			exit 1
			;;
		esac
	done

	shift $((OPTIND - 1))
	type="$1"
	folder_name="$2"
	category="$3"
}

create_tutorial() {
	test $is_dry_run -eq 0 && hugo new "$path" --editor "$EDITOR"
}

main() {
	local is_dry_run=0
	local type=""
	local date=""
	local folder_name=""
	local category=""

	parse_arguments "$@"

	TYPES=(news tutorial)
	CATEGORIES=("2D" "3D" pcg shaders ai physics ui audio animation vfx tool)

	if [[ $type = tutorial && ! "${CATEGORIES[@]}" =~ "${category}" ]]; then
		echo "Category is incorrect for this tutorial. Try $NAME --help to see available categories. Aborting operation." && exit 1
	fi

	test "$folder_name" = "" && echo "Missing folder_name. Please enter the article's folder_name" && read -r folder_name
	case $type in
	news)
		test "$date" = "" && date=$(date -I)
		path=news/$(date -d "$date" +%Y)/$(date -d "$date" +%m)/"$(path_sanitize "$folder_name")"/index.md
		;;
	tutorial)
		path=tutorial/godot/$category/"$(path_sanitize "$folder_name")"/index.md
		;;
	*)
		echo "Invalid type, should be one of ${TYPES[*]}"
		;;
	esac

	test $is_dry_run -eq 0 && hugo new "$path" --editor "$EDITOR"

	exit $?
}

main "$@"
