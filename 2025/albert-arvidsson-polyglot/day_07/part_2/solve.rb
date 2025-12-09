#!/usr/bin/env ruby

lines = File.readlines(ARGV[0], chomp: true)
lines = lines.map do |line|
  line.chars.each.with_index.with_object([]) do |(char, i), arr|
    arr << i if char == '^'
  end
end
lines = lines.reject(&:empty?)
lines = lines.reduce({ lines.first.first => 1 }) do |beams, splitters|
  misses = beams.except(*splitters)
  hits = beams.slice(*splitters)
  timelines = hits.each_with_object(misses) do |(b, n), h|
    h[b - 1] ||= 0
    h[b - 1] += n
    h[b + 1] ||= 0
    h[b + 1] += n
  end
  timelines.sort.to_h
end
pp lines.values.sum
