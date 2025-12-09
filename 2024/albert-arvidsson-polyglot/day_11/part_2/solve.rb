#!/usr/bin/env ruby

solve = lambda do |stones|
  75.times.reduce(stones) do |old, _|
    old.each_with_object(Hash.new(0)) do |(stone, count), hash|
      if stone == '0'
        hash['1'] += count
      elsif stone.size.even?
        half = stone.size / 2
        hash[stone[0...half].to_i.to_s] += count
        hash[stone[half..].to_i.to_s] += count
      else
        hash[(stone.to_i * 2024).to_s] += count
      end
    end
  end
end

File.read(ARGV[0]).scan(/\d+/)
    .group_by(&:itself)
    .transform_values(&:size)
    .then(&solve)
    .values
    .sum
    .then(&method(:pp))
