#!/usr/bin/env ruby

reduce = lambda do |(times, angle), num|
  num.abs.times do
    angle = (angle + (num / num.abs)) % 100
    times += 1 if angle.zero?
  end
  [times, angle]
end
pp(File.read(ARGV[0]).gsub('L', '-').scan(/-?\d+/).map(&:to_i)
       .reduce([0, 50], &reduce).first)
