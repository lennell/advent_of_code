#!/usr/bin/env ruby

split = ->(stone, at) { [stone[0...at], stone[at..]].map(&:to_i).map(&:to_s) }

stare = lambda do |stone|
  next ['1'] if stone == '0'
  next split.call(stone, stone.size / 2) if stone.size.even?

  (stone.to_i * 2024).to_s
end

blink = lambda do |stones, count|
  count.times.reduce(stones) { |acc, _| acc.flat_map(&stare) }
end

File.read(ARGV[0]).scan(/\d+/)
    .then { |stones| blink.call(stones, 25) }
    .size
    .then(&method(:pp))
