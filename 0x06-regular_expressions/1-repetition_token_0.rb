#!/usr/bin/env ruby
#match the occurence from 2 to 5 times

puts ARGV[0].scan(/hbt{2,5}n/).join
