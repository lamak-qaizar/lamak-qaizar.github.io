# Borrowed from https://ognjen.io/flatten-plugin-for-jekyll/

module Jekyll
  module Flattener
    module FlattenerFilter
      def flatten(input)
        return input.flatten
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::Flattener::FlattenerFilter)