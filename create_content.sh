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
	printf 'Creates content pieces for our hugo website.

%s:
%s type [Options]

Positional arguments must come before option flags.

%s:

type -- Type of content, "news"

%s:
-h/--help             -- Display this help message.
-d/--date             -- (Optional) date override to create news posts
-n/--name             -- File or directory name for the new content
-x/--dry-run          -- Display debug messages without modifying any file
' "$(format_bold Usage)" "$NAME" "$(format_bold Positional arguments)" "$(format_bold Options)"
	exit 0
}

# Parses the arguments passed to the program.
parse_arguments() {
	args=()
	# Handle long options
	for arg; do
		case "$arg" in
		--help) args+=(-h) ;;
		--dry-run) args+=(-d) ;;
		--date) args+=(-d) ;;
		--name) args+=(-n) ;;
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
		n)
			filename="$OPTARG"
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
	command="$1"
}

create_news() {
	test "$date" = "" && date=$(date -I)
	test "$filename" = "" && echo "Missing filename. Please enter the article's filename" && read -r filename
	path=news/$(date -d "$date" +%Y)/$(date -d "$date" +%m)/"$(path_sanitize "$filename")"/index.md
	test $is_dry_run -eq 0 && hugo new "$path" --editor "$EDITOR"
}

# Executes the program.
main() {
	local is_dry_run=0
	local command=""
	local date=""
	local filename=""

	parse_arguments "$@"
	test "$command" = "news" && create_news
	exit $?
}

main "$@"
