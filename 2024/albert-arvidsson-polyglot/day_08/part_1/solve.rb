#!/usr/bin/env ruby

require_relative '../../../utils'

chars = File.readlines(ARGV[0]).map(&:strip).map(&:chars)
xrange = 0..(chars.first.size - 1)
yrange = 0..(chars.size - 1)
inside = ->(x, y) { xrange.cover?(x) && yrange.cover?(y) }

antennas = {}

chars.each_with_index do |line, y|
  line.each_with_index do |char, x|
    next if char == '.'

    antennas[char] ||= []
    antennas[char] << [x, y]
  end
end

lerp = lambda do |x1, y1, x2, y2, t|
  [((1 - t) * x1) + (t * x2), ((1 - t) * y1) + (t * y2)]
end

antinodes = Set.new

antennas.each_value do |frequencies|
  frequencies.combination(2).each do |((x1, y1), (x2, y2))|
    anti1 = lerp.call(x1, y1, x2, y2, -1)
    anti2 = lerp.call(x1, y1, x2, y2, 2)
    antinodes << anti1 if inside.call(*anti1)
    antinodes << anti2 if inside.call(*anti2)
  end
end

warn(chars.map.with_index do |line, y|
  line.map.with_index do |char, x|
    antinodes.include?([x, y]) ? '#' : char
  end.join
end.join("\n"))

pp antinodes.size
