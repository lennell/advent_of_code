#!/usr/bin/env ruby

keep = lambda do |num|
  str = num.to_s
  width = str.size
  half = width / 2
  width.even? && str[...half] == str[half..]
end

pp(File.read(ARGV[0]).scan(/\d+-\d+/).map { |s| s.split('-') }.sum do |a, b|
  (a.to_i..b.to_i).lazy.filter(&keep).sum
end)
