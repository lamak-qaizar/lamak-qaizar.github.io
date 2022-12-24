module Jekyll
  module ArrayIntersectionFilter
    def intersects(first, second)
      return (first.to_s.split(',').map(&:strip) & second.to_s.split(',').map(&:strip)).size != 0
    end
  end
end

Liquid::Template.register_filter(Jekyll::ArrayIntersectionFilter)