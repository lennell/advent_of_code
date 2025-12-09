#!/usr/bin/env ruby

pp(File.readlines(ARGV[0], chomp: true).map(&:chars).sum do |line|
  12.times.reduce([[], 0]) do |(res, start), i|
    last = line.size - 12 + i
    largest = (start..last).max_by { |k| line[k].to_i }
    [res << line[largest], largest + 1]
  end.first.join.to_i
end)
