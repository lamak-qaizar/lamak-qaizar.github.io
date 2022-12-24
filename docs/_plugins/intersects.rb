module Jekyll
  module ArrayIntersectionFilter
    def intersects(first, second)
      return (first & second).size != 0
    end
  end
end

Liquid::Template.register_filter(Jekyll::ArrayIntersectionFilter)