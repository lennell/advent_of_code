#!/usr/bin/env ruby

pp(File.readlines(ARGV[0], chomp: true).map(&:chars).sum do |line|
  (0..(line.size - 2)).map do |i|
    [line[i].to_i, line[(i + 1)..].map(&:to_i).max].join.to_i
  end.max
end)
