# _plugins/mermaid_debug.rb
begin
  require 'jekyll-mermaid'
  Jekyll.logger.info "🔍", "jekyll-mermaid **LOADED**"
rescue LoadError => e
  Jekyll.logger.error "🚨", "jekyll-mermaid NOT loaded: #{e.message}"
end
