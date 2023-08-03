#!/usr/bin/env ruby
# A regular expression that matches a given pattern

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit(1)
end

# Extract the input string from the command-line argument
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /hbt+n/

# Match the pattern in the input string
match_result = input_string.match(pattern)

# Output the matched result or an empty string if no match found
puts match_result ? match_result[0] : ""

