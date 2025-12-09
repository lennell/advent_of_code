#!/usr/bin/env ruby

solve = lambda do |(ax, ay, bx, by, px, py)|
  (0..100).to_a.product((0..100).to_a).find do |a, b|
    (a * ax) + (b * bx) == px && (a * ay) + (b * by) == py
  end
end

pp(File.read(ARGV[0]).scan(/\d+/).map(&:to_i).each_slice(6).map(&solve).compact
  .sum { |a, b| (a * 3) + b })
