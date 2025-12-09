#!/usr/bin/env ruby

pp(File.readlines(ARGV[0]).map(&:chop).map(&:chars).transpose
  .map(&:join).reverse.map(&:strip).join("\n").split("\n\n")
  .sum { |col| col.scan(/\d+/).map(&:to_i).reduce(col[-1].to_sym) })
