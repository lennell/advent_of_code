#!/usr/bin/env ruby

lines = File.readlines(ARGV[0], chomp: true)
grid = lines.flat_map.with_index do |line, y|
  line.chars.flat_map.with_index { |char, x| char == '@' ? [[x, y]] : [] }
end.to_set

nine = [*-1..1].product([*-1..1])
pp(grid.count do |a, b|
  nine.count { |dx, dy| grid.include? [a + dx, b + dy] } <= 4
end)
