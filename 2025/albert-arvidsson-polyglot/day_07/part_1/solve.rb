#!/usr/bin/env ruby

lines = File.readlines(ARGV[0], chomp: true)
lines = lines.map do |line|
  line.chars.each.with_index.with_object(Set.new) do |(char, i), set|
    set.add(i) if char == '^'
  end
end
lines = lines.reject(&:empty?)
lines = lines.reduce([0, lines.first]) do |(count, acc), line|
  splits = acc & line
  beams = acc - line
  tachyons = line.flat_map { |index| [index - 1, index + 1] }.to_set
  [count + splits.size, (beams + tachyons).sort.to_set]
end
pp lines.first
