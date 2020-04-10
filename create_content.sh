#!/usr/bin/env sh
#
# Creates content pieces for our hugo website.
NAME="create_content"

# Debug
is_dry_run=0

# Main variables
command=""
date=""
filename=""

# UTILS
FORMAT_NORMAL=$(tput sgr0)
FORMAT_BOLD=$(tput bold)
COLOR_RED=$(tput setaf 1)

format_bold() {
	printf "%s%s%s" "$FORMAT_BOLD" "$*" "$FORMAT_NORMAL"
}

echo_error() {
	function_name=$1
	shift
	printf "%s in %s: %s" "$(color_apply red Error)" "$(format_bold "$function_name")" "$*"
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
' "$(format_bold Usage)" "$NAME" "$(format_bold Positional arguments)" "$(format_bold Options)"
	exit 0
}

# Parses the arguments passed to the program.
parse_arguments() {
	# Start with subcommand
	case "$1" in
	-h | --help)
		echo_help
		exit
		;;
	news)
		command="$1"
		shift
		;;
	esac
	test "$command" = "" && echo_error "parse_arguments" "Missing subcommand. Run '$NAME --help' for usage information. Exiting." && exit 1

	arguments=$(getopt --name "$NAME" -o "h,x,d:,n:" -l "help,dry-run,date:,name:" -- "$@")
	eval set -- "$arguments"
	while true; do
		case "$1" in
		-d | --date)
			date=$(date -d "$2" -I)
			test $? -ne 0 && echo "Invalid date. Use a format supported by date, like $(date -I). Exiting" && exit 1
			shift 2
			;;
		-n | --name)
			filename="$2"
			shift 2
			;;
		-x | --dry-run)
			is_dry_run=1
			shift
			;;
		--)
			shift
			break
			;;
		*)
			echo_error "parse_arguments" "Missing option flag. Try '$NAME --help' for more information"
			exit 1
			;;
		esac
	done
}

create_news() {
	test "$date" = "" && date=$(date -I)
	test "$filename" = "" && echo "Missing filename. Please enter the article's filename" && read -r filename
	path=news/$(date -d "$date" +%Y)/$(date -d "$date" +%m)/"$(path_sanitize "$filename")"/index.md
	test $is_dry_run -eq 0 && hugo new "$path" --editor "$EDITOR"
	exit 0
}

# Executes the program.
main() {
	parse_arguments "$@"
	test $? -ne 0 && echo_error "main" "There was an error parsing the command line arguments. Run '$NAME --help' for usage information. Exiting." && exit $?
	test "$command" = "news" && create_news
	exit $?
}

main "$@"
exit $?
