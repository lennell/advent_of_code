#!/usr/bin/env ruby

ran, ids = File.read(ARGV[0]).strip.split("\n\n").map { |s| s.split("\n") }
ran = ran.map { |s| s.split('-').map(&:to_i) }
pp(ids.map(&:to_i).count { |n| ran.any? { |min, max| (min..max).cover?(n) } })
