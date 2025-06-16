module Jekyll::Filters
  def sci(input, digits = 2)
    ("%0.#{digits}E" % input).gsub('E', '\\times10^{') + '}'
  end
end
