#!/usr/bin/env ruby

pp(File.readlines(ARGV[0], chomp: true).map(&:strip)
    .reverse
    .map { |line| line.split(/\s+/) }
    .transpose
    .sum { |(op, *arr)| arr.map(&:to_i).reduce(op.to_sym) })
