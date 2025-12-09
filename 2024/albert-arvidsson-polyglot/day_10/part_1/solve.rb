#!/usr/bin/env ruby

require_relative '../../../utils'

grid = File.readlines(ARGV[0], chomp: true)
           .map { |line| line.chars.map(&:to_i) }
range = 0...grid.size

heads = Hash.new { |h, k| h[k] = Set.new }
grid.each_with_index do |line, y|
  line.each_with_index do |value, x|
    heads[[x, y]] if value.zero?
  end
end

neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]

res = heads.each do |head, set|
  set.merge((1..9).reduce([head]) do |acc, i|
    break [] if acc.empty?

    acc.flat_map do |x, y|
      neighbours.flat_map do |(dx, dy)|
        nx = x + dx
        ny = y + dy
        next [] unless range.cover?(nx) && range.cover?(ny)

        grid[ny][nx] == i ? [[nx, ny]] : []
      end
    end
  end)
end

pp res.values.map(&:size).sum
